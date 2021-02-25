import queue


def simulate(time, trafficSignals, cars, pointPerCar):
    cost = 0
    for i in range(0, time):
        toRemove = []
        for trafficLight in trafficSignals:
            trafficLight.updateRoad()
        for car in cars:

            temp = car.updateCar()
            if temp == 1:
                cost += pointPerCar + (time - 1)
                toRemove.append(car)
        for car in toRemove:
            cars.remove(car)
    return cost
