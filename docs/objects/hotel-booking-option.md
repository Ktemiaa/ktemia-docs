# The Hotel booking option object

> Canonical, always current: [ktemia.com/docs/api/objects/hotel-booking-option/](https://www.ktemia.com/docs/api/objects/hotel-booking-option/). This repository is generated from it.


A seller for a stay, with a provider URL.

Results include a short form of this object on `bestOption` - price, provider, and a few flags. Details lists every seller and fills in `providerUrl`.

## Attributes

- `provider` (string, optional): Seller name.
- `price` (object, optional): Stay price before taxes.
  - `amount` (number, optional): Numeric amount in the country’s native currency.
  - `currency` (string, optional): ISO 4217 code of that country’s native currency.
  - `formatted` (string, optional): Same amount, already formatted for display.
- `totalPrice` (object, optional): Stay price with taxes included.
  - `amount` (number, optional): Numeric amount in the country’s native currency.
  - `currency` (string, optional): ISO 4217 code of that country’s native currency.
  - `formatted` (string, optional): Same amount, already formatted for display.
- `rateType` (string, optional): Rate label from the seller.
- `roomCode` (string, optional): Room code at the seller, when one is published.
- `freebies` (array of strings, optional): Included extras.
- `taxEstimated` (boolean, optional): True when the tax portion is an estimate.
- `instantBooking` (boolean, optional): True when the seller can confirm immediately.
- `directWithProperty` (boolean, optional): True when this option is booked with the property itself.
- `privateDeal` (boolean, optional): True when the rate is a private or member deal.
- `providerUrl` (string, optional): URL that opens this seller’s site with the stay filled in. `null` when it did not resolve.
- `providerDomain` (string, optional): Host of `providerUrl`.

## Example

```json
{
  "provider": "Booking.com",
  "price": {
    "amount": 760,
    "currency": "USD",
    "formatted": "$760"
  },
  "totalPrice": {
    "amount": 904,
    "currency": "USD",
    "formatted": "$904"
  },
  "rateType": "bestAvailable",
  "roomCode": "36278308",
  "freebies": null,
  "taxEstimated": false,
  "instantBooking": true,
  "directWithProperty": false,
  "privateDeal": false,
  "providerUrl": "https://www.booking.com/hotel/gb/threadneedles-london.html?…",
  "providerDomain": "www.booking.com"
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/objects/hotel-booking-option/)._

Docs: https://www.ktemia.com/docs/api/objects/hotel-booking-option/
