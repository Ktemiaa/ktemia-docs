# The Flight object

> Canonical, always current: [ktemia.com/docs/api/objects/flight/](https://www.ktemia.com/docs/api/objects/flight/). This repository is generated from it.


One itinerary: legs, segments, and the fares on it.

A flight is one way of making the trip you searched. `legs` follows the trip: one entry outbound, two for a round trip, one per `legs` item for multi-city. `id` is stable for the life of the search token and meaningless after it expires.

## Attributes

- `id` (string, required): Opaque identifier of this itinerary. Pass it as `resultId` to `/flights/details`.
- `legs` (array of objects, optional): One entry per takeoff-to-landing journey. A one-way has one, a round trip two, a multi-city one per `legs` item you sent.
  - `departure` (string, optional): Local departure time of the first segment.
  - `arrival` (string, optional): Local arrival time of the last segment.
  - `duration` (integer, optional): Total elapsed time in minutes, including layovers.
  - `stops` (integer, optional): Number of stops. `0` is nonstop.
  - `segments` (array of objects, optional): The individual flights that make up this leg.
    - `airline` (string, optional): IATA airline code, e.g. `B6`.
    - `flightNumber` (string, optional): Airline flight number without the carrier prefix repeated, e.g. `723`.
    - `origin` (string, optional): Departure airport for this segment.
    - `destination` (string, optional): Arrival airport for this segment.
    - `departure` (string, optional): Local departure time, ISO-8601 without a zone, e.g. `2026-12-03T13:59:00`.
    - `arrival` (string, optional): Local arrival time, same format.
    - `duration` (integer, optional): Block time in minutes.
    - `aircraft` (string, optional): Aircraft name when the carrier publishes one.
- `bookingOptions` (array of objects, optional): Fares on this itinerary. Details expands each option with a booking URL, bags, and cabin amenities.
  - `providerCode` (string, optional): IATA code of the selling airline or agency.
  - `price` (number, optional): Displayed fare in the country’s native currency, per person unless noted.
  - `currency` (string, optional): ISO 4217 code of that country’s native currency.
  - `formattedPrice` (string, optional): Same fare, already formatted for display.
  - `totalPrice` (number, optional): Fare for the whole party.
  - `formattedTotalPrice` (string, optional): Whole-party fare, formatted.
  - `isDirect` (boolean, optional): True when this option is sold by the operating carrier.
  - `isFreeCancellation` (boolean, optional): True when the fare can be cancelled without a fee.
- `totalProviders` (integer, optional): How many sellers offered this itinerary.
- `isBest` (boolean, optional): True when this is the recommended option.
- `isCheapest` (boolean, optional): True when this is the lowest fare on the page.

## Example

```json
{
  "id": "31a71cd28ef337786fe1b368caf96730",
  "legs": [
    {
      "departure": "2026-12-03T13:59:00",
      "arrival": "2026-12-03T17:17:00",
      "duration": 378,
      "stops": 0,
      "segments": [
        {
          "airline": "B6",
          "flightNumber": "723",
          "origin": "JFK",
          "destination": "LAX",
          "departure": "2026-12-03T13:59:00",
          "arrival": "2026-12-03T17:17:00",
          "duration": 378,
          "aircraft": "Airbus A318/A319/A320/A321"
        }
      ]
    }
  ],
  "bookingOptions": [
    {
      "providerCode": "B6",
      "price": 159,
      "currency": "USD",
      "formattedPrice": "$159",
      "totalPrice": 159,
      "formattedTotalPrice": "$159",
      "isDirect": true,
      "isFreeCancellation": true
    },
    {
      "providerCode": "B6",
      "price": 214,
      "currency": "USD",
      "formattedPrice": "$214",
      "totalPrice": 214,
      "formattedTotalPrice": "$214",
      "isDirect": true,
      "isFreeCancellation": true
    },
    {
      "providerCode": "B6",
      "price": 294,
      "currency": "USD",
      "formattedPrice": "$294",
      "totalPrice": 294,
      "formattedTotalPrice": "$294",
      "isDirect": true,
      "isFreeCancellation": true
    }
  ],
  "totalProviders": 1,
  "isBest": true,
  "isCheapest": false
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/objects/flight/)._

Docs: https://www.ktemia.com/docs/api/objects/flight/
