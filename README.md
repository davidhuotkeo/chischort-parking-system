# Chis Chort [ជិះចត] Parking Service System

## Table of Content
```
- Purposes
- To do
- System Explaination
```

## Purposes
We create this in order to **ease out** the street parking and **helping** the cambodia's traffic better in *the future*.

## To do
We create this with **python** as backend.
This makes it easier for us to inspect in each laptop locally.
*Make sure you install python before running this*

to do this, we write command:

### Linux / Macos
```
$ source env/bin/activate
$ python3 run.py
```

### Windows
```
$ /env/bin/activate
$ python3 run.py
```

## System Explaination
How this work is
1. People write their email (Bottom of homepage) to get email tickets from ChisChort (This is for the offline purpose / Prevent the lost of tickets if the user forgot to screen shot their ticket) [Optional]
2. When People parked, they take out their camera's phone and scan the lane QRCode that they park to get the url for the ticket
3. There will be the page where the there is an option for normal parking or extra service like tire checking
4. The user will get a *pretty ticket* and it's for screenshot to prevent the error system
5. After they want to get out, the security will scan the QRCode from the ticket and pay to the security guard as the balance shown on the security guard's phone.
