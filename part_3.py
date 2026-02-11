def motor_controller():
    while True:    
        try:
            motor_speed = int(input("enter motor speed: "))
            if motor_speed >= 100:
                print("out of range")
            elif motor_speed <= 0:
                print("out of range")
            else:
                print (f"set speed to {motor_speed}")
                break

        except ValueError:
            print ("Error: Corrupted Signal. Maintaining current speed.")

motor_controller()

def get_coordinates():
    while True:

        coordinate =  input("enter x coordinate: ")
    
        if not coordinate.isdigit():
            print ("invalid coordinate")
        elif coordinate.isdigit() >= 100:
            print("out of range")
        elif coordinate.isdigit() <= -100:
            print("out of range")
        else:
            break
    
get_coordinates()

