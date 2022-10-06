"""
Land
"""


def string_to_file(strInput):
    """Function to take a string and put it in a file."""
    text_file = open("data.txt", "w")
    text_file.write(strInput)
    text_file.close()


from pyparrot.Bebop import Bebop

bebop = Bebop(drone_type="Bebop")
# bebop.set_hull_protection(1)

# print("connecting")
success = bebop.connect(10)
print(success)

if success:
    test = bebop.sensors.battery

    string_to_file(str(test))

    print("DONE - disconnecting")
    bebop.disconnect()
