# Search airlines

> Canonical, always current: [ktemia.com/docs/api/flights/airlines/](https://www.ktemia.com/docs/api/flights/airlines/). This repository is generated from it.


Look up an airline code by name. Use the code on airlines when you search flights. Code in cURL, Python, Node, Go, Java, Ruby, and PHP.

Base URL: https://api.ktemia.com
Authentication: send header `X-API-Key` on every request.

`GET /flights/airlines`

Find the airline codes a flight search accepts on airlines.

The `airlines` field on a flight search takes 2-character codes, not names. This call turns “Delta” or `DL` into the `code` you send.

Send `X-API-Key` the same way as on every other call. `query` is required. `country` and `locale` are optional and default to US and `en`.

## Which code to send

Use `airlines[].code` on [Search flights](https://www.ktemia.com/docs/api/flights/search/), inside `airlines`. `DL` is Delta. `LH` is Lufthansa. Codes longer than two characters are left out, because the search rejects them.

A query that matches nothing returns `200` with an empty `airlines` list. A missing `query`, a blank `query`, a bad `locale`, or an unsupported `country` returns `400`. If the lookup itself fails, the response is `502 AIRLINES_UNAVAILABLE`.

## Query parameters

- `query` (string, required): Airline name or code. 1 to 80 characters. A blank value is rejected.
- `country` (string, optional): ISO 3166-1 alpha-2 market. Omit it for US. Any other value is rejected. Same set as on a flight search.
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
- `airlines` (array of objects, required): Matching airlines, best match first. Empty when nothing matches. Only codes a flight search accepts are included.
  - `code` (string, required): 2-character IATA airline code. Send this in `airlines` on a flight search.
  - `name` (string, required): Airline name.
  - `logo` (string, optional): Logo image URL, when one is available.

## Example: Delta

`GET /flights/airlines` → 200

Request:

```json
{
  "query": "delta",
  "country": null,
  "locale": null
}
```

Response:

```json
{
  "query": "delta",
  "airlines": [
    {
      "code": "DL",
      "name": "Delta",
      "logo": "https://content.r9cdn.net/rimg/provider-logos/airlines/h/DL.png?…"
    }
  ]
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/flights/airlines/)._

## Example: Lufthansa

`GET /flights/airlines` → 200

Request:

```json
{
  "query": "lufthansa"
}
```

Response:

```json
{
  "query": "lufthansa",
  "airlines": [
    {
      "code": "LH",
      "name": "Lufthansa",
      "logo": "https://content.r9cdn.net/rimg/provider-logos/airlines/h/LH.png?…"
    },
    {
      "code": "CL",
      "name": "Lufthansa CityLine",
      "logo": "https://content.r9cdn.net/rimg/provider-logos/airlines/h/CL.png?…"
    }
  ]
}
```

_Trimmed: lists to 3 items, and query strings removed from URLs (shown as `?…`). Live responses return full booking URLs. The captured response is on [the canonical page](https://www.ktemia.com/docs/api/flights/airlines/)._

## Skill

Claude Code, Cursor, and Codex can search with the Ktemia skills: `flight-search`, `car-search`, and `hotel-search`.
https://github.com/Ktemiaa/ktemia-skills

Install in Claude Code:

```
/plugin marketplace add Ktemiaa/ktemia-skills
/plugin install ktemia@ktemia
```

Set `KTEMIA_API_KEY` in the environment. The flight skill looks up airport codes, asks when a name matches several cities, and returns each seller’s booking URL. It does not book tickets. Do not guess origin, destination, or dates.

Docs: https://www.ktemia.com/docs/api/flights/airlines/
