import calculate

def run_test(control_dist):
    print("\ncontrol location = {}".formatcontrol_dist))
    test = calculate.calc(control_dist)
    if test == -1:
        return
    start = test[0].format("MMM.DD.YYYY HH:mm")
    finish = test[1].format("MMM.DD.YYYY HH:mm")
    print (start)
    print (finish)
