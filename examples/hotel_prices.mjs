// London hotels priced by Hotels.com only. Node 18+.
// KTEMIA_API_KEY=... node hotel_prices.mjs
// Walkthrough: https://www.ktemia.com/blog/hotel-price-api/

const API = "https://api.ktemia.com";
const headers = { "X-API-Key": process.env.KTEMIA_API_KEY, "Content-Type": "application/json" };

const search = await fetch(`${API}/hotels/search`, {
  method: "POST",
  headers,
  body: JSON.stringify({
    location: "29230", // London, from /hotels/locations
    checkin: "2026-12-05",
    checkout: "2026-12-07",
    adults: 2,
    providers: ["Hotels.com"],
  }),
}).then((res) => res.json());

const page = await fetch(`${API}/hotels/results?token=${encodeURIComponent(search.searchToken)}`, { headers }).then(
  (res) => res.json(),
);
for (const hotel of page.hotels) {
  console.log(hotel.name, hotel.bestOption.provider, hotel.bestOption.price.formatted);
}
