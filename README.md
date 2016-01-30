# proj3-ajax
Reimplement the RUSA ACP controle time calculator with flask and ajax

## ACP controle times AJAX and Flask reimplementation

The current RUSA controle time calculator is a Perl script that takes an HTML form and emits a text page. The reimplementation will fill in times as the input fields are filled.  Each time a distance is filled in, the corresponding open and close times should be filled in.   If no begin time has been provided, use 0:00 as the begin time.

## Calculation of Control Times

### Minimum and maximum speeds for ACP brevets

```
Control Location (km)  |  Minimum Speed (km/hr) | Maximum Speed (km/hr)
      0-200            |          15            |         34
      200-400          |          15            |         32
      400-600          |          15            |         30  
      600-1000         |          11.428        |         28
```

### distance, speed and time Calculation

distance (km) / speed (km/hr) = time (hr)

Convert the time into hours and minutes by subtracting the whole number of hours and multiplying the fractional part by 60. For example, 6.6666..hours will be expressed as 6H40.

### Opening times: control location / maximum

For controls above 200km, the max speed begins to reduce:
  Ex: 350km = 200/34 + 150/32 = 5H53 + 4H41 = 10H34

```
if control location = 0
      return 0


if control location 0 <= 200
      200/34


if control location 201 <= 400
      200/34 + 200/32


if control location 401 <= 600
      200/34 + 200/32 + 200/30


if control location 601 <= 1000
      200/34 + 200/32 + 200/30 + 400/28

```


### Closing times: control location / minimum

Closing time for the starting point control (at 0km) is one hour after the official start.

```
if control location = 0
      return 1

if control location 1 <= 600
      600/15

if control location 601 <= 1000
      600/15 + 400/11.428
```
### Special rules:
  - Brevets can be: 200, 300, 400, 600, 1000
  - The total distance of the route cannot be more than 10% longer than the theoretical distance, inclusive
  - Times are shown in 24-hour format
  - Minutes should be rounded to the nearest minute.
  - It is assumed that all checkpoints are located within the same time zone
  - Ending time for brevets (not calculated out):
  ```
    200km brevet is 13H30
    300km brevet is 20H00
    400km brevet is 27H00
    600km brevet is 40H00
    1000km brevet is 51H00
  ```

## Testing

Run the unit test scripts by running:
```
    python3 unit_test.py
```
