# Retrieve flight details

> Canonical, always current: [ktemia.com/docs/api/flights/details/](https://www.ktemia.com/docs/api/flights/details/). This repository is generated from it.


Expand one itinerary into every fare, with a URL that opens the seller’s booking page. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.

Base URL: https://api.ktemia.com
Authentication: send header `X-API-Key` on every request.

`GET /flights/details`

Expand one itinerary into booking options with provider URLs.

Query parameters are `token` and `resultId`. You do not send the route, dates, cabin, or sort again. This call usually answers in 3–4 seconds and includes a booking link for each fare.

## The booking URL

`bookingOptions[].providerUrl` opens the seller’s site with the trip filled in. Open it in a new tab and leave the query string as returned.

## Read more

Why details hands off to the seller instead of booking: [GDS vs booking engine vs a search API](https://www.ktemia.com/blog/search-api-vs-gds-booking-engine/). Connecting search to an agent in Cursor or Claude: [flights MCP](https://www.ktemia.com/blog/flights-mcp/).

## Query parameters

- `token` (string, required): Any token of the search that produced the flight - the original `searchToken` or a later `nextToken`.
- `resultId` (string, required): The `id` of a flight from `/flights/results` for this same token.

## Response fields

- `resultId` (string, required): The `id` you asked about.
- `tripInfo` (object, optional): Classification of the trip.
  - `tripType` (string, optional): `oneWay`, `roundTrip`, or `multiCity`.
  - `isDomestic` (boolean, optional): True when every airport is in the same country.
  - `isMultiAirport` (boolean, optional): True when a city pair uses more than one airport.
- `legs` (array of objects, optional): Same shape as on the flight object.
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
- `bookingOptions` (array of objects, optional): Every fare class on this itinerary, with a provider URL.
  - `providerCode` (string, optional): IATA code of the seller.
  - `providerUrl` (string, optional): Booking link on the seller’s site. Open it as returned.
  - `providerDomain` (string, optional): Host of `providerUrl`.
  - `price` (number, optional): Per-person fare in the country’s native currency.
  - `currency` (string, optional): ISO 4217 code of that country’s native currency.
  - `formattedPrice` (string, optional): Per-person fare, formatted.
  - `totalPrice` (number, optional): Fare for the whole party.
  - `formattedTotalPrice` (string, optional): Whole-party fare, formatted.
  - `bagFees` (object, optional): Carry-on and checked-bag policy for this fare.
    - `carryOn` (object, optional): Carry-on policy for this fare.
      - `status` (string, optional): `included`, `fee`, or `unavailable`.
      - `price` (number, optional): Fee amount when status is `fee`.
      - `label` (string, optional): Short display label.
    - `checked` (object, optional): Checked-bag fees.
      - `firstBag` (object, optional): First checked bag: `status` and `price`.
      - `secondBag` (object, optional): Second checked bag: `status` and `price`.
    - `disclosures` (array of strings, optional): Carrier-written size or weight notes.
    - `policy` (array of objects, optional): Structured bag types with dimension restrictions.
  - `segmentFares` (array of objects, optional): Cabin and onboard amenities per segment.
    - `cabin` (string, optional): Cabin of this segment: `economy`, `premiumEconomy`, `business`, or `first`.
    - `quality` (array of objects, optional): Amenity rows. `type` is one of `aircraft`, `wifi`, `entertainment`, `power`, `seat`, `food`.
  - `badges` (array of strings, optional): Highlights such as `direct` or `freeCancellation`.
- `fareFamilies` (array of objects, optional): Named branded fares with amenity matrices.
  - `id` (string, optional): Carrier fare-family code.
  - `name` (string, optional): Display name, e.g. `Main Base`.
  - `cabin` (string, optional): `economy`, `premiumEconomy`, `business`, or `first`.
  - `price` (number, optional): Starting fare for this family.
  - `formattedPrice` (string, optional): Same fare, formatted.
  - `amenities` (array of objects, optional): `type` is camelCase (`carryOnBag`, `checkedBag`, `seatSelection`, …). `restriction` is `included`, `fee`, or `unavailable`.
- `airlines` (object, optional): Map of airline code to `{ name, feePageUrl }`.
- `airports` (object, optional): Map of airport code to `{ name, city, cityCode, utcOffsetHours }`.
- `providers` (object, optional): Map of provider code to `{ name, type }`.

## Example: One-way itinerary

`GET /flights/details` → 200

Request:

```json
{
  "token": "eyJwIjoxLCJzIjoiNDk1NGMzNmY2ZWY1NDdiYWI4NTI3YzA3ZTBlOWNjZjMiLCJ2IjoxfQ",
  "resultId": "31a71cd28ef337786fe1b368caf96730"
}
```

Response:

```json
{
  "resultId": "31a71cd28ef337786fe1b368caf96730",
  "tripInfo": {
    "tripType": "oneWay",
    "isDomestic": true,
    "isMultiAirport": false
  },
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
      "providerUrl": "https://www.jetblue.com/booking/trip-summary?…",
      "providerDomain": "www.jetblue.com",
      "price": 159,
      "currency": "USD",
      "formattedPrice": "$159",
      "totalPrice": 159,
      "formattedTotalPrice": "$159",
      "bagFees": {
        "carryOn": {
          "status": "included",
          "price": 0,
          "label": "Included"
        },
        "checked": {
          "firstBag": {
            "status": "fee",
            "price": 49
          },
          "secondBag": {
            "status": "fee",
            "price": 69
          }
        },
        "disclosures": [
          "Up to 62in total"
        ],
        "policy": [
          {
            "type": "personalItem",
            "restrictions": {
              "dimensions": "Up to 16 x 12 x 7in"
            }
          },
          {
            "type": "carryOn",
            "restrictions": {
              "dimensions": "Up to 21 x 13 x 8in"
            }
          },
          {
            "type": "checked",
            "restrictions": {
              "dimensions": "Up to 62in total"
            }
          }
        ]
      },
      "segmentFares": [
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Airbus A318/A319/A320/A321 (Narrow-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi"
            },
            {
              "type": "entertainment",
              "label": "Seatback on-demand & live TV"
            }
          ]
        }
      ],
      "badges": [
        "direct",
        "freeCancellation"
      ]
    },
    {
      "providerCode": "B6",
      "providerUrl": "https://www.jetblue.com/booking/trip-summary?…",
      "providerDomain": "www.jetblue.com",
      "price": 214,
      "currency": "USD",
      "formattedPrice": "$214",
      "totalPrice": 214,
      "formattedTotalPrice": "$214",
      "bagFees": {
        "carryOn": {
          "status": "included",
          "price": 0,
          "label": "Included"
        },
        "checked": {
          "firstBag": {
            "status": "fee",
            "price": 49
          },
          "secondBag": {
            "status": "fee",
            "price": 69
          }
        },
        "disclosures": [
          "Up to 62in total"
        ],
        "policy": [
          {
            "type": "personalItem",
            "restrictions": {
              "dimensions": "Up to 16 x 12 x 7in"
            }
          },
          {
            "type": "carryOn",
            "restrictions": {
              "dimensions": "Up to 21 x 13 x 8in"
            }
          },
          {
            "type": "checked",
            "restrictions": {
              "dimensions": "Up to 62in total"
            }
          }
        ]
      },
      "segmentFares": [
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Airbus A318/A319/A320/A321 (Narrow-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi"
            },
            {
              "type": "entertainment",
              "label": "Seatback on-demand & live TV"
            }
          ]
        }
      ],
      "badges": [
        "direct",
        "freeCancellation"
      ]
    },
    {
      "providerCode": "B6",
      "providerUrl": "https://www.jetblue.com/booking/trip-summary?…",
      "providerDomain": "www.jetblue.com",
      "price": 294,
      "currency": "USD",
      "formattedPrice": "$294",
      "totalPrice": 294,
      "formattedTotalPrice": "$294",
      "bagFees": {
        "carryOn": {
          "status": "included",
          "price": 0,
          "label": "Included"
        },
        "checked": {
          "firstBag": {
            "status": "unknown",
            "price": null
          },
          "secondBag": {
            "status": "unknown",
            "price": null
          }
        },
        "disclosures": [
          "Up to 50lbs per bag",
          "Up to 62in total"
        ],
        "policy": [
          {
            "type": "personalItem",
            "restrictions": {
              "dimensions": "Up to 16 x 12 x 7in"
            }
          },
          {
            "type": "carryOn",
            "restrictions": {
              "dimensions": "Up to 21 x 13 x 8in"
            }
          },
          {
            "type": "checked",
            "restrictions": {
              "weight": "Up to 50lbs per bag"
            }
          }
        ]
      },
      "segmentFares": [
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Airbus A318/A319/A320/A321 (Narrow-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi"
            },
            {
              "type": "entertainment",
              "label": "Seatback on-demand & live TV"
            }
          ]
        }
      ],
      "badges": [
        "direct",
        "freeCancellation"
      ]
    }
  ],
  "fareFamilies": [
    {
      "id": "DN",
      "name": "Main Base",
      "cabin": "economy",
      "price": 159,
      "formattedPrice": "$159",
      "amenities": [
        {
          "type": "carryOnBag",
          "restriction": "included",
          "prices": {
            "firstBag": 0
          }
        },
        {
          "type": "checkedBag",
          "restriction": "fee",
          "prices": {
            "firstBag": 49,
            "secondBag": 69
          }
        },
        {
          "type": "seatSelection",
          "restriction": "fee",
          "prices": null
        }
      ]
    },
    {
      "id": "AN",
      "name": "Main",
      "cabin": "economy",
      "price": 214,
      "formattedPrice": "$214",
      "amenities": [
        {
          "type": "carryOnBag",
          "restriction": "included",
          "prices": {
            "firstBag": 0
          }
        },
        {
          "type": "checkedBag",
          "restriction": "fee",
          "prices": {
            "firstBag": 49,
            "secondBag": 69
          }
        },
        {
          "type": "seatSelection",
          "restriction": "included",
          "prices": null
        }
      ]
    },
    {
      "id": "GR",
      "name": "Main Flex",
      "cabin": "economy",
      "price": 294,
      "formattedPrice": "$294",
      "amenities": [
        {
          "type": "carryOnBag",
          "restriction": "included",
          "prices": {
            "firstBag": 0
          }
        },
        {
          "type": "checkedBag",
          "restriction": "fee",
          "prices": null
        },
        {
          "type": "seatSelection",
          "restriction": "included",
          "prices": null
        }
      ]
    }
  ],
  "airports": {
    "LAX": {
      "name": "Los Angeles",
      "city": "Los Angeles",
      "cityCode": "LAX",
      "utcOffsetHours": -8
    },
    "JFK": {
      "name": "John F Kennedy Intl",
      "city": "New York",
      "cityCode": "NYC",
      "utcOffsetHours": -5
    }
  },
  "airlines": {
    "B6": {
      "name": "JetBlue",
      "feePageUrl": "https://www.jetblue.com/at-the-airport/baggage-information"
    }
  },
  "providers": {
    "B6": {
      "name": "JetBlue",
      "type": "Airline"
    }
  }
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/flights/details/)._

## Example: Round-trip itinerary

`GET /flights/details` → 200

Request:

```json
{
  "token": "eyJwIjoxLCJzIjoiODRiZjZlYzU3ZGQyNDJkZDk4NmZhNzAzM2JhY2I3ODkiLCJ2IjoxfQ",
  "resultId": "07804f9e1b83425f0e30951ae0c29a9a"
}
```

Response:

```json
{
  "resultId": "07804f9e1b83425f0e30951ae0c29a9a",
  "tripInfo": {
    "tripType": "roundTrip",
    "isDomestic": false,
    "isMultiAirport": false
  },
  "legs": [
    {
      "departure": "2026-12-03T21:15:00",
      "arrival": "2026-12-04T09:15:00",
      "duration": 420,
      "stops": 0,
      "segments": [
        {
          "airline": "AA",
          "flightNumber": "104",
          "origin": "JFK",
          "destination": "LHR",
          "departure": "2026-12-03T21:15:00",
          "arrival": "2026-12-04T09:15:00",
          "duration": 420,
          "aircraft": "Boeing 787-9 Dreamliner"
        }
      ]
    },
    {
      "departure": "2026-12-10T19:20:00",
      "arrival": "2026-12-10T22:25:00",
      "duration": 485,
      "stops": 0,
      "segments": [
        {
          "airline": "AA",
          "flightNumber": "6942",
          "origin": "LHR",
          "destination": "JFK",
          "departure": "2026-12-10T19:20:00",
          "arrival": "2026-12-10T22:25:00",
          "duration": 485,
          "aircraft": "Boeing 777"
        }
      ]
    }
  ],
  "bookingOptions": [
    {
      "providerCode": "AA",
      "providerUrl": "https://www.aa.com/goto/metasearch?…",
      "providerDomain": "www.aa.com",
      "price": 830,
      "currency": "USD",
      "formattedPrice": "$830",
      "totalPrice": 1659,
      "formattedTotalPrice": "$1,659",
      "bagFees": {
        "carryOn": {
          "status": "included",
          "price": 0,
          "label": "Included"
        },
        "checked": {
          "firstBag": {
            "status": "unknown",
            "price": null
          },
          "secondBag": {
            "status": "unknown",
            "price": null
          }
        },
        "disclosures": [
          "Up to 50lbs per bag",
          "Up to 62in total",
          "Up to 50lbs per bag"
        ],
        "policy": [
          {
            "type": "personalItem",
            "restrictions": {
              "dimensions": "Up to 17 x 13 x 7in"
            }
          },
          {
            "type": "carryOn",
            "restrictions": {
              "dimensions": "Up to 22 x 14 x 9in"
            }
          },
          {
            "type": "checked",
            "restrictions": {
              "weight": "Up to 50lbs per bag"
            }
          }
        ]
      },
      "segmentFares": [
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 787-9 Dreamliner (Wide-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi"
            },
            {
              "type": "entertainment",
              "label": "Seatback on-demand video"
            }
          ]
        },
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 777 (Wide-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi (fee)"
            },
            {
              "type": "entertainment",
              "label": "Seatback on-demand video"
            }
          ]
        }
      ],
      "badges": [
        "direct",
        "freeCancellation"
      ]
    },
    {
      "providerCode": "AA",
      "providerUrl": "https://www.aa.com/goto/metasearch?…",
      "providerDomain": "www.aa.com",
      "price": 1070,
      "currency": "USD",
      "formattedPrice": "$1,070",
      "totalPrice": 2139,
      "formattedTotalPrice": "$2,139",
      "bagFees": {
        "carryOn": {
          "status": "included",
          "price": 0,
          "label": "Included"
        },
        "checked": {
          "firstBag": {
            "status": "unknown",
            "price": null
          },
          "secondBag": {
            "status": "unknown",
            "price": null
          }
        },
        "disclosures": [
          "Up to 50lbs per bag",
          "Up to 62in total",
          "Up to 50lbs per bag"
        ],
        "policy": [
          {
            "type": "personalItem",
            "restrictions": {
              "dimensions": "Up to 17 x 13 x 7in"
            }
          },
          {
            "type": "carryOn",
            "restrictions": {
              "dimensions": "Up to 22 x 14 x 9in"
            }
          },
          {
            "type": "checked",
            "restrictions": {
              "weight": "Up to 50lbs per bag"
            }
          }
        ]
      },
      "segmentFares": [
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 787-9 Dreamliner (Wide-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi"
            },
            {
              "type": "entertainment",
              "label": "Seatback on-demand video"
            }
          ]
        },
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 777 (Wide-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi (fee)"
            },
            {
              "type": "entertainment",
              "label": "Seatback on-demand video"
            }
          ]
        }
      ],
      "badges": [
        "direct",
        "freeCancellation"
      ]
    }
  ],
  "fareFamilies": [
    {
      "id": "BASIC",
      "name": "Basic Economy",
      "cabin": "economy",
      "price": 830,
      "formattedPrice": "$830",
      "amenities": [
        {
          "type": "carryOnBag",
          "restriction": "included",
          "prices": {
            "firstBag": 0
          }
        },
        {
          "type": "checkedBag",
          "restriction": "fee",
          "prices": null
        },
        {
          "type": "seatSelection",
          "restriction": "fee",
          "prices": null
        }
      ]
    },
    {
      "id": "MAIN",
      "name": "Main Cabin",
      "cabin": "economy",
      "price": 1070,
      "formattedPrice": "$1,070",
      "amenities": [
        {
          "type": "carryOnBag",
          "restriction": "included",
          "prices": {
            "firstBag": 0
          }
        },
        {
          "type": "checkedBag",
          "restriction": "unknown",
          "prices": null
        },
        {
          "type": "seatSelection",
          "restriction": "included",
          "prices": null
        }
      ]
    }
  ],
  "airports": {
    "LHR": {
      "name": "Heathrow",
      "city": "London",
      "cityCode": "LON",
      "utcOffsetHours": 0
    },
    "JFK": {
      "name": "John F Kennedy Intl",
      "city": "New York",
      "cityCode": "NYC",
      "utcOffsetHours": -5
    }
  },
  "airlines": {
    "AA": {
      "name": "American Airlines",
      "feePageUrl": "https://www.aa.com/web/i18n/travel-info/baggage/checked-baggage-policy.html"
    }
  },
  "providers": {
    "AA": {
      "name": "American Airlines",
      "type": "Airline"
    },
    "AS": {
      "name": "Alaska Airlines",
      "type": "Airline"
    },
    "AY": {
      "name": "Finnair",
      "type": "Airline"
    },
    "IB": {
      "name": "Iberia",
      "type": "Airline"
    },
    "ASWHISKY": {
      "name": "Alaska Airlines",
      "type": "Airline"
    },
    "BA": {
      "name": "British Airways",
      "type": "Airline"
    }
  }
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/flights/details/)._

