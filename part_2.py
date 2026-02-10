def rover_status():


    statuses = {
        "battery": 100,
        "heater" : "off",
        "camera" : "standby"
    }

    print (statuses["battery"])

def status_update(statuses):
    statusupdate = {
        "battery": 85,
        "heater": "on",
        "camera": "standby",
        "speed": 5
    }
    yes = input("status update?")
    if yes == "yes":
        print(statusupdate)
    else:
        print (statuses["battery"])
status_update(rover_status())

def mission_log():
    missionlog = []
    dictionary1 = {
        "Site": "Crater A",
        "Radiation": "Low",
        "Water": False
    }
    dictionary2 = {
        "Site": "Dune B",
        "Radiation": "High",
        "Water": True
        }
    for i in range(1):
        print (dictionary1)
        print (dictionary2)
mission_log()