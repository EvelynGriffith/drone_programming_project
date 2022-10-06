from pyparrot.Bebop import Bebop
import sys

"""
- Take off, fly some distance in a pre-defined pattern, land. Do this at least twice.
- Use at least one loop and at least one conditional statement. User-defined input is welcome.
- Navigation must last at least one minute.
- Your drone should take at least five photos during each leg of the flight (from take off to landing) and record the video of its flight in its entirety.
- The program should collect the sensor data each time a sensor is updated and output it into a file.z
"""


def string_to_file(strInput):
    """Function to take a string and put it in a file."""
    text_file = open("data.txt", "w")
    text_file.write(strInput)
    text_file.close()


bebop = Bebop(drone_type="Bebop")
# bebop.set_hull_protection(1)

print("connecting")
success = bebop.connect(10)
print(success)

if success and len(sys.argv > 1):
    # Start recording flight
    print("turning on the video")
    bebop.start_video_stream()

    # TODO: collect sensor data every time a sensor is updated and output it into a file.z
    # ex. photos, battery percentage, flip statements, positional
    # bebop.ask_for_state_update()

    # runs for the amount of time the user inputs
    # only enter 1 or 2 to be safe.
    inputNum = sys.Argv[1]
    for i in range(inputNum):
        battery = bebop.sensors.battery
        string_to_file(str(battery))

        bebop.safe_takeoff(10)
        # fly forwards

        bebop.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=2)
        bebop.smart_sleep(5)

        # do a flip!
        print("flip right")
        state = bebop.sensors.flying_state
        print("flying state is %s" % bebop.sensors.flying_state)
        string_to_file(state)
        working = bebop.flip(direction="right")
        string_to_file(working)
        print("mambo flip result %s" % working)
        # bebop.smart_sleep(5)
        # bebop.safe_land(10)

        # take off, fly in a small square, land
        # bebop.safe_takeoff(10)
        # fly forwards and backwards
        bebop.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=2)
        bebop.smart_sleep(5)

        # do a flip!
        print("flip left")
        state = bebop.sensors.flying_state
        print("flying state is %s" % bebop.sensors.flying_state)
        string_to_file(state)
        working = bebop.flip(direction="left")
        string_to_file(working)
        print("mambo flip result %s" % working)
        bebop.smart_sleep(5)
        bebop.safe_land(10)

        battery = bebop.sensors.battery
        string_to_file(str(battery))

    # Stop recording flight
    print("DONE - disconnecting")
    bebop.stop_video_stream()
    bebop.disconnect()
