# Introduction

> Canonical, always current: [ktemia.com/docs/api/](https://www.ktemia.com/docs/api/). This repository is generated from it.


One travel API for flights, hotels and car rentals: search, compare every seller’s price and get booking links. Examples in 7 languages and a free plan.

A travel API for search and compare: flights, hotels, and car rentals in one contract. Describe a trip and get the providers who can sell it, with prices. Booking stays with the provider.

Ktemia is a travel search API. You describe a trip for a person. The response is the providers who can sell it: airlines, agencies, and other sellers, with prices you can compare.

The API does not issue a ticket, take payment, or hold a reservation. When you open an offer, the response includes that provider’s URL. The person books on the provider’s site.

Choosing between providers first? [Travel APIs compared by who gives you a key](https://www.ktemia.com/blog/best-travel-api/) covers Amadeus, Skyscanner, Booking.com Demand, Expedia Rapid, CarTrawler, and Ktemia.

## Flights API

Turn a place into an airport or city code with [Search airports](https://www.ktemia.com/docs/api/flights/airports/) and an airline name into a code with [Search airlines](https://www.ktemia.com/docs/api/flights/airlines/). Search one-way, round trip, or multi-city with 2 to 6 legs, and get every seller’s fare with a booking link. Start with the [flight search API](https://www.ktemia.com/docs/api/flights/search/).

## Hotel API

Turn a city, neighbourhood, or property name into a location id, search by dates and guests, and compare every booking site’s price for each hotel, with guest reviews. Start with the [hotel API](https://www.ktemia.com/docs/api/hotels/search/).

## Car rental API

Find a pickup location, search by dates, and compare rental companies and booking sites for each car. Narrow results to named rental companies with `agencies`. Start with the [car rental API](https://www.ktemia.com/docs/api/cars/search/).

## Base URL

Every request goes to `https://api.ktemia.com`. There is no version prefix. The API is HTTPS only.

Send JSON, and you get JSON back. A search is `POST` with a body. A read that follows a search is `GET` with query parameters.

## Providers

Each offer names the provider and the price, so you can show a person the choices side by side. The booking link opens that provider’s site with the trip filled in. Leave the URL as the API returned it.

To get data from one provider only, filter the search: `airlines` on flights, `providers` on hotels and cars, and `agencies` on cars. [Providers](https://www.ktemia.com/providers/) lists every airline, booking site, and rental company we have seen, with the id to send.

Look up an airport or city code with [Search airports](https://www.ktemia.com/docs/api/flights/airports/), and an airline code with [Search airlines](https://www.ktemia.com/docs/api/flights/airlines/). Then start a flight search at [Search flights](https://www.ktemia.com/docs/api/flights/search/). For a car hire, look up a place with [Search locations](https://www.ktemia.com/docs/api/cars/locations/), then start at [Search cars](https://www.ktemia.com/docs/api/cars/search/). For a stay, look up a place with [Search locations](https://www.ktemia.com/docs/api/hotels/locations/), then start at [Search hotels](https://www.ktemia.com/docs/api/hotels/search/). Authentication, errors, and pagination are the sections below. They apply to every call.

## Read more

How Ktemia compares with other travel APIs, by who can get a key: [best travel API in 2026](https://www.ktemia.com/blog/best-travel-api/). Why a search API is not a GDS or a booking engine: [GDS vs booking engine vs a search API](https://www.ktemia.com/blog/search-api-vs-gds-booking-engine/). Search from Claude Code, Cursor, or Codex with the open-source [Ktemia skills](https://github.com/Ktemiaa/ktemia-skills) (`flight-search`, `car-search`, `hotel-search`): `/plugin marketplace add Ktemiaa/ktemia-skills`, then `/plugin install ktemia@ktemia`.

## Authentication

Every request requires an API key. Create one in the [dashboard](https://app.ktemia.com), then send it on every call.

### The header

Pass `X-API-Key: <your key>`. A missing key answers `401 MISSING_API_KEY`. A bad key answers `401 INVALID_API_KEY`. Both include `{"success": false, "error": {"code", "message"}, "data": null}`.

Keys are secrets. Keep them in an environment variable on a server. The playground on this site keeps a key in this browser tab so you can try a call. Do not put a key in the JavaScript of your own app.

### HTTPS only

The API is HTTPS only. Call it from your server. This site’s playground is allowed to call it from the browser; other websites are not.

## Errors

Success responses are the JSON shown on each endpoint. Errors use one shape: a missing key, a bad body, an empty search, an expired token.

### The envelope

`error.code` is stable and uppercase. `error.message` is safe to show. `error.param` is the field to highlight when the input was wrong (`departureDate`, `legs[1].date`, `airlines[0]`). It is omitted when the failure is not about a field.

Unknown fields are rejected. The response names the field in `error.param`.

### Status codes

`400` - the request is malformed (`MISSING_FIELD`, `TRIP_CONFLICT`, `INVALID_ORIGIN`, `INVALID_LOCATION`, `LEGS_OUT_OF_ORDER`, `INVALID_SEARCH_TOKEN`, …).

`401` - missing or invalid API key.

`404` - `NO_RESULTS` on search (the trip is valid, nothing published), or `NO_MORE_RESULTS` on a page past the end.

`410` - `SEARCH_EXPIRED`. The token was valid and is now gone. Start a new search; retrying this one will not help.

`429` - rate limit or a temporary block after repeated auth failures. Honour `Retry-After`.

`502` - `SEARCH_FAILED`, `DETAILS_FAILED`, `AIRPORTS_UNAVAILABLE`, `AIRLINES_UNAVAILABLE`, `LOCATIONS_UNAVAILABLE`, `REVIEWS_UNAVAILABLE`, or `UPSTREAM_ERROR`. Temporary. Retry the same request.

## Pagination

Each search is fixed for 60 minutes. `/flights/results`, `/cars/results`, and `/hotels/results` read the next page of that search. Page 2 does not repeat page 1. Hotel reviews are separate: they take a hotel id and do not expire with the search.

### Tokens, not page numbers

`/flights/search`, `/cars/search`, and `/hotels/search` return `searchToken` for page 1. Each results response that is not the last page includes `nextToken`. Send that as the `token` query parameter. Flights and cars return 20 per page. Hotels return up to 30. You cannot request a page by number. Hotel reviews are the exception: `/hotels/reviews` takes `page`, 10 reviews at a time.

A token that is not valid answers `400 INVALID_SEARCH_TOKEN`. A token that has expired answers `410 SEARCH_EXPIRED`. Start a new search.

### totalResults

`totalResults` is how many itineraries, cars, or hotels the search contains. `hasMore` is true when another page exists. The last page omits `nextToken`. Requesting a page after that returns `404 NO_MORE_RESULTS`.

Docs: https://www.ktemia.com/docs/api/

## Flights

`GET /flights/airports?query=` returns airport and city codes. Send `code` as origin or destination. `allAirports: true` is a city code such as NYC or LON.
`GET /flights/airlines?query=` returns 2-character airline codes. Send `code` in the `airlines` array on a flight search.
`POST /flights/search` starts a search and returns a searchToken. It does not return offers. One-way is origin, destination, and departureDate. Round trip adds returnDate. Multi-city sends `legs` (2 to 6) and does not send the flat fields in the same body.
`GET /flights/results?token=` returns a page of 20 offers. Use nextToken for the following page.
`GET /flights/details?token=&resultId=` returns one itinerary, including each provider booking URL.

## Skill

Claude Code, Cursor, and Codex can search with the Ktemia skills: `flight-search`, `car-search`, and `hotel-search`.
https://github.com/Ktemiaa/ktemia-skills

Install in Claude Code:

```
/plugin marketplace add Ktemiaa/ktemia-skills
/plugin install ktemia@ktemia
```

Set `KTEMIA_API_KEY` in the environment. The flight skill looks up airport codes, asks when a name matches several cities, and returns each seller’s booking URL. It does not book tickets. Do not guess origin, destination, or dates.

## Cars

`GET /cars/locations?query=` returns pickup ids. Send `locationId` as pickupLocation.
`POST /cars/search` starts a search and returns a searchToken. It does not return cars. Required fields are pickupLocation, pickupDate, and dropoffDate.
`GET /cars/results?token=` returns a page of 20 cars. Use nextToken for the following page.
`GET /cars/details?token=&resultId=` returns one car, including each provider booking URL.

## Hotels

`GET /hotels/locations?query=` returns place ids. Send `locationId` as location. A named hotel also returns `hotelId`, which is for reviews.
`POST /hotels/search` starts a search and returns a searchToken. It does not return hotels. Required fields are location, checkin, and checkout. Prices come back in the country’s native currency.
`GET /hotels/results?token=` returns a page of up to 30 hotels. Use nextToken for the following page.
`GET /hotels/details?token=&resultId=` returns one hotel, including each provider booking URL and up to 5 recent reviews.
`GET /hotels/reviews?hotelId=` pages guest reviews, 10 at a time. It does not need a search token.

Each endpoint page lists every parameter, the allowed values, and a captured example.

https://www.ktemia.com/docs/api/flights/search/
https://www.ktemia.com/docs/api/cars/search/
https://www.ktemia.com/docs/api/hotels/search/

## Docs index

Every page of the docs. Append `.md` to a URL (without the trailing slash) for the Markdown version.

### Guides

- [Getting started](https://www.ktemia.com/docs/getting-started/): Call the live flights, cars, and hotels APIs: POST search, GET results, GET details. Same compare job as the dashboard and the copilot.
- [MCP server](https://www.ktemia.com/docs/mcp/): Run the Ktemia MCP server in Cursor, Claude Code, Claude Desktop, or Codex. Seven read-only tools for flights, hotels, and cars.
- [Required fields](https://www.ktemia.com/docs/copilot/): If a field is missing, the copilot asks and the API names it. Neither invents a city or a day.
- [API changelog](https://www.ktemia.com/docs/changelog/): Dated changes to the Ktemia flights, hotels, and cars APIs: new endpoints, filters, limits, and tooling.

### Reference

- [Introduction](https://www.ktemia.com/docs/api/): One travel API for flights, hotels and car rentals: search, compare every seller’s price and get booking links. Examples in 7 languages and a free plan.
- [Check key status](https://www.ktemia.com/docs/api/key/): Read the plan, rate limits, and remaining monthly quota for an API key. Not metered, so checking costs nothing. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.

### Flights

- [Search airports](https://www.ktemia.com/docs/api/flights/airports/): Look up an airport or city code by name. Use the code as origin or destination on a flight search. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.
- [Search airlines](https://www.ktemia.com/docs/api/flights/airlines/): Look up an airline code by name. Use the code on airlines when you search flights. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.
- [Search flights](https://www.ktemia.com/docs/api/flights/search/): Start a flight search: one-way, round trip, or multi-city. Returns a token, not results. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.
- [List results](https://www.ktemia.com/docs/api/flights/results/): Fetch a page of flight data for a search: 20 itineraries, a nextToken, an exact total. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.
- [Retrieve flight details](https://www.ktemia.com/docs/api/flights/details/): Expand one itinerary into every fare, with a URL that opens the seller’s booking page. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.

### Hotels

- [Search locations](https://www.ktemia.com/docs/api/hotels/locations/): Hotel API location lookup in Python, JavaScript, Go, Ruby, Java, and PHP. Turn a city, neighbourhood, or property name into the id a hotel search accepts. cURL included.
- [Search hotels](https://www.ktemia.com/docs/api/hotels/search/): Hotel API and stays API in Python, JavaScript, Go, Ruby, Java, and PHP. Start a hotel search for a city and dates. Returns a token, not results. cURL included.
- [List results](https://www.ktemia.com/docs/api/hotels/results/): Hotel API results in Python, JavaScript, Go, Ruby, Java, and PHP. Fetch a page of up to 30 hotels, a nextToken, and an exact total. cURL included.
- [Retrieve hotel details](https://www.ktemia.com/docs/api/hotels/details/): Hotel API details in Python, JavaScript, Go, Ruby, Java, and PHP. Expand one hotel into every seller, with a URL that opens that booking site. cURL included.
- [Hotel reviews](https://www.ktemia.com/docs/api/hotels/reviews/): Hotel reviews API in Python, JavaScript, Go, Ruby, Java, and PHP. Page guest reviews for one hotel by date, score, traveller, month, or source. cURL included.

### Cars

- [Search locations](https://www.ktemia.com/docs/api/cars/locations/): Car rental API location lookup in Python, JavaScript, Go, Ruby, Java, and PHP. Turn a city or airport name into the id a car hire search accepts. cURL included.
- [Search cars](https://www.ktemia.com/docs/api/cars/search/): Car rental API, rentals API, and car hire API in Python, JavaScript, Go, Ruby, Java, and PHP. Start a rental cars search for a pickup and dates. Returns a token, not results. cURL included.
- [List results](https://www.ktemia.com/docs/api/cars/results/): Car rental API and rentals API results in Python, JavaScript, Go, Ruby, Java, and PHP. Fetch a page of 20 cars, a nextToken, and an exact total. cURL included.
- [Retrieve car details](https://www.ktemia.com/docs/api/cars/details/): Car hire API details in Python, JavaScript, Go, Ruby, Java, and PHP. Expand one car into every seller, with a URL that opens that booking site. cURL included.

### Objects

- [The Flight object](https://www.ktemia.com/docs/api/objects/flight/): One itinerary: legs, segments, and the fares on it.
- [The Booking option object](https://www.ktemia.com/docs/api/objects/booking-option/): A fare on an itinerary, with bags, amenities, and a provider URL.
- [The Car object](https://www.ktemia.com/docs/api/objects/car/): One vehicle: the car, the desk, and the sellers on it.
- [The Car booking option object](https://www.ktemia.com/docs/api/objects/car-booking-option/): A seller for a car, with terms and a provider URL.
- [The Hotel object](https://www.ktemia.com/docs/api/objects/hotel/): One property: the stay, the place, and the cheapest seller.
- [The Hotel booking option object](https://www.ktemia.com/docs/api/objects/hotel-booking-option/): A seller for a stay, with a provider URL.
- [The Hotel review object](https://www.ktemia.com/docs/api/objects/hotel-review/): One guest review, scored on the same 0–10 scale as the hotel.

### Machine-readable

- [OpenAPI spec](https://www.ktemia.com/openapi.json): OpenAPI 3.1 contract for every public endpoint.
- [AGENTS.md](https://www.ktemia.com/AGENTS.md): Setup, auth, rules, and errors for coding agents.
- [APIs.json profile](https://www.ktemia.com/apis.yml): Every machine-readable resource for the API, also as [JSON](https://www.ktemia.com/apis.json).
- [API catalog](https://www.ktemia.com/.well-known/api-catalog): RFC 9727 well-known catalog.
- [Site llms.txt](https://www.ktemia.com/llms.txt): Product, use cases, docs, and blog.