## Example: Multi-city itinerary

`GET /flights/details` → 200

Request:

```json
{
  "token": "eyJwIjoxLCJzIjoiZjVmZDc1YzM4NTM5NDhkZGE2ZjAyZjE3MDQ3ZjNmM2EiLCJ2IjoxfQ",
  "resultId": "84604222a90ff5883c97f139be649c27"
}
```

Response:

```json
{
  "resultId": "84604222a90ff5883c97f139be649c27",
  "tripInfo": {
    "tripType": "multiCity",
    "isDomestic": true,
    "isMultiAirport": false
  },
  "legs": [
    {
      "departure": "2026-12-03T17:29:00",
      "arrival": "2026-12-03T23:12:00",
      "duration": 523,
      "stops": 1,
      "segments": [
        {
          "airline": "AS",
          "flightNumber": "41",
          "origin": "JFK",
          "destination": "SFO",
          "departure": "2026-12-03T17:29:00",
          "arrival": "2026-12-03T21:05:00",
          "duration": 396,
          "aircraft": "Boeing 737 MAX 9"
        },
        {
          "airline": "AS",
          "flightNumber": "661",
          "origin": "SFO",
          "destination": "LAX",
          "departure": "2026-12-03T21:45:00",
          "arrival": "2026-12-03T23:12:00",
          "duration": 87,
          "aircraft": "Boeing 737-900 (winglets)"
        }
      ]
    },
    {
      "departure": "2026-12-10T13:50:00",
      "arrival": "2026-12-10T15:16:00",
      "duration": 86,
      "stops": 0,
      "segments": [
        {
          "airline": "AS",
          "flightNumber": "465",
          "origin": "LAX",
          "destination": "SFO",
          "departure": "2026-12-10T13:50:00",
          "arrival": "2026-12-10T15:16:00",
          "duration": 86,
          "aircraft": "Boeing 737 MAX 9"
        }
      ]
    },
    {
      "departure": "2026-12-17T09:10:00",
      "arrival": "2026-12-17T22:29:00",
      "duration": 619,
      "stops": 1,
      "segments": [
        {
          "airline": "AS",
          "flightNumber": "3178",
          "origin": "SFO",
          "destination": "PSP",
          "departure": "2026-12-17T09:10:00",
          "arrival": "2026-12-17T10:51:00",
          "duration": 101,
          "aircraft": "Embraer 175"
        },
        {
          "airline": "AS",
          "flightNumber": "242",
          "origin": "PSP",
          "destination": "JFK",
          "departure": "2026-12-17T14:14:00",
          "arrival": "2026-12-17T22:29:00",
          "duration": 315,
          "aircraft": "Boeing 737-800 (winglets)"
        }
      ]
    }
  ],
  "bookingOptions": [
    {
      "providerCode": "AS",
      "providerUrl": "https://www.alaskaair.com/search/cart?…",
      "providerDomain": "www.alaskaair.com",
      "price": 463,
      "currency": "USD",
      "formattedPrice": "$463",
      "totalPrice": 463,
      "formattedTotalPrice": "$463",
      "bagFees": {
        "policy": [
          {
            "type": "personalItem",
            "restrictions": {}
          },
          {
            "type": "carryOn",
            "restrictions": {
              "dimensions": "Up to 21 x 13 x 8in"
            }
          },
          {
            "type": "checked",
            "restrictions": {
              "dimensions": "Up to 62in total"
            }
          }
        ]
      },
      "segmentFares": [
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 737 MAX 9 (Narrow-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi (fee)"
            },
            {
              "type": "entertainment",
              "label": "Streaming entertainment"
            }
          ]
        },
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 737-900 (winglets) (Narrow-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi (fee)"
            },
            {
              "type": "entertainment",
              "label": "Streaming entertainment"
            }
          ]
        },
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 737 MAX 9 (Narrow-body jet)"
            },
            {
              "type": "wifi",
              "label": "Streaming capable Wi-Fi (fee)"
            },
            {
              "type": "entertainment",
              "label": "Streaming entertainment"
            }
          ]
        }
      ],
      "badges": [
        "direct",
        "freeCancellation"
      ]
    },
    {
      "providerCode": "AS",
      "providerUrl": "https://www.alaskaair.com/search/cart?…",
      "providerDomain": "www.alaskaair.com",
      "price": 628,
      "currency": "USD",
      "formattedPrice": "$628",
      "totalPrice": 628,
      "formattedTotalPrice": "$628",
      "bagFees": {
        "policy": [
          {
            "type": "personalItem",
            "restrictions": {}
          },
          {
            "type": "carryOn",
            "restrictions": {
              "dimensions": "Up to 21 x 13 x 8in"
            }
          },
          {
            "type": "checked",
            "restrictions": {
              "dimensions": "Up to 62in total"
            }
          }
        ]
      },
      "segmentFares": [
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 737 MAX 9 (Narrow-body jet)"
            },
            {
              "type": "wifi",
              "label": "Wi-Fi available"
            }
          ]
        },
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 737-900 (winglets) (Narrow-body jet)"
            },
            {
              "type": "wifi",
              "label": "Wi-Fi available"
            }
          ]
        },
        {
          "cabin": "economy",
          "quality": [
            {
              "type": "aircraft",
              "label": "Boeing 737 MAX 9 (Narrow-body jet)"
            },
            {
              "type": "wifi",
              "label": "Wi-Fi available"
            }
          ]
        }
      ],
      "badges": [
        "direct",
        "freeCancellation"
      ]
    }
  ],
  "fareFamilies": [
    {
      "id": "SV",
      "name": "Saver",
      "cabin": "economy",
      "price": 463,
      "formattedPrice": "$463",
      "amenities": [
        {
          "type": "carryOnBag",
          "restriction": "included",
          "prices": {
            "firstBag": 0
          }
        },
        {
          "type": "checkedBag",
          "restriction": "fee",
          "prices": null
        },
        {
          "type": "seatSelection",
          "restriction": "unavailable",
          "prices": null
        }
      ]
    },
    {
      "id": "MA",
      "name": "Main",
      "cabin": "economy",
      "price": 628,
      "formattedPrice": "$628",
      "amenities": [
        {
          "type": "carryOnBag",
          "restriction": "included",
          "prices": {
            "firstBag": 0
          }
        },
        {
          "type": "checkedBag",
          "restriction": "fee",
          "prices": null
        },
        {
          "type": "seatSelection",
          "restriction": "included",
          "prices": null
        }
      ]
    }
  ],
  "airports": {
    "LAX": {
      "name": "Los Angeles",
      "city": "Los Angeles",
      "cityCode": "LAX",
      "utcOffsetHours": -8
    },
    "PSP": {
      "name": "Palm Springs",
      "city": "Palm Springs",
      "cityCode": "PSP"
    },
    "SFO": {
      "name": "San Francisco",
      "city": "San Francisco",
      "cityCode": "SFO",
      "utcOffsetHours": -8
    },
    "JFK": {
      "name": "John F Kennedy Intl",
      "city": "New York",
      "cityCode": "NYC",
      "utcOffsetHours": -5
    }
  },
  "airlines": {
    "AS": {
      "name": "Alaska Airlines",
      "feePageUrl": "https://www.alaskaair.com/content/travel-info/policies/baggage-checked.aspx?…"
    }
  },
  "providers": {
    "AS": {
      "name": "Alaska Airlines",
      "type": "Airline"
    }
  }
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/flights/details/)._

## Skill

Claude Code, Cursor, and Codex can search with the Ktemia skills: `flight-search`, `car-search`, and `hotel-search`.
https://github.com/Ktemiaa/ktemia-skills

Install in Claude Code:

```
/plugin marketplace add Ktemiaa/ktemia-skills
/plugin install ktemia@ktemia
```

Set `KTEMIA_API_KEY` in the environment. The flight skill looks up airport codes, asks when a name matches several cities, and returns each seller’s booking URL. It does not book tickets. Do not guess origin, destination, or dates.

Docs: https://www.ktemia.com/docs/api/flights/details/
