def number(bus_stops):
    # Good Luck!
    passengers = 0
    for stop in bus_stops:
        passengers += stop[0]
        passengers -= stop[1]
    return passengers


number([[10, 0], [3, 5], [5, 8]])
number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])
number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]])
