import timeDuration


def getTotalEventSpan(eventName):
    days = 0
    weeks = 0
    hours = 0
    with open("Events.txt", "r") as file:
        for line in file.readlines()[2:]:
            elements = line.split()
            if elements[0] == eventName:
                if "w" in elements[1]:
                    weeks += int(elements[1].strip("w")) * int(elements[2])
                if "d" in elements[1]:
                    days += int(elements[1].strip("d")) * int(elements[2])
                if "h" in elements[1]:
                    hours += int(elements[1].strip("h")) * int(elements[2])

    return timeDuration.TimeSpan(weeks,days,hours)


def rankEventsBySpan(*args):
    eventTimeDict={}
    eventList = list(args)
    for event in args:
        eventTimeDict[event] = getTotalEventSpan(event).getTotalHours()
    for index1, event1 in enumerate(eventList):
        for index, event in enumerate(eventList[1:]):
            if eventTimeDict[event] > eventTimeDict[eventList[index-1]]:
                temp = eventList[index-1]
                eventList[index-1] = event
                eventList[index] = temp

    return eventList





