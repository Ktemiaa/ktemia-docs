# List results

> Canonical, always current: [ktemia.com/docs/api/hotels/results/](https://www.ktemia.com/docs/api/hotels/results/). This repository is generated from it.


Hotel API results in Python, JavaScript, Go, Ruby, Java, and PHP. Fetch a page of up to 30 hotels, a nextToken, and an exact total. cURL included.

Base URL: https://api.ktemia.com
Authentication: send header `X-API-Key` on every request.

`GET /hotels/results`

Read a page of a search identified by its token.

Pass the `searchToken` from `/hotels/search` as the `token` query parameter to get page 1. Each response that has another page includes `nextToken`. This call usually answers in 2–5 seconds.

## What is in a page

`hotels` holds up to 30 properties. Page 1 is often a few short of 30. `bestOption` is the cheapest seller on the before-tax stay price, which is also what `sortBy=price` orders by. `totalPrice` on that option includes taxes.

`availableFilters` describes this search. `minStars`, `minRating`, `maxPrice`, `freeCancellation`, amenity ids, and booking-site ids (as `providers`) can be sent on a new `/hotels/search`. The `id` on a hotel is what `/hotels/details` wants as `resultId`, and what `/hotels/reviews` wants as `hotelId`. Keep the token - details needs it too. Reviews do not.

## Query parameters

- `token` (string, required): A `searchToken` from `/hotels/search` for page 1, or a `nextToken` from the previous page. There is no page number to set.

## Response fields

- `hotels` (array of objects, required): Up to 30 hotels. The first page is often a few short of 30.
  - `id` (string, required): Hotel id. Pass it as `resultId` to `/hotels/details`, and as `hotelId` to `/hotels/reviews`.
  - `name` (string, optional): Property name.
  - `description` (string, optional): Short description when the property publishes one.
  - `propertyType` (object, optional): What kind of stay this is.
    - `code` (string, optional): Type code, for example `hotel`.
    - `name` (string, optional): Display name, for example `Hotel`.
  - `stars` (number, optional): Star rating. `0` means the property is unrated, not zero stars.
  - `usesStarRating` (boolean, optional): True when `stars` is a star class rather than an unrated property.
  - `rating` (object, optional): Guest score.
    - `score` (number, optional): Guest score on a 0–10 scale.
    - `label` (string, optional): Short label for the score, for example `Very good`.
    - `reviewCount` (integer, optional): How many reviews the score is based on.
  - `location` (object, optional): Where the property is.
    - `city` (string, optional): City.
    - `neighborhood` (string, optional): Neighbourhood when the property publishes one.
    - `distance` (string, optional): Distance from the reference point, already formatted.
    - `distanceFrom` (string, optional): What the distance is measured from, for example the city centre.
    - `lat` (number, optional): Latitude.
    - `lng` (number, optional): Longitude.
  - `phone` (string, optional): Phone number when the property publishes one.
  - `image` (string, optional): Representative image URL.
  - `imageCount` (integer, optional): How many images details can return.
  - `amenities` (array of strings, optional): Amenity names. The ids you can filter on are in `availableFilters.amenities`.
  - `badges` (array of objects, optional): Highlights on the property. Each has `type` and `label`.
  - `highlight` (string, optional): A short callout when the property has one.
  - `bestOption` (object, optional): The cheapest seller on the before-tax stay price. Details lists every seller.
    - `provider` (string, optional): Seller with the lowest before-tax stay price.
    - `price` (object, optional): Stay price before taxes. This is the price a `price` sort uses.
      - `amount` (number, optional): Numeric amount in the country’s native currency.
      - `currency` (string, optional): ISO 4217 code of that country’s native currency.
      - `formatted` (string, optional): Same amount, already formatted for display.
    - `totalPrice` (object, optional): Stay price with taxes included.
      - `amount` (number, optional): Numeric amount in the country’s native currency.
      - `currency` (string, optional): ISO 4217 code of that country’s native currency.
      - `formatted` (string, optional): Same amount, already formatted for display.
    - `rateType` (string, optional): Rate label from the seller, for example `memberOnly`.
    - `freebies` (array of strings, optional): Included extras, such as free cancellation, when the seller lists them.
    - `taxEstimated` (boolean, optional): True when the tax portion is an estimate.
    - `instantBooking` (boolean, optional): True when the seller can confirm the stay immediately.
    - `privateDeal` (boolean, optional): True when the rate is a private or member deal.
  - `optionCount` (integer, optional): How many sellers offered this property.
  - `usualPrice` (object, optional): A recent higher price for the same stay, when one is published.
    - `amount` (number, optional): Numeric amount in the country’s native currency.
    - `currency` (string, optional): ISO 4217 code of that country’s native currency.
    - `formatted` (string, optional): Same amount, already formatted for display.
  - `viewRank` (integer, optional): Position of this hotel in the current sort, starting at 0.
- `page` (integer, required): 1-based page number for the token you sent.
- `hasMore` (boolean, required): True when another page exists.
- `expiresIn` (integer, required): Seconds remaining on this search.
- `totalResults` (integer, optional): How many hotels this search contains.
- `nextToken` (string, optional): Present when `hasMore` is true. Send it as `token` on the next `/hotels/results` call.
- `destination` (object, optional): The place this search resolved to. For display. `cityId` here is not the `locationId` you send on a search.
  - `name` (string, optional): Full place name.
  - `shortName` (string, optional): Short place name.
  - `cityId` (string, optional): Display id of the city. Do not send this as `location`.
  - `country` (string, optional): Country name.
  - `countryCode` (string, optional): ISO 3166-1 alpha-2 country code.
- `availableFilters` (object, optional): Facets of this result set. `minStars`, `minRating`, `maxPrice`, `freeCancellation`, `amenities`, and `bookingSites` (as `providers`) can be sent on a new `/hotels/search`. The rest is for display.
  - `price` (object, optional): Price buckets for the before-tax stay price, in the country’s native currency.
  - `stars` (object, optional): Star counts. `minStars` on a new search keeps that many stars and above.
    - `options` (array of objects, optional): One entry per star value.
      - `id` (string, optional): Filter id.
      - `label` (string, optional): Display label.
      - `count` (integer, optional): How many hotels match this option.
  - `rating` (object, optional): Guest-score buckets. `minRating` takes `6`, `7`, `8`, or `9`.
    - `options` (array of objects, optional): One entry per score bucket.
      - `id` (string, optional): Filter id.
      - `label` (string, optional): Display label.
      - `count` (integer, optional): How many hotels match this option.
  - `amenities` (object, optional): Amenity ids. Send them as `amenities` on a new search.
    - `options` (array of objects, optional): One entry per amenity.
      - `id` (string, optional): Filter id.
      - `label` (string, optional): Display label.
      - `count` (integer, optional): How many hotels match this option.
  - `freebies` (object, optional): Included extras such as free cancellation.
  - `propertyType` (object, optional): Property types in this result set. For display.
  - `bookingSites` (object, optional): Booking sites selling stays in this result set. Send their ids as `providers` on a new search.
    - `options` (array of objects, optional): One entry per booking site.
      - `id` (string, optional): Filter id.
      - `label` (string, optional): Display label.
      - `count` (integer, optional): How many hotels match this option.

## Example: Page 1

`GET /hotels/results` → 200

Request:

```json
{
  "token": "eyJwIjoxLCJzIjoiNjgyMmZiMzMyMzA4NDZjNGFiZWRiM2Q2OTRiM2YyNjgiLCJ2IjoxfQ"
}
```

Response:

```json
{
  "hotels": [
    {
      "id": "5782",
      "name": "Threadneedles Autograph Collection",
      "description": "Experience refined luxury combined with incredible convenience at our boutique hotel in London. Perfectly situated within the former Victorian City Bank, it features 5-star guest rooms and suites with distinctive, tim...",
      "propertyType": {
        "code": "hotel",
        "name": "Hotel"
      },
      "stars": 5,
      "usesStarRating": true,
      "rating": {
        "score": 8.9,
        "label": "Very good",
        "reviewCount": 504
      },
      "location": {
        "city": "London",
        "neighborhood": "City of London",
        "distance": "2.0 mi",
        "distanceFrom": "from city center",
        "lat": 51.51415,
        "lng": -0.085678
      },
      "phone": "+44 207 657 8080",
      "image": "https://content.r9cdn.net/rimg/himg/1b/39/42/leonardo-5782-3599011-366479.jpg?…",
      "imageCount": 15,
      "amenities": [
        "24hr front desk",
        "Air-conditioned",
        "Airport shuttle"
      ],
      "badges": [
        {
          "type": "freeWifi",
          "label": "Free WiFi"
        }
      ],
      "highlight": "Near observatory, near station, complimentary mini-bar",
      "bestOption": {
        "provider": "Marriott Bonvoy",
        "price": {
          "amount": 753,
          "currency": "USD",
          "formatted": "$753"
        },
        "totalPrice": {
          "amount": 753,
          "currency": "USD",
          "formatted": "$753"
        },
        "rateType": "memberOnly",
        "freebies": null,
        "taxEstimated": false,
        "instantBooking": true,
        "privateDeal": false
      },
      "optionCount": 8,
      "usualPrice": {
        "amount": 899.15,
        "currency": "USD",
        "formatted": "$899"
      },
      "viewRank": 0
    },
    {
      "id": "2222365",
      "name": "Montcalm East, Autograph Collection",
      "description": "See life in a whole new light at Montcalm East, a standout luxury hotel in Shoreditch, central London. Just a short stroll from Old Street station and close to Liverpool Street, this innovative hotel brings East Londo...",
      "propertyType": {
        "code": "hotel",
        "name": "Hotel"
      },
      "stars": 5,
      "usesStarRating": true,
      "rating": {
        "score": 8.8,
        "label": "Very good",
        "reviewCount": 4264
      },
      "location": {
        "city": "London",
        "neighborhood": "Hackney",
        "distance": "2.5 mi",
        "distanceFrom": "from city center",
        "lat": 51.527763,
        "lng": -0.088972
      },
      "phone": "+44 203 837 3000",
      "image": "https://content.r9cdn.net/rimg/himg/bb/01/77/leonardo-2222365-1447407-933236.jpg?…",
      "imageCount": 15,
      "amenities": [
        "24hr front desk",
        "Air-conditioned",
        "Airport shuttle"
      ],
      "badges": [
        {
          "type": "freeWifi",
          "label": "Free WiFi"
        }
      ],
      "highlight": "Near park, near station, great stay",
      "bestOption": {
        "provider": "Booking.com",
        "price": {
          "amount": 600,
          "currency": "USD",
          "formatted": "$600"
        },
        "totalPrice": {
          "amount": 720,
          "currency": "USD",
          "formatted": "$720"
        },
        "rateType": "bestAvailable",
        "freebies": [
          "Free cancellation"
        ],
        "taxEstimated": false,
        "instantBooking": true,
        "privateDeal": false
      },
      "optionCount": 7,
      "usualPrice": {
        "amount": 622.82,
        "currency": "USD",
        "formatted": "$623"
      },
      "viewRank": 1
    }
  ],
  "page": 1,
  "hasMore": true,
  "expiresIn": 3596,
  "totalResults": 4687,
  "nextToken": "eyJwIjoyLCJzIjoiNjgyMmZiMzMyMzA4NDZjNGFiZWRiM2Q2OTRiM2YyNjgiLCJ2IjoxfQ",
  "destination": {
    "name": "London, England, United Kingdom",
    "shortName": "London",
    "cityId": "28501",
    "country": "United Kingdom",
    "countryCode": "GB"
  },
  "availableFilters": {
    "stars": {
      "options": [
        {
          "id": "0",
          "label": "0+",
          "count": 4687
        },
        {
          "id": "2",
          "label": "2",
          "count": 125
        },
        {
          "id": "3",
          "label": "3",
          "count": 481
        }
      ],
      "usesStarRatings": true
    },
    "rating": {
      "options": [
        {
          "id": "awful",
          "label": "0+",
          "count": 4687
        },
        {
          "id": "okay",
          "label": "6+",
          "count": 2783
        },
        {
          "id": "good",
          "label": "7+",
          "count": 2390
        }
      ]
    },
    "freebies": {
      "options": [
        {
          "id": "freeinternet",
          "label": "Free internet",
          "count": 3464,
          "icon": "freeinternet"
        },
        {
          "id": "freecancellation",
          "label": "Free cancellation",
          "count": 2239,
          "icon": "freecancellation"
        },
        {
          "id": "freeparking",
          "label": "Free parking",
          "count": 1027,
          "icon": "freeparking"
        }
      ]
    },
    "propertyType": {
      "options": [
        {
          "id": "apthotel",
          "label": "Aparthotel",
          "count": 76,
          "parent": "hotels"
        },
        {
          "id": "bb",
          "label": "Bed & Breakfast",
          "count": 35,
          "parent": "hotels"
        },
        {
          "id": "guesthouse",
          "label": "Guest house",
          "count": 176,
          "parent": "hotels"
        }
      ]
    },
    "amenities": {
      "options": [
        {
          "id": "nosmokerooms",
          "label": "Non-smoking rooms",
          "count": 4345,
          "icon": "smoking-na",
          "category": "general"
        },
        {
          "id": "wifi",
          "label": "Wi-Fi",
          "count": 4116,
          "icon": "wifi",
          "category": "internet"
        },
        {
          "id": "hairdryer",
          "label": "Hairdryer",
          "count": 3217,
          "category": "general"
        }
      ]
    },
    "price": {
      "values": [
        30,
        38,
        49
      ],
      "formattedValues": [
        "$30",
        "$38",
        "$49"
      ]
    }
  }
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/hotels/results/)._

## Example: Page 2

`GET /hotels/results` → 200

Request:

```json
{
  "token": "eyJwIjoyLCJzIjoiNjgyMmZiMzMyMzA4NDZjNGFiZWRiM2Q2OTRiM2YyNjgiLCJ2IjoxfQ"
}
```

Response:

```json
{
  "hotels": [
    {
      "id": "54877",
      "name": "Holiday Inn Express London - Stratford By IHG",
      "description": "Welcome to Holiday Inn Express London - Stratford, where smart value meets East London energy. We're a 6-minute walk from Stratford Station, with the Elizabeth Line, DLR, and Central and Jubilee lines putting all of L...",
      "propertyType": {
        "code": "hotel",
        "name": "Hotel"
      },
      "stars": 3,
      "usesStarRating": true,
      "rating": {
        "score": 8.8,
        "label": "Very good",
        "reviewCount": 7872
      },
      "location": {
        "city": "London",
        "neighborhood": "Newham",
        "distance": "5.8 mi",
        "distanceFrom": "from city center",
        "lat": 51.53633,
        "lng": -0.004469
      },
      "phone": "+44 20 8536 8000",
      "image": "https://content.r9cdn.net/rimg/himg/05/19/01/leonardo-54877-202966946-029789.jpg?…",
      "imageCount": 15,
      "amenities": [
        "24hr front desk",
        "Air-conditioned",
        "Business center"
      ],
      "badges": [
        {
          "type": "freeWifi",
          "label": "Free WiFi"
        }
      ],
      "highlight": "Near theater, good breakfast, good value",
      "bestOption": {
        "provider": "Super.com",
        "price": {
          "amount": 359,
          "currency": "USD",
          "formatted": "$359"
        },
        "totalPrice": {
          "amount": 431,
          "currency": "USD",
          "formatted": "$431"
        },
        "rateType": "bestAvailable",
        "freebies": [
          "Free breakfast"
        ],
        "taxEstimated": false,
        "instantBooking": true,
        "privateDeal": false
      },
      "optionCount": 7,
      "usualPrice": {
        "amount": 252.54,
        "currency": "USD",
        "formatted": "$253"
      },
      "viewRank": 0
    }
  ],
  "page": 2,
  "hasMore": true,
  "expiresIn": 3591,
  "totalResults": 4687,
  "nextToken": "eyJwIjozLCJzIjoiNjgyMmZiMzMyMzA4NDZjNGFiZWRiM2Q2OTRiM2YyNjgiLCJ2IjoxfQ"
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/hotels/results/)._

Docs: https://www.ktemia.com/docs/api/hotels/results/
