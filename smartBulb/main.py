from yeelight import discover_bulbs

from bulb import My_bulb

if __name__ == '__main__':
    print("Scanning the network..")
    scan = discover_bulbs()

    print("Available devices : " + scan[0]["ip"])
    ip = input("\nPlease enter the IP of the Bulb: ")

    bulb = My_bulb(ip)
    bulb.start_music()

while True:
    massage = input("\nEnter your Message to send it in morse code: ")
    bulb.morse_code(massage)
