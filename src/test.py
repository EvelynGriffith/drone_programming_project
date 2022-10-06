from pyparrot.Bebop import Bebop

bebop = Bebop(drone_type="Bebop")

print("connecting")
success = bebop.connect(10)
print(success)

if success:
    print("turning on the video")
    bebop.start_video_stream()

    print("sleeping")

    bebop.smart_sleep(2)

    bebop.ask_for_state_update()

    bebop.safe_takeoff(10)

    # set safe indoor parameters
    bebop.set_max_tilt(5)
    bebop.set_max_vertical_speed(1)

    # trying out the new hull protector parameters - set to 1 for a hull protection and 0 without protection
    # bebop.set_hull_protection(1)

    print("Flying direct: Slow move for indoors")
    bebop.safe_takeoff(10)
    # fly forward and backwards
    bebop.fly_direct(roll=20, pitch=0, yaw=0, vertical_movement=0, duration=2)
    # bebop.fly_direct(roll=20, pitch=0, yaw=0, vertical_movement=0, duration=2)
    bebop.fly_direct(roll=-60, pitch=0, yaw=0, vertical_movement=0, duration=2)
    # bebop.fly_direct(roll=-20, pitch=0, yaw=0, vertical_movement=0, duration=2)
    # bebop.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=2)
    bebop.smart_sleep(2)

    bebop.safe_land(10)

    print("DONE - disconnecting")
    bebop.stop_video_stream()
    bebop.smart_sleep(5)
    print(bebop.sensors.battery)
    bebop.disconnect()
