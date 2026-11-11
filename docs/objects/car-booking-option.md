# The Car booking option object

> Canonical, always current: [ktemia.com/docs/api/objects/car-booking-option/](https://www.ktemia.com/docs/api/objects/car-booking-option/). This repository is generated from it.


A seller for a car, with terms and a provider URL.

Results include a short form of this object - price, provider, payment type. Details fills in `providerUrl`, cancellation, mileage, fuel, and known fees.

## Attributes

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

## Example

```json
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
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/objects/car-booking-option/)._

Docs: https://www.ktemia.com/docs/api/objects/car-booking-option/
