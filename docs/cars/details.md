# Retrieve car details

> Canonical, always current: [ktemia.com/docs/api/cars/details/](https://www.ktemia.com/docs/api/cars/details/). This repository is generated from it.


Car hire API details in Python, JavaScript, Go, Ruby, Java, and PHP. Expand one car into every seller, with a URL that opens that booking site. cURL included.

Base URL: https://api.ktemia.com
Authentication: send header `X-API-Key` on every request.

`GET /cars/details`

Expand one car into booking options with provider URLs.

Query parameters are `token` and `resultId`. You do not send the location, dates, or sort again. This call usually answers in 2–5 seconds and includes a booking link for each seller that resolved.

## The booking URL

`bookingOptions[].providerUrl` opens the seller’s site with the hire filled in. Open it in a new tab and leave the query string as returned. A `null` URL means that seller did not resolve; the others on the same car are still usable.

## Read more

Why details hands off to the seller instead of booking: [GDS vs booking engine vs a search API](https://www.ktemia.com/blog/search-api-vs-gds-booking-engine/). The compare job: [car rental API](https://www.ktemia.com/blog/car-rental-api/).

## Query parameters

- `token` (string, required): Any token of the search that produced the car - the original `searchToken` or a later `nextToken`.
- `resultId` (string, required): The `id` of a car from `/cars/results` for this same token.

## Response fields

- `resultId` (string, required): The `id` you asked about.
- `car` (object, optional): The vehicle.
  - `name` (string, optional): Vehicle name as listed, for example `Nissan Versa`.
  - `class` (string, optional): Display class, for example `Compact` or `Intermediate SUV`.
  - `classGroups` (array of strings, optional): Groups this car belongs to, such as `small` or `suv`. Matches `carClass` on a new search.
  - `image` (string, optional): Image URL.
  - `passengers` (integer, optional): Seat count.
  - `bags` (integer, optional): Bag count.
  - `doors` (integer, optional): Door count.
  - `transmission` (string, optional): `automatic` or `manual`.
  - `airConditioning` (boolean, optional): True when the car has air conditioning.
  - `fuelType` (string, optional): Fuel label, for example `Gas` or `Fully electric`.
  - `sipCode` (string, optional): ACRISS / SIP code when the supplier publishes one.
- `agency` (object, optional): The rental company.
- `pickup` (object, optional): The pickup desk.
  - `locationId` (string, optional): Desk id. Different from the city id you sent as `pickupLocation`.
  - `type` (string, optional): Desk type, for example `IN_TERMINAL` or `NON_AIRPORT`.
  - `isAirport` (boolean, optional): True when the desk is at an airport.
  - `airportCode` (string, optional): IATA airport code when `isAirport` is true.
  - `address` (string, optional): Street address when the supplier publishes one.
  - `city` (string, optional): City of the desk.
  - `country` (string, optional): ISO 3166-1 alpha-2 country code.
  - `distance` (string, optional): Distance from the city centre, already formatted.
  - `lat` (number, optional): Latitude.
  - `lng` (number, optional): Longitude.
  - `rating` (object, optional): Desk reviews.
    - `overall` (number, optional): Desk score on a 0–10 scale.
    - `label` (string, optional): Short label for the score, for example `good`.
    - `count` (integer, optional): How many reviews the score is based on.
    - `breakdowns` (array of objects, optional): Per-category scores when the supplier publishes them.
  - `operatingHours` (array of objects, optional): Opening hours. `open` and `close` are `HHMM` integers, for example `730` is 07:30.
- `bookingOptions` (array of objects, optional): Every seller for this car, with a provider URL when it resolved.
  - `provider` (object, optional): The seller.
    - `code` (string, optional): Seller code.
    - `name` (string, optional): Display name.
    - `site` (string, optional): Seller hostname, without a scheme.
  - `providerUrl` (string, optional): Booking link on the seller’s site. Open it as returned. Null when the seller did not resolve.
  - `providerDomain` (string, optional): Host of `providerUrl`.
  - `price` (object, optional): Displayed price.
    - `amount` (number, optional): Numeric amount in the country’s native currency.
    - `currency` (string, optional): ISO 4217 code of that country’s native currency.
    - `formatted` (string, optional): Same amount, already formatted for display.
  - `perDay` (object, optional): Average daily price.
    - `amount` (number, optional): Numeric amount in the country’s native currency.
    - `currency` (string, optional): ISO 4217 code of that country’s native currency.
    - `formatted` (string, optional): Same amount, already formatted for display.
  - `totalPrice` (object, optional): Total for the hire.
    - `amount` (number, optional): Numeric amount in the country’s native currency.
    - `currency` (string, optional): ISO 4217 code of that country’s native currency.
    - `formatted` (string, optional): Same amount, already formatted for display.
  - `paymentType` (string, optional): `PREPAY` or `PAY_AT_PICKUP`.
  - `requiresCreditCard` (boolean, optional): True when the seller asks for a card at booking.
  - `cancellation` (object, optional): Cancellation terms.
    - `policyType` (string, optional): Policy id from the seller.
    - `free` (boolean, optional): True when a free cancellation window exists.
    - `limitHours` (integer, optional): Hours before pickup after which a fee applies.
    - `fee` (object, optional): Fee when cancellation is not free.
      - `amount` (number, optional): Numeric amount in the country’s native currency.
      - `currency` (string, optional): ISO 4217 code of that country’s native currency.
      - `formatted` (string, optional): Same amount, already formatted for display.
    - `summary` (array of strings, optional): Seller-written terms.
  - `mileage` (object, optional): Mileage allowance.
  - `fuel` (object, optional): Fuel policy.
  - `insurance` (array of objects, optional): Insurance extras when the seller lists them.
  - `extras` (object, optional): Flags such as contactless pickup or a free additional driver.
  - `knownFees` (array of objects, optional): Fees that are not in the total, such as a security deposit.
  - `vehicle` (object, optional): The vehicle this seller is quoting.
    - `name` (string, optional): Vehicle name as listed, for example `Nissan Versa`.
    - `class` (string, optional): Display class, for example `Compact` or `Intermediate SUV`.
    - `classGroups` (array of strings, optional): Groups this car belongs to, such as `small` or `suv`. Matches `carClass` on a new search.
    - `image` (string, optional): Image URL.
    - `passengers` (integer, optional): Seat count.
    - `bags` (integer, optional): Bag count.
    - `doors` (integer, optional): Door count.
    - `transmission` (string, optional): `automatic` or `manual`.
    - `airConditioning` (boolean, optional): True when the car has air conditioning.
    - `fuelType` (string, optional): Fuel label, for example `Gas` or `Fully electric`.
    - `sipCode` (string, optional): ACRISS / SIP code when the supplier publishes one.

## Example: Austin hire

`GET /cars/details` → 200

Request:

```json
{
  "token": "eyJwIjoxLCJzIjoiMzY5Yjc0Yzc0NDI1NGYxYThjMWIyNGQ3NjgxMmZjMWUiLCJ2IjoxfQ",
  "resultId": "cd9d6ba5326148f167cee70439f61ea9"
}
```

Response:

```json
{
  "resultId": "cd9d6ba5326148f167cee70439f61ea9",
  "car": {
    "name": "Ford EcoSport",
    "class": "Intermediate SUV",
    "classGroups": [
      "suv"
    ],
    "image": "https://content.r9cdn.net/rimg/car-images/generic/05_suv-small_black.png?…"
  },
  "agency": {
    "code": "fox",
    "name": "Fox"
  },
  "pickup": {
    "locationId": "56753",
    "type": "IN_TERMINAL",
    "isAirport": true,
    "airportCode": "AUS",
    "address": "3819 Presidential Boulevard",
    "city": "Austin",
    "country": "US",
    "distance": "7.1 mi from city center",
    "lat": 30.19453,
    "lng": -97.66987,
    "rating": {
      "overall": 6.4,
      "label": "good",
      "count": 96,
      "breakdowns": null
    },
    "operatingHours": [
      {
        "days": "Monday - Sunday",
        "open": 700,
        "close": 2359
      }
    ]
  },
  "bookingOptions": [
    {
      "provider": {
        "code": "IWISECARS",
        "name": "Wisecars",
        "site": "wisecars.com"
      },
      "price": {
        "amount": 253,
        "currency": "USD",
        "formatted": "$253"
      },
      "perDay": {
        "amount": 37,
        "currency": "USD",
        "formatted": "$37"
      },
      "totalPrice": {
        "amount": 253,
        "currency": "USD",
        "formatted": "$253"
      },
      "paymentType": "PREPAY",
      "requiresCreditCard": false,
      "cancellation": {
        "policyType": "FREE_POSSIBLE",
        "free": true,
        "limitHours": null,
        "fee": null,
        "summary": [
          "Cancel for free up to 48 hours before pick-up.",
          "If you cancel within 48 hours of pick-up, a fee applies."
        ]
      },
      "mileage": {
        "type": "unlimited",
        "limit": "Unlimited miles",
        "detail": "Your rental includes unlimited free miles"
      },
      "fuel": {
        "code": "FULL_TO_FULL",
        "name": "full-to-full",
        "description": "Pick up and drop off the car with a full tank"
      },
      "insurance": null,
      "extras": {
        "contactless": false,
        "enhancedCleaning": false,
        "freeAdditionalDriver": false,
        "hiddenCharges": false
      },
      "knownFees": [
        {
          "type": "securityDeposit",
          "status": "amountKnown",
          "amount": {
            "amount": 150,
            "currency": "USD",
            "formatted": "$150"
          },
          "included": false
        }
      ],
      "badges": [
        {
          "type": "freeCancellation",
          "label": "Free Cancellation"
        }
      ],
      "displayBadges": null,
      "vehicle": {
        "name": "Ford EcoSport",
        "class": "Intermediate SUV",
        "doors": 5,
        "bags": 3,
        "passengers": 5,
        "transmission": "automatic",
        "airConditioning": true,
        "fuelType": "Gas",
        "sipCode": "IFAR"
      },
      "providerUrl": "https://www.wisecars.com/en-us/results/?…",
      "providerDomain": "www.wisecars.com"
    },
    {
      "provider": {
        "code": "IAUTOEUROPE",
        "name": "Auto Europe",
        "site": "autoeurope.com"
      },
      "price": {
        "amount": 274,
        "currency": "USD",
        "formatted": "$274"
      },
      "perDay": {
        "amount": 40,
        "currency": "USD",
        "formatted": "$40"
      },
      "totalPrice": {
        "amount": 274,
        "currency": "USD",
        "formatted": "$274"
      },
      "paymentType": "PREPAY",
      "requiresCreditCard": false,
      "cancellation": {
        "policyType": "FREE_POSSIBLE",
        "free": true,
        "limitHours": null,
        "fee": null,
        "summary": [
          "Cancel for free up to 48 hours before pick-up.",
          "If you cancel within 48 hours of pick-up, a fee applies."
        ]
      },
      "mileage": {
        "type": "unlimited",
        "limit": "Unlimited miles",
        "detail": "Your rental includes unlimited free miles"
      },
      "fuel": {
        "code": "FULL_TO_FULL",
        "name": "full-to-full",
        "description": "Pick up and drop off the car with a full tank"
      },
      "insurance": null,
      "extras": {
        "contactless": false,
        "enhancedCleaning": false,
        "freeAdditionalDriver": false,
        "hiddenCharges": false
      },
      "knownFees": [
        {
          "type": "securityDeposit",
          "status": "amountKnown",
          "amount": {
            "amount": 150,
            "currency": "USD",
            "formatted": "$150"
          },
          "included": false
        }
      ],
      "badges": [
        {
          "type": "freeCancellation",
          "label": "Free Cancellation"
        }
      ],
      "displayBadges": null,
      "vehicle": {
        "name": "Ford EcoSport",
        "class": "Intermediate SUV",
        "doors": 5,
        "bags": 3,
        "passengers": 5,
        "transmission": "automatic",
        "airConditioning": true,
        "fuelType": "Gas",
        "sipCode": "IFAR"
      },
      "providerUrl": "https://book.autoeurope.com/en-us/options?…",
      "providerDomain": "book.autoeurope.com"
    },
    {
      "provider": {
        "code": "ICARRENTAL8",
        "name": "Car Rental 8",
        "site": "carrental8.com"
      },
      "price": {
        "amount": 274,
        "currency": "USD",
        "formatted": "$274"
      },
      "perDay": {
        "amount": 40,
        "currency": "USD",
        "formatted": "$40"
      },
      "totalPrice": {
        "amount": 274,
        "currency": "USD",
        "formatted": "$274"
      },
      "paymentType": "PREPAY",
      "requiresCreditCard": false,
      "cancellation": {
        "policyType": "FREE_POSSIBLE",
        "free": true,
        "limitHours": null,
        "fee": null,
        "summary": [
          "Cancel for free up to 48 hours before pick-up.",
          "If you cancel within 48 hours of pick-up, a fee applies."
        ]
      },
      "mileage": {
        "type": "unlimited",
        "limit": "Unlimited miles",
        "detail": "Your rental includes unlimited free miles"
      },
      "fuel": {
        "code": "FULL_TO_FULL",
        "name": "full-to-full",
        "description": "Pick up and drop off the car with a full tank"
      },
      "insurance": null,
      "extras": {
        "contactless": false,
        "enhancedCleaning": false,
        "freeAdditionalDriver": false,
        "hiddenCharges": false
      },
      "knownFees": [
        {
          "type": "securityDeposit",
          "status": "amountKnown",
          "amount": {
            "amount": 150,
            "currency": "USD",
            "formatted": "$150"
          },
          "included": false
        }
      ],
      "badges": [
        {
          "type": "freeCancellation",
          "label": "Free Cancellation"
        }
      ],
      "displayBadges": null,
      "vehicle": {
        "name": "Ford EcoSport",
        "class": "Intermediate SUV",
        "doors": 5,
        "bags": 3,
        "passengers": 5,
        "transmission": "automatic",
        "airConditioning": true,
        "fuelType": "Gas",
        "sipCode": "IFAR"
      },
      "providerUrl": "https://www.carrental8.com/en-us/bookings/create?…",
      "providerDomain": "www.carrental8.com"
    }
  ]
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/cars/details/)._

Docs: https://www.ktemia.com/docs/api/cars/details/
