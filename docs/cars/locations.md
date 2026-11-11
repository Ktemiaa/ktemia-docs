# Search locations

> Canonical, always current: [ktemia.com/docs/api/cars/locations/](https://www.ktemia.com/docs/api/cars/locations/). This repository is generated from it.


Car rental API location lookup in Python, JavaScript, Go, Ruby, Java, and PHP. Turn a city or airport name into the id a car hire search accepts. cURL included.

Base URL: https://api.ktemia.com
Authentication: send header `X-API-Key` on every request.

`GET /cars/locations`

Find the location ids a car search accepts.

Pickup and dropoff on a car search are location ids, not names. This call turns a name or a code into the `locationId` you send as `pickupLocation` or `dropoffLocation`.

Send `X-API-Key` the same way as on every other call. `query` is required. `type` defaults to city. `country` and `locale` default to US and `en`.

## Which id to send

Use `locations[].locationId`. A city id is numeric (`22863` is Austin, Texas). An airport id is often the IATA code. The same place can appear twice - once as a city, once as an airport - with the same id.

A query that matches nothing returns `200` with an empty `locations` list. A missing `query`, a blank `query`, a bad `locale`, or an unsupported `country` returns `400`. If the lookup itself fails, the response is `502 LOCATIONS_UNAVAILABLE`.

## Read more

What a car rental search API does, and what it does not: [car rental API](https://www.ktemia.com/blog/car-rental-api/). Why one search lists several sellers for the same car: [car rental aggregator API](https://www.ktemia.com/blog/car-rental-aggregator-api/).

## Query parameters

- `query` (string, required): City name, airport name, or code. 1 to 80 characters. A blank value is rejected.
- `type` (string, optional): Which places to return. Defaults to city.
  - `city` - Default. Cities, and city-level airport matches.
  - `airport` - Airports only.
  - `all` - Cities and airports.
- `country` (string, optional): ISO 3166-1 alpha-2 market. Omit it for US. Any other value is rejected. Same set as on a car search.
  - `US`
  - `GB`
  - `DE`
  - `FR`
  - `ES`
  - `IT`
  - `NL`
  - `BE`
  - `AT`
  - `CH`
  - `IE`
  - `PT`
  - `GR`
  - `PL`
  - `CZ`
  - `RO`
  - `SE`
  - `NO`
  - `DK`
  - `FI`
  - `TR`
  - `AE`
  - `SA`
  - `IL`
  - `IN`
  - `JP`
  - `KR`
  - `HK`
  - `TW`
  - `SG`
  - `MY`
  - `TH`
  - `ID`
  - `PH`
  - `VN`
  - `AU`
  - `NZ`
  - `CA`
  - `MX`
  - `BR`
  - `AR`
  - `CL`
  - `CO`
  - `PE`
  - `UY`
  - `PY`
  - `BO`
  - `EC`
  - `VE`
  - `CR`
  - `PA`
  - `GT`
  - `HN`
  - `NI`
  - `SV`
  - `DO`
  - `PR`
  - `ZA`
  - `UA`
- `locale` (string, optional): 2-letter language code. Omit it for `en`. Anything that is not two letters is rejected.

## Response fields

- `query` (string, required): The query you sent, with surrounding spaces removed.
- `locations` (array of objects, required): Matching places, best match first. Empty when nothing matches.
  - `locationId` (string, required): Id to send as `pickupLocation` or `dropoffLocation` on [Search cars](https://www.ktemia.com/docs/api/cars/search/). A city id is numeric. An airport id is often the IATA code.
  - `name` (string, optional): Full display name.
  - `city` (string, optional): City.
  - `country` (string, optional): Country name.
  - `countryCode` (string, optional): ISO 3166-1 alpha-2 country code.
  - `locationType` (string, optional): `city` or `airport`.
  - `airportCode` (string, optional): IATA airport code when this place is tied to an airport.
  - `timezone` (string, optional): IANA timezone, for example `America/Chicago`.

## Example: Austin

`GET /cars/locations` → 200

Request:

```json
{
  "query": "austin"
}
```

Response:

```json
{
  "query": "austin",
  "locations": [
    {
      "locationId": "22863",
      "name": "Austin, Texas, United States",
      "city": "Austin",
      "country": "United States",
      "countryCode": "US",
      "locationType": "city",
      "airportCode": "AUS",
      "timezone": "America/Chicago"
    },
    {
      "locationId": "22863",
      "name": "Austin Bergstrom, Austin, Texas, United States, (AUS)",
      "city": "Austin",
      "country": "United States",
      "countryCode": "US",
      "locationType": "airport",
      "airportCode": "AUS",
      "timezone": "America/Chicago"
    },
    {
      "locationId": "34419",
      "name": "Austin, Minnesota, United States",
      "city": "Austin",
      "country": "United States",
      "countryCode": "US",
      "locationType": "city",
      "airportCode": "AUM",
      "timezone": "America/Chicago"
    }
  ]
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/cars/locations/)._

Docs: https://www.ktemia.com/docs/api/cars/locations/
