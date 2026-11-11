# Ktemia API docs

Search and compare flights, hotels, and car rentals from airlines and booking sites in one API. Each result names the seller, the price, and a booking link. Ktemia compares; the traveller books on the seller's site.

The canonical docs, with a live playground and code in seven languages, are at **[ktemia.com/docs/api](https://www.ktemia.com/docs/api/)**. This repository is generated from them, so coding agents and readers on GitHub get the same contract.

## Quickstart

1. Get a key at [app.ktemia.com](https://app.ktemia.com). The Free plan includes 100 API requests a month.
2. Send it as `X-API-Key` on every request to `https://api.ktemia.com`, from a server.
3. Start a search, then read the results:

```bash
curl https://api.ktemia.com/flights/search \
  -H "X-API-Key: $KTEMIA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"origin": "JFK", "destination": "LAX", "departureDate": "2026-12-05"}'
# -> {"searchToken": "...", "expiresIn": 3600}

curl "https://api.ktemia.com/flights/results?token=SEARCH_TOKEN" -H "X-API-Key: $KTEMIA_API_KEY"
```

Every vertical works the same way: a search returns a token, results pages through offers, details expands one offer into every seller's price and booking URL.

## Contents

- [Introduction](docs/introduction.md): base URL, authentication, errors, pagination
- [Getting started](docs/getting-started.md)
- [Filter by provider](docs/guides/filter-by-provider.md): every airline, booking site, and rental company id

### Flights

- [Search airports](docs/flights/airports.md)
- [Search airlines](docs/flights/airlines.md)
- [Search flights](docs/flights/search.md)
- [List results](docs/flights/results.md)
- [Retrieve flight details](docs/flights/details.md)

### Hotels

- [Search locations](docs/hotels/locations.md)
- [Search hotels](docs/hotels/search.md)
- [List results](docs/hotels/results.md)
- [Retrieve hotel details](docs/hotels/details.md)
- [Hotel reviews](docs/hotels/reviews.md)

### Cars

- [Search locations](docs/cars/locations.md)
- [Search cars](docs/cars/search.md)
- [List results](docs/cars/results.md)
- [Retrieve car details](docs/cars/details.md)

### Objects

- [The Flight object](docs/objects/flight.md)
- [The Booking option object](docs/objects/booking-option.md)
- [The Hotel object](docs/objects/hotel.md)
- [The Hotel booking option object](docs/objects/hotel-booking-option.md)
- [The Hotel review object](docs/objects/hotel-review.md)
- [The Car object](docs/objects/car.md)
- [The Car booking option object](docs/objects/car-booking-option.md)

### Examples

- [hotel_prices.py](examples/hotel_prices.py): search, read the booking sites, filter to two, compare every seller
- [hotel_prices.mjs](examples/hotel_prices.mjs): a search priced by one booking site, in JavaScript

## Use it from a coding agent

- Skills for Claude Code, Codex, and Cursor: [Ktemiaa/ktemia-skills](https://github.com/Ktemiaa/ktemia-skills)
- `llms.txt`: [https://www.ktemia.com/docs/api/llms.txt](https://www.ktemia.com/docs/api/llms.txt)

## Links

- [API reference](https://www.ktemia.com/docs/api/) · [Providers](https://www.ktemia.com/providers/) · [Pricing](https://www.ktemia.com/pricing/) · [Blog](https://www.ktemia.com/blog/)
- Guides: [hotel price API](https://www.ktemia.com/blog/hotel-price-api/), [flight search API](https://www.ktemia.com/blog/flight-search-api/), [car rental API](https://www.ktemia.com/blog/car-rental-api/)

Questions: contact@ktemia.com

## License

MIT. See [LICENSE](LICENSE).
