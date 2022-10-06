from pyparrot.Bebop import Bebop
import sys

"""
- Take off, fly some distance in a pre-defined pattern, land. Do this at least twice.
- Use at least one loop and at least one conditional statement. User-defined input is welcome.
- Navigation must last at least one minute.
- Record the video of its flight in its entirety.
- The program should collect the sensor data each time a sensor is updated and output it into a file.z
"""
bebop = Bebop(drone_type="Bebop")
# bebop.set_hull_protection(1)

print("connecting")
success = bebop.connect(10)
print(success)

if success:
    # Start recording flight
    print("turning on the video")
    bebop.start_video_stream()

    # Navigation should be at least 1 minute
    # TODO: collect sensor data every time a sensor is updated and output it into a file.z

    bebop.safe_takeoff(10)
    # fly forwards
    bebop.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=2)
    bebop.smart_sleep(5)

    # do a flip!
    print("flip right")
    print("flying state is %s" % bebop.sensors.flying_state)
    working = bebop.flip(direction="right")
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
    print("flying state is %s" % bebop.sensors.flying_state)
    working = bebop.flip(direction="left")
    print("mambo flip result %s" % working)
    bebop.smart_sleep(5)
    bebop.safe_land(10)

    # REPEAT

    # TODO: take off, fly in a small square, land
    bebop.safe_takeoff(10)
    # fly forwards and backwards
    bebop.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=2)
    bebop.smart_sleep(5)

    # do a flip!
    print("flip right")
    print("flying state is %s" % bebop.sensors.flying_state)
    working = bebop.flip(direction="right")
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
    print("flying state is %s" % bebop.sensors.flying_state)
    working = bebop.flip(direction="left")
    print("mambo flip result %s" % working)
    bebop.smart_sleep(5)
    bebop.safe_land(10)

    # Stop recording flight
    print("DONE - disconnecting")
    bebop.stop_video_stream()
    bebop.disconnect()
