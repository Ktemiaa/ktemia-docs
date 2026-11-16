# Check key status

> Canonical, always current: [ktemia.com/docs/api/key/](https://www.ktemia.com/docs/api/key/). This repository is generated from it.


Read the plan, rate limits, and remaining monthly quota for an API key. Not metered, so checking costs nothing. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.

Base URL: https://api.ktemia.com
Authentication: send header `X-API-Key` on every request.

`GET /key`

Read the plan, limits, and remaining monthly allowance for your key.

Send `X-API-Key` and nothing else. The response describes that key: its plan, its rate limits, and how much of this month’s allowance is left.

This is the one endpoint that is **not metered**. Asking what is left does not spend it, and the call keeps working after the quota is gone.

## Why it is free

Two reasons, both practical. A client that checks its budget before every search would otherwise double what it spends. And a key refused with `429 QUOTA_EXCEEDED` has to stay able to find out why - metering the diagnostic would make it unanswerable at exactly the moment it is needed.

Unmetered is not unlimited. The call still takes a token from the same rate-limit bucket as any other, so polling it in a loop answers `429 RATE_LIMIT_EXCEEDED`. The two 429s mean opposite things: a rate limit is worth retrying after `Retry-After`, a spent quota is not worth retrying at all this month.

## A shared allowance

When `usage.scope` is `account`, the number is the whole account’s. Every key you hold spends the same allowance, so minting another key does not buy more requests, and `remaining` is not this key’s alone to spend.

`key` means this key has its own counter, which applies to keys issued outside the dashboard.

Nothing is ever reset. The month is part of the record, so `usage.resetsAt` is when a new month starts counting rather than when a counter is cleared.

## What it does not tell you

A key describes itself, not its owner. Whoever holds a key is not necessarily the account holder, because keys get pasted into shared agent configs and CI, so the response carries no email address, no account id, and no list of your other keys.

`key.fingerprint` is a short prefix for telling several keys apart in a log. The key cannot be reconstructed from it.

## Every response carries the same numbers

You do not need this call to track usage. Every metered response already includes `X-Quota-Limit`, `X-Quota-Used`, `X-RateLimit-Limit`, and `X-RateLimit-Remaining`, so a client can read its budget from work it was doing anyway.

This endpoint covers the two cases headers cannot: before you have made any call, and after one was refused. Being unmetered, it sets `X-Quota-Limit` but no `X-Quota-Used` - the body carries the authoritative figure.

## Read more

What each plan includes: [pricing](https://www.ktemia.com/pricing/). What the error codes mean and which are worth retrying: [Errors](https://www.ktemia.com/docs/api/#errors). How to send the key in the first place: [Authentication](https://www.ktemia.com/docs/api/#authentication).

## Response fields

- `key` (object, optional): The key you authenticated with.
  - `fingerprint` (string, optional): First 8 characters of the key’s SHA-256 fingerprint. Enough to tell your keys apart in a log. Not a credential, and the key cannot be derived from it.
  - `status` (string, optional): Always `active` on a successful call. A revoked key is refused with `403 KEY_REVOKED` before it reaches this endpoint.
  - `createdAt` (string | null, optional): ISO 8601 timestamp of when the key was issued.
- `plan` (object, optional): The limits this key is subject to.
  - `name` (string, optional): Plan name: `free`, `pro`, `business`, or `enterprise`.
  - `monthlyQuota` (integer, optional): Requests included per calendar month. Reflects any custom limit set on the key, so it can differ from the published plan.
  - `requestsPerSecond` (number, optional): Sustained request rate. Exceeding it answers `429 RATE_LIMIT_EXCEEDED` with `Retry-After`.
  - `burst` (integer, optional): How many requests can arrive at once before the per-second rate applies. This is the number in `X-RateLimit-Limit`.
- `usage` (object, optional): Month-to-date consumption and what is left.
  - `month` (string, optional): The month being reported, as `YYYY-MM` in UTC.
  - `used` (integer, optional): Requests counted this month. Can exceed `monthlyQuota`, because the request that crosses the limit is itself counted.
  - `remaining` (integer, optional): `monthlyQuota` minus `used`, floored at 0.
  - `resetsAt` (string, optional): ISO 8601 timestamp of when the next month starts counting.
  - `scope` (string, optional): Whose allowance `used` describes.
    - `account` - Shared. Every key on the account draws from this one allowance, so `remaining` is not this key’s alone to spend.
    - `key` - This key has its own counter. Applies to keys issued outside the dashboard.
- `metered` (boolean, optional): Always `false`. This call does not count against the quota.

## Example: Free key, shared allowance

`GET /key` → 200

Request:

```json
{}
```

Response:

```json
{
  "key": {
    "fingerprint": "63505517",
    "status": "active",
    "createdAt": "2026-11-02T09:14:00+00:00"
  },
  "plan": {
    "name": "free",
    "monthlyQuota": 100,
    "requestsPerSecond": 2,
    "burst": 5
  },
  "usage": {
    "month": "2026-11",
    "used": 37,
    "remaining": 63,
    "resetsAt": "2026-12-01T00:00:00+00:00",
    "scope": "account"
  },
  "metered": false
}
```

## Example: Business key, own counter

`GET /key` → 200

Request:

```json
{}
```

Response:

```json
{
  "key": {
    "fingerprint": "61dae60c",
    "status": "active",
    "createdAt": "2026-09-20T11:03:00+00:00"
  },
  "plan": {
    "name": "business",
    "monthlyQuota": 250000,
    "requestsPerSecond": 250,
    "burst": 500
  },
  "usage": {
    "month": "2026-11",
    "used": 18402,
    "remaining": 231598,
    "resetsAt": "2026-12-01T00:00:00+00:00",
    "scope": "key"
  },
  "metered": false
}
```

Docs: https://www.ktemia.com/docs/api/key/
