# Search flights

> Canonical, always current: [ktemia.com/docs/api/flights/search/](https://www.ktemia.com/docs/api/flights/search/). This repository is generated from it.


Start a flight search: one-way, round trip, or multi-city. Returns a token, not results. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.

Base URL: https://api.ktemia.com
Authentication: send header `X-API-Key` on every request.

`POST /flights/search`

Start a search. Returns a token, not results.

This call returns a `searchToken`. It does not return flights. A domestic one-way usually answers in 2–5 seconds; a long-haul can take longer.

## Country and currency

Send `country` to pick the market. Prices come back in that country’s native currency. `GB` returns GBP, `DE` returns EUR, `US` returns USD. Omit `country` and the market is the US, so prices are USD.

There is no `currency` field on this call. Sending one is rejected. You cannot ask for US prices in GBP, or UK prices in USD - the country decides the currency.

## One-way, round trip, multi-city

Send `origin`, `destination`, and `departureDate` for a one-way. Add `returnDate` for a round trip. Send `legs` instead for multi-city. Mixing the two forms answers `400 TRIP_CONFLICT`. A `legs` array of length 1 answers `400 TOO_FEW_LEGS` - use the flat form.

Origin and destination are codes, not names. Look them up with [Search airports](https://www.ktemia.com/docs/api/flights/airports/) and send `code`. A code with `allAirports` true (`NYC`, `LON`) covers every airport in that city. Origin and destination on a single leg must differ.

## When there is nothing to page

If there are no flights, the call returns `404 NO_RESULTS` and no token. Schedules are usually published under a year ahead, so a date further out is the usual cause.

## Flights from one airline

Send `airlines` with 2-letter IATA codes, for example `["UA"]` for United. Every itinerary in the results then uses only those airlines. Find a code with [Search airlines](https://www.ktemia.com/docs/api/flights/airlines/), or pick an airline on [Providers](https://www.ktemia.com/providers/#airlines) to open this page with the filter already in the examples.

## Read more

What a flight search API does, and what it does not: [flight search API](https://www.ktemia.com/blog/flight-search-api/). Moving from another provider: [Kiwi Tequila API](https://www.ktemia.com/blog/kiwi-tequila-api/), [Amadeus API vs Skyscanner API](https://www.ktemia.com/blog/amadeus-api-vs-skyscanner-api/), and why there is no [Google Flights API](https://www.ktemia.com/blog/google-flights-api/). Claude Code skill: [Ktemiaa/ktemia-skills](https://github.com/Ktemiaa/ktemia-skills).

## Body parameters

- `origin` (string, optional): IATA airport or city code, 3 or 4 letters. Required for a one-way or round trip. Do not send it together with legs. Look the code up with [Search airports](https://www.ktemia.com/docs/api/flights/airports/) and send `code` from that response.
- `destination` (string, optional): IATA airport or city code. Required when origin is set, and it must be different from origin. Look the code up with [Search airports](https://www.ktemia.com/docs/api/flights/airports/) and send `code` from that response.
- `departureDate` (string, optional): Outbound date, YYYY-MM-DD. Required when origin is set. Cannot be in the past. Schedules are usually published under a year ahead.
- `returnDate` (string, optional): Return date, YYYY-MM-DD. Sending it makes the search a round trip. Cannot be before departureDate. Omit it for a one-way.
- `legs` (array of objects, optional): Multi-city trip. Send 2 to 6 legs, in travel order. Do not send origin, destination, departureDate, or returnDate in the same request. One leg is not enough - use the flat fields for a one-way.
  - `origin` (string, required): IATA airport or city code, 3 or 4 letters. Look the code up with [Search airports](https://www.ktemia.com/docs/api/flights/airports/). Airport codes such as JFK and city codes such as NYC are both accepted.
  - `destination` (string, required): IATA airport or city code. Must be different from origin on this same leg. Look the code up with [Search airports](https://www.ktemia.com/docs/api/flights/airports/).
  - `date` (string, required): Departure date for this leg, YYYY-MM-DD. Cannot be in the past, and cannot be earlier than the previous leg.
- `cabin` (string, optional): Which cabin to search. Defaults to economy.
  - `economy` - Default. Results can include every cabin.
  - `premiumEconomy` - Only premium economy fares.
  - `business` - Only business fares.
  - `first` - Only first fares.
- `passengers` (object, optional): How many travellers of each fare type. Defaults to one adult. The counts added together must be at least 1 and at most 9.
  - `adults` (integer, optional): Ages 18–64. Defaults to 1. Each count is 0–9, and all counts together must be at least 1 and at most 9.
  - `seniors` (integer, optional): Ages 65 and over. Defaults to 0.
  - `students` (integer, optional): Ages 18 and over, on a student fare. Defaults to 0.
  - `youths` (integer, optional): Ages 12–17. Defaults to 0.
  - `children` (integer, optional): Ages 2–11. Defaults to 0.
  - `infantsInSeat` (integer, optional): Under 2, in their own seat. Defaults to 0.
  - `infantsOnLap` (integer, optional): Under 2, on a lap. Defaults to 0. Cannot be higher than adults + seniors + students.
- `maxStops` (integer, optional): How many stops to allow. Omit it to allow any number of stops.
  - `0` - Nonstop only.
  - `1` - At most one stop.
  - `2` - At most two stops.
- `airlines` (array of strings, optional): IATA airline codes to keep, 2 characters each, for example ["B6", "DL"]. Look a name up with [Search airlines](https://www.ktemia.com/docs/api/flights/airlines/) and send `code`. Send 1 to 20 codes. Every itinerary in the results uses only these airlines. Omit it to allow any airline.
- `alliances` (array of strings, optional): Alliances to keep. Send one or more. Every itinerary in the results belongs to one of them.
  - `oneworld` - oneworld carriers only.
  - `skyteam` - SkyTeam carriers only.
  - `starAlliance` - Star Alliance carriers only.
- `maxPrice` (integer, optional): Highest per-person fare to return, as a whole number in the country’s native currency. Minimum is 1. Omit it for no price cap.
- `sortBy` (string, optional): How to order the results. Defaults to bestValue.
  - `bestValue` - Default. Recommended order.
  - `price` - By fare.
  - `duration` - By total travel time.
  - `departure` - By departure time.
  - `arrival` - By arrival time.
- `sortOrder` (string, optional): Direction for sortBy. Defaults to asc.
  - `asc` - Default. Lowest price, shortest time, or earliest time first.
  - `desc` - The other direction.
- `country` (string, optional): ISO 3166-1 alpha-2 market. Prices come back in that country’s native currency - GB returns GBP, DE returns EUR, US returns USD. There is no separate currency field; sending `currency` is rejected. Omit country for US. Any other value is rejected.
  - `US` - Prices in USD.
  - `GB` - Prices in GBP.
  - `DE` - Prices in EUR.
  - `FR` - Prices in EUR.
  - `ES` - Prices in EUR.
  - `IT` - Prices in EUR.
  - `NL` - Prices in EUR.
  - `BE` - Prices in EUR.
  - `AT` - Prices in EUR.
  - `CH` - Prices in CHF.
  - `IE` - Prices in EUR.
  - `PT` - Prices in EUR.
  - `GR` - Prices in EUR.
  - `PL` - Prices in PLN.
  - `CZ` - Prices in CZK.
  - `RO` - Prices in EUR.
  - `SE` - Prices in SEK.
  - `NO` - Prices in NOK.
  - `DK` - Prices in DKK.
  - `FI` - Prices in EUR.
  - `TR` - Prices in TRY.
  - `AE` - Prices in AED.
  - `SA` - Prices in SAR.
  - `IL` - Prices in ILS.
  - `IN` - Prices in INR.
  - `JP` - Prices in JPY.
  - `KR` - Prices in KRW.
  - `HK` - Prices in HKD.
  - `TW` - Prices in TWD.
  - `SG` - Prices in SGD.
  - `MY` - Prices in MYR.
  - `TH` - Prices in THB.
  - `ID` - Prices in IDR.
  - `PH` - Prices in PHP.
  - `VN` - Prices in VND.
  - `AU` - Prices in AUD.
  - `NZ` - Prices in NZD.
  - `CA` - Prices in CAD.
  - `MX` - Prices in MXN.
  - `BR` - Prices in BRL.
  - `AR` - Prices in ARS.
  - `CL` - Prices in CLP.
  - `CO` - Prices in COP.
  - `PE` - Prices in PEN.
  - `UY` - Prices in USD.
  - `PY` - Prices in USD.
  - `BO` - Prices in USD.
  - `EC` - Prices in USD.
  - `VE` - Prices in USD.
  - `CR` - Prices in USD.
  - `PA` - Prices in USD.
  - `GT` - Prices in USD.
  - `HN` - Prices in USD.
  - `NI` - Prices in USD.
  - `SV` - Prices in USD.
  - `DO` - Prices in USD.
  - `PR` - Prices in USD.
  - `ZA` - Prices in ZAR.
  - `UA` - Prices in UAH.

## Response fields

- `searchToken` (string, required): Opaque handle for this search. Pass it to `/flights/results` for page 1, and to `/flights/details` with a flight `id`. Valid for 60 minutes.
- `expiresIn` (integer, required): Seconds remaining until the token expires, starting at `3600`.

## Example: One-way

`POST /flights/search` → 200

Request:

```json
{
  "origin": "JFK",
  "destination": "LAX",
  "departureDate": "2026-12-03",
  "returnDate": null,
  "legs": null,
  "cabin": "economy",
  "passengers": {
    "adults": 1,
    "seniors": 0,
    "students": 0,
    "youths": 0,
    "children": 0,
    "infantsInSeat": 0,
    "infantsOnLap": 0
  },
  "maxStops": null,
  "airlines": null,
  "alliances": null,
  "maxPrice": null,
  "sortBy": "bestValue",
  "sortOrder": "asc",
  "country": null
}
```

Response:

```json
{
  "searchToken": "eyJwIjoxLCJzIjoiNDk1NGMzNmY2ZWY1NDdiYWI4NTI3YzA3ZTBlOWNjZjMiLCJ2IjoxfQ",
  "expiresIn": 3600
}
```

## Example: Round trip

`POST /flights/search` → 200

Request:

```json
{
  "origin": "JFK",
  "destination": "LHR",
  "departureDate": "2026-12-03",
  "returnDate": "2026-12-10",
  "legs": null,
  "cabin": "economy",
  "passengers": {
    "adults": 2,
    "seniors": 0,
    "students": 0,
    "youths": 0,
    "children": 0,
    "infantsInSeat": 0,
    "infantsOnLap": 0
  },
  "maxStops": 0,
  "airlines": null,
  "alliances": null,
  "maxPrice": null,
  "sortBy": "bestValue",
  "sortOrder": "asc",
  "country": null
}
```

Response:

```json
{
  "searchToken": "eyJwIjoxLCJzIjoiODRiZjZlYzU3ZGQyNDJkZDk4NmZhNzAzM2JhY2I3ODkiLCJ2IjoxfQ",
  "expiresIn": 3600
}
```

## Example: Multi-city

`POST /flights/search` → 200

Request:

```json
{
  "origin": null,
  "destination": null,
  "departureDate": null,
  "returnDate": null,
  "legs": [
    {
      "origin": "JFK",
      "destination": "LAX",
      "date": "2026-12-03"
    },
    {
      "origin": "LAX",
      "destination": "SFO",
      "date": "2026-12-10"
    },
    {
      "origin": "SFO",
      "destination": "JFK",
      "date": "2026-12-17"
    }
  ],
  "cabin": "economy",
  "passengers": {
    "adults": 1,
    "seniors": 0,
    "students": 0,
    "youths": 0,
    "children": 0,
    "infantsInSeat": 0,
    "infantsOnLap": 0
  },
  "maxStops": null,
  "airlines": null,
  "alliances": null,
  "maxPrice": null,
  "sortBy": "price",
  "sortOrder": "asc",
  "country": null
}
```

Response:

```json
{
  "searchToken": "eyJwIjoxLCJzIjoiZjVmZDc1YzM4NTM5NDhkZGE2ZjAyZjE3MDQ3ZjNmM2EiLCJ2IjoxfQ",
  "expiresIn": 3600
}
```

## Skill

Claude Code, Cursor, and Codex can search with the Ktemia skills: `flight-search`, `car-search`, and `hotel-search`.
https://github.com/Ktemiaa/ktemia-skills

Install in Claude Code:

```
/plugin marketplace add Ktemiaa/ktemia-skills
/plugin install ktemia@ktemia
```

Set `KTEMIA_API_KEY` in the environment. The flight skill looks up airport codes, asks when a name matches several cities, and returns each seller’s booking URL. It does not book tickets. Do not guess origin, destination, or dates.

Docs: https://www.ktemia.com/docs/api/flights/search/
