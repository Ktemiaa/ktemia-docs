# The Hotel object

> Canonical, always current: [ktemia.com/docs/api/objects/hotel/](https://www.ktemia.com/docs/api/objects/hotel/). This repository is generated from it.


One property: the stay, the place, and the cheapest seller.

A hotel is one property you can book for the dates you searched. `bestOption` is the cheapest seller on the before-tax price. `id` is stable for the life of the search token, and it is also the id reviews accept after the token expires.

## Attributes

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

## Example

```json
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
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/objects/hotel/)._

Docs: https://www.ktemia.com/docs/api/objects/hotel/
