from yeelight import discover_bulbs

from bulb import My_bulb

if __name__ == '__main__':
    print("Scanning the network..")
    scan = discover_bulbs()

    print("Available devices : " + scan[0]["ip"])
    ip = input("Please enter the ip of the bulb: ")

    bulb = My_bulb(ip)
    bulb.start_music()

while True:
    massage = input("\nEnter your massage to send it in morse code: ")
    bulb.morse_code(massage)
