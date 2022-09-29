"""
Land
"""

from pyparrot.Bebop import Bebop

bebop = Bebop(drone_type="Bebop")

print("connecting")
success = bebop.connect(10)
print(success)

if (success):
    bebop.safe_takeoff(5)
    bebop.smart_sleep(5)
    bebop.safe_land(5)

    print("DONE - disconnecting")
    bebop.disconnect()
