# Filter by provider

> Canonical, always current: [ktemia.com/providers/](https://www.ktemia.com/providers/). This repository is generated from it.

Get data from one airline, booking site, or rental company only. Send its id on a search:

| Vertical | Parameter | Example |
| --- | --- | --- |
| Flights | `airlines` (up to 20 IATA codes) | `"airlines": ["UA"]` |
| Hotels | `providers` (up to 10) | `"providers": ["Booking.com"]` |
| Cars | `providers` (booking sites, up to 10) | `"providers": ["Expedia"]` |
| Cars | `agencies` (rental companies, up to 10) | `"agencies": ["hertz"]` |

Ids come from the data. Run a search without a filter, then read `availableFilters` on the results page: `airlines` for flights, `bookingSites` for hotels and cars, `agency` for cars. Coverage changes by place and date, so read the ids from a real search instead of hard-coding this list.

The lists below are what the API returned in test searches across 10 cities and 10 flight routes (collected 2026-11). Names belong to their owners and are shown only to say where prices come from; Ktemia is not affiliated with them.

## Airlines

| Airline | `airlines` id |
| --- | --- |
| Turkish Airlines | `TK` |
| United Airlines | `UA` |
| British Airways | `BA` |
| Alaska Airlines | `AS` |
| American Airlines | `AA` |
| Delta | `DL` |
| Emirates | `EK` |
| KLM | `KL` |
| Air France | `AF` |
| Ethiopian Air | `ET` |
| Finnair | `AY` |
| Iberia | `IB` |
| LOT | `LO` |
| Qatar Airways | `QR` |
| Scandinavian Airlines | `SK` |
| SWISS | `LX` |
| TAP AIR PORTUGAL | `TP` |
| Austrian Airlines | `OS` |
| easyJet | `U2` |
| ITA Airways | `AZ` |
| JetBlue | `B6` |
| Korean Air | `KE` |
| Lufthansa | `LH` |
| SAUDIA | `SV` |
| Vueling | `VY` |
| Aeromexico | `AM` |
| Air Canada | `AC` |
| Air Europa | `UX` |
| Air Serbia | `JU` |
| Asiana Airlines | `OZ` |
| Avianca | `AV` |
| Brussels Airlines | `SN` |
| Cathay Pacific | `CX` |
| Egyptair | `MS` |
| Frontier | `F9` |
| Qantas Airways | `QF` |
| Singapore Airlines | `SQ` |
| WestJet | `WS` |
| Aegean Airlines | `A3` |
| Aer Lingus | `EI` |
| Air Algerie | `AH` |
| Air India | `AI` |
| AIR PREMIA | `YP` |
| AJet | `VF` |
| ANA | `NH` |
| China Airlines | `CI` |
| China Southern | `CZ` |
| Etihad Airways | `EY` |
| Eurowings | `EW` |
| EVA Air | `BR` |
| Fiji Airways | `FJ` |
| Gulf Air | `GF` |
| Hong Kong Airlines | `HX` |
| Icelandair | `FI` |
| IndiGo | `6E` |
| Japan Airlines | `JL` |
| Jetstar | `JQ` |
| Jetstar Japan | `GK` |
| LATAM Airlines | `LA` |
| LEVEL | `LL` |
| Norwegian | `DY` |
| Oman Air | `WY` |
| Pegasus Airlines | `PC` |
| Philippine Airlines | `PR` |
| Rex | `ZL` |
| Southwest | `WN` |
| STARLUX Airlines | `JX` |
| Sun Country Air | `SY` |
| Transavia | `HV` |
| Transavia France | `TO` |
| Vietnam Airlines | `VN` |
| Virgin Atlantic | `VS` |
| Virgin Australia | `VA` |
| ZIPAIR | `ZG` |

## Hotel booking sites

| Booking site | `providers` id |
| --- | --- |
| Booking.com | `Booking.com` |
| Expedia | `Expedia` |
| Priceline | `Priceline` |
| Agoda.com | `Agoda.com` |
| HomeToGo | `HomeToGo` |
| Hotels.com | `Hotels.com` |
| Preferred Hotels | `Preferred Hotels` |
| Super.com | `Super.com` |
| Trip.com | `Trip.com` |
| Homestay.com | `Homestay.com` |
| Traveluro | `Traveluro` |
| Pricetravel | `Pricetravel` |
| Prestigia | `Prestigia` |
| Glamping Hub | `Glamping Hub` |
| IHG Hotels & Resorts | `IHG Hotels & Resorts` |
| JAPANiCAN | `JAPANiCAN` |

## Car booking sites

| Booking site | `providers` id |
| --- | --- |
| AirportRentalCars | `AirportRentalCars` |
| Auto Europe | `Auto Europe` |
| Avis | `Avis` |
| Booking.com | `Booking.com` |
| Budget | `Budget` |
| Car Rental 8 | `Car Rental 8` |
| DiscoverCars.com | `DiscoverCars.com` |
| EconomyBookings | `EconomyBookings` |
| Expedia | `Expedia` |
| Hertz | `Hertz` |
| Priceline | `Priceline` |
| QEEQ.COM | `QEEQ.COM` |
| Dollar | `Dollar` |
| Sixt | `Sixt` |
| Thrifty | `Thrifty` |
| Wisecars | `Wisecars` |
| Europcar | `Europcar` |
| Turo | `Turo` |
| Ace | `Ace` |
| NextCar | `NextCar` |
| Priceless | `Priceless` |
| Car Rental Express | `Car Rental Express` |
| GotRentalCars | `GotRentalCars` |
| Rent-A-Wreck | `Rent.a.Wreck` |
| Economy Rent a Car | `Economy` |
| NU Car | `NU car` |
| Easirent | `Easi Rent` |

## Car rental companies

| Rental company | `agencies` id |
| --- | --- |
| Alamo | `alamo` |
| Avis | `avis` |
| Budget | `budget` |
| Enterprise | `enterprise` |
| Hertz | `hertz` |
| National | `national` |
| Dollar | `dollar` |
| Sixt | `sixtrentacar` |
| Thrifty | `thrifty` |
| Europcar | `europcar` |
| Turo | `turo` |
| Fox | `fox` |
| Movly | `movly` |
| Global Rent A Car | `global` |
| GREEN MOTION | `greenmotion` |
| U-Save | `u-save` |
| Ace | `ace` |
| keddy by Europcar | `keddy` |
| NextCar | `nextcar` |
| Payless | `payless` |
| Priceless | `priceless` |
| FlexWays | `flexways` |
| SURPRICE CAR RENTAL | `surpricecarrental` |
| ADDCAR RENTAL | `addcarrental` |
| CarWiz | `carwiz` |
| Rent-A-Wreck | `rentawreck` |
| Routes Car & Truck Rentals | `routescartrk` |
| Autounion Car Rental | `autounion` |
| DISCOUNT.QUEBEC | `discount.quebec` |
| DRIVALIA | `drivalia` |
| Drive Rental Cars | `driverentalcars` |
| Economy Rent a Car | `economy` |
| Final Rentals | `finalrentals` |
| MEXRENTACAR | `mexrentacar` |
| Street Rent a Car | `streetrent` |
| Zezgo | `zezgo` |
| America Car Rental | `americacarrental` |
| NU Car | `nucar` |
| OK Mobility | `okmobility` |
| Right Cars | `rightcars` |
| Wheego | `wheego` |
| Yesaway | `yesaway` |
| York Car Rental | `yorkcarrental` |
| Zoom Rent A Car | `zoomrentals` |
| AcaRent | `acarent` |
| Advantage | `advantage` |
| Arnold Clark | `arnoldclark` |
| Centauro | `centauro` |
| Clubs Car Rental | `clubscarrental` |
| Drivo Rent A Car | `drivorentacar` |
| Easirent | `easirent` |
| EL8 Luxury Car Rental | `el8luxurycarrental` |
| Empire Rent A Car | `empire` |
| H-Lead Hospitality | `hleadhospitality` |
| HDC Rent A Car | `hdcrentacar` |
| Midway | `midwaycarren` |
| Record go | `recordgo` |
| State Van Rental | `statevan` |
| Stride | `stride` |
| United Rent A Car | `unitedrentacar` |
| Virtuo | `virtuo` |
| AAMCAR | `aamcar` |
| Alquicoche | `alquicoche` |
| Autostrad Rent A Car | `autostrad` |
| Autovia | `autovia` |
| Blitz Car Rentals | `blitzcarrentals` |
| CarQ | `carq` |
| CLICK RENT | `clickrent` |
| DiffeRental | `differental` |
| Drive Tri-State | `drivetristate` |
| Dryyve | `dryyve` |
| Ecovia | `ecovia` |
| Flex To Go | `flextogo` |
| Friendly Cars | `friendlycars` |
| Galdierirent | `galierirent` |
| Goldcar Rental SP | `goldcar` |
| Hub Rent a Car | `hubrentacar` |
| Italy Car Rent | `italycar` |
| IX Rental | `ixrental` |
| KTC Gulf Rent A Car | `ktcgulfrentacar` |
| LOCAUTO | `locauto` |
| Nichu rent a car | `nichu` |
| Nico Nico Rent-a-Car | `niconico` |
| Nissan Rent-A-Car | `nissan` |
| NIZACARS | `nizacars` |
| NOLEGGIARE | `noleggiare` |
| OptimoRent | `optimorent` |
| ORIX Rent a Car | `orix` |
| Quick Drive | `quickdrive` |
| Quicklease | `quicklease` |
| Rental Plus | `rentalplus` |
| Rentscape | `rentscape` |
| SAC Rental Cars | `sacrentalcars` |
| Shayar Rent A Car | `shayar` |
| SICILY BY CAR | `sicilybycar` |
| Skylimit Srl | `skylimitsrl` |
| Target Italy | `targetitaly` |
| Viaggiare Rent | `viaggiare` |
| Vivarent | `vivarent` |
