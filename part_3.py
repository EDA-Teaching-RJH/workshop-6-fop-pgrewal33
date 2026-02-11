def motor_controller():
    try:
        motor_speed = int(input("enter motor speed: "))
        print (f"set speed to {motor_speed}")

    except ValueError:
        print ("Error: Corrupted Signal. Maintaining current speed.")

motor_controller()

def get_coordinates():
    while True:

        coordinate = input("enter x coordinate: ")
    
        if not coordinate.isdigit():
            print ("invalid coordinate")
            
        
        else:
            break
    
get_coordinates()

