# proj3-ajax
Reimplement the RUSA ACP controle time calculator with flask and ajax

## ACP controle times AJAX and Flask reimplementation

The current RUSA controle time calculator is a Perl script that takes an HTML form and emits a text page. The reimplementation will fill in times as the input fields are filled.  Each time a distance is filled in, the corresponding open and close times should be filled in.   If no begin time has been provided, use 0:00 as the begin time.

### Author

Megan McMillan

### Project Link


## Setup and Run Project
1. Modify Makefile and CONFIG.py to point to the appropriate local environment variables.
2. Run ```make install```
3. Activate the virtual environment by running ```. env/bin/activate```
4. Run ```python3 app.py```


# Calculation of Control Times

### Minimum and Maximum speeds for ACP brevets

```
Control Location (km)  |  Minimum Speed (km/hr) | Maximum Speed (km/hr)
      0-200            |          15            |         34
      200-400          |          15            |         32
      400-600          |          15            |         30  
      600-1000         |          11.428        |         28
```

### Distance, Speed and Time Calculation

distance (km) / speed (km/hr) = time (hr)

### Opening Times:

Control Location / Maximum Speed = Opening Time

For controls above 200km, the max speed begins to reduce:
  Ex: 350km = 200/34 + 150/32 = 5H53 + 4H41 = 10H34

### Closing Times:

Control Location / Minimum Speed = Closing Time

For controls above 600km, the max speed begins to reduce:
  Ex: 650km = 600/15 + 50/11.428 = 4H00 + 4H23 = 8H23

### Special Rules:
  - Brevets can be: 200, 300, 400, 600, 1000
  - Ending time for brevets:

```
  200km brevet is 13H30
  300km brevet is 20H00
  400km brevet is 27H00
  600km brevet is 40H00
  1000km brevet is 51H00
```

  - Closing time for the starting point control (at 0km) is one hour after the official start.
  - The total distance of the route cannot be more than 10% longer than the theoretical distance.
  - Times are shown in 24-hour format.
  - Minutes should be rounded to the nearest minute.
  - It is assumed that all checkpoints are located within the same time zone.

### Form Rules
- Control point distance field only takes numbers
- If a setting is changed above, all modified form elements should update accordingly

## Testing

Run the unit test scripts by running:
```
    python3 unit_test.py
```
