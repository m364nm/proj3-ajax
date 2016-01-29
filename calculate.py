
"""brevet_distance
start_date
start_time

input_units

control_distance"""

import arrow

###
# initializing the global variables
###
global brevet
brevet = 0

global startdatetime
startdatetime = arrow.utcnow()

global units
units = "km"

###
# Input: location in km
# Output: opening time for the control location in HH:mm
###
def get_opening_time(location): #in km
    if location == 0:
        return parse_time(0)
    elif location <= 200:
        return parse_time(location/34)
    elif location <= 400:
        tmp = location-200
        return parse_time(200/34 + tmp/32)
    elif location <= 600:
        tmp = location-400
        return parse_time(200/34 + 200/32 + tmp/30)
    elif location <= 1000:
        tmp = location-600
        return parse_time(200/34 + 200/32 + 200/30 + tmp/28)
    else:
        return parse_time(200/34 + 200/32 + 200/30 + 400/28)

###
# Input: location in km
# Output: closing time for the control location in HH:mm
###
def get_closing_time(location): #in km
    if location == 0:
        return parse_time(1)
    elif location <= 600:
        return parse_time(location/15)
    elif location <= 1000:
        tmp = location-600
        return parse_time(600/15 + tmp/11.428)
    else:
        return parse_time(600/15 + 400/11.428)


def get_special_case(location):
    if location == 200:
        return "{}:{}".format(13, 30)
    elif location == 300:
        return "{}:{}".format(20, 00)
    elif location == 400:
        return "{}:{}".format(27, 00)
    elif location == 600:
        return "{}:{}".format(40, 00)
    else: #brevet is 1000
        return "{}:{}".format(51, 00)


###
# Takes a float time and formats as HH:mm
###
def parse_time(time):
    decimal = time - int(time)
    minutes = decimal*60
    return "{}:{}".format(int(time), int(minutes))


###
# Input: distance
# Output: the open and close date/time of the control location in list:
#            list[0] = opening date and time
#            list[1] = closing date and time
#         return -1 if the distance is greater than 10% of the brevet
###
def calc(dist):

    if units == "mi":
        distance = 0
    else:
        distance = dist

    ## The route distance must not be longer than 10% + the brevet
    print ("in calc, distance = {}, brevet = {}".format(distance, brevet))
    if (distance/brevet) > 1.10:
        print ("throw error: you cannot have a control longer than 10% of the total distance")
        return -1
    else:
        ## When the distance we are dealing with is the brevet length or greater,
        ## then return the special case, else get the opening and closing times
        if distance >= brevet:
            opentime = get_opening_time(distance)
            closetime = get_special_case(distance)
        else:
            opentime = get_opening_time(distance)
            closetime = get_closing_time(distance)

        open_time = opentime.split(":")
        close_time = closetime.split(":")

        start_date_time = startdatetime.replace(hours=+int(open_time[0]), minutes=+int(open_time[1]))
        close_date_time = startdatetime.replace(hours=+int(close_time[0]), minutes=+int(close_time[1]))

        return [start_date_time, close_date_time]
