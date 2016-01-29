import calculate

def run_test(test_num, brevet_dist, control_dist):
    print("\nTest Num {} \nbrevet = {}, control location = {}".format(test_num, brevet_dist, control_dist))
    test = calculate.calc(control_dist)
    if test == -1:
        return
    start = test[0].format("MMM.DD.YYYY HH:mm")
    finish = test[1].format("MMM.DD.YYYY HH:mm")
    print (start)
    print (finish)

if __name__ == "__main__":
    ## run_test(test_num, brevet_dist, control_dist)

    ### Need to add in a comparing test to test expected vs actual
    print("\n----------------------------")
    # Brevet = 200
    calculate.brevet = 200
    run_test(1.0, 200, 0)
    run_test(1.1, 200, 1)
    run_test(1.2, 200, 199)
    run_test(1.3, 200, 200)
    run_test(1.4, 200, 201)
    run_test(1.5, 200, 220)
    run_test(1.6, 200, 225)

    print("\n----------------------------")
    # Brevet = 300
    calculate.brevet = 300
    run_test(2.0, 300, 0)
    run_test(2.1, 300, 200)
    run_test(2.2, 300, 299)
    run_test(2.3, 300, 300)
    run_test(2.4, 300, 330)
    run_test(2.5, 300, 340)

    print("\n----------------------------")
    # Brevet = 400
    calculate.brevet = 400
    run_test(3.0, 400, 0)
    run_test(3.1, 400, 300)
    run_test(3.2, 400, 399)
    run_test(3.3, 400, 400)
    run_test(3.4, 400, 440)
    run_test(3.5, 400, 441)

    print("\n----------------------------")
    # Brevet = 600
    calculate.brevet = 600
    run_test(4.0, 600, 0)
    run_test(4.1, 600, 200)
    run_test(4.2, 600, 599)
    run_test(4.3, 600, 600)
    run_test(4.4, 600, 660)
    run_test(4.5, 600, 661)

    print("\n----------------------------")
    # Brevet = 1000
    calculate.brevet = 1000
    run_test(5.0, 1000, 0)
    run_test(5.1, 1000, 400)
    run_test(5.2, 1000, 999)
    run_test(5.3, 1000, 1000)
    run_test(5.4, 1000, 1001)
    run_test(5.5, 1000, 1100)
    run_test(5.6, 1000, 1101)
