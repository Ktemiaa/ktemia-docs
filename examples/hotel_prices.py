# Search London hotels, read the booking sites, filter to two, compare.
# pip install requests && KTEMIA_API_KEY=... python3 hotel_prices.py
# Walkthrough: https://www.ktemia.com/blog/hotel-price-api/

import os
import requests

API = "https://api.ktemia.com"
HEADERS = {"X-API-Key": os.environ["KTEMIA_API_KEY"]}
STAY = {"checkin": "2026-12-05", "checkout": "2026-12-07", "adults": 2}

# 1. Turn a name into a location id.
places = requests.get(f"{API}/hotels/locations", headers=HEADERS, params={"query": "London"}).json()
location = places["locations"][0]["locationId"]

# 2. Open search: which booking sites sell stays here?
token = requests.post(f"{API}/hotels/search", headers=HEADERS, json={"location": location, **STAY}).json()["searchToken"]
page = requests.get(f"{API}/hotels/results", headers=HEADERS, params={"token": token}).json()
for site in page["availableFilters"]["bookingSites"]["options"]:
    print(site["id"], site["count"])

# 3. Search again, priced by two sites only.
token = requests.post(
    f"{API}/hotels/search",
    headers=HEADERS,
    json={"location": location, **STAY, "providers": ["Booking.com", "Expedia"]},
).json()["searchToken"]
page = requests.get(f"{API}/hotels/results", headers=HEADERS, params={"token": token}).json()
hotel = page["hotels"][0]
print(hotel["name"], hotel["bestOption"]["provider"], hotel["bestOption"]["price"]["formatted"])

# 4. Every seller for that hotel, with a booking link.
details = requests.get(
    f"{API}/hotels/details", headers=HEADERS, params={"token": token, "resultId": hotel["id"]}
).json()
for option in details["bookingOptions"]:
    total = (option.get("totalPrice") or {}).get("formatted")
    print(option["provider"], option["price"]["formatted"], total, option["providerUrl"])
