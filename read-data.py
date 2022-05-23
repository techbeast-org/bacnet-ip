import BAC0
import json
import time
bacnet = BAC0.lite(ip="192.168.18.6/24" ,port=47809)  
data = {}


def main():
    while True:
        for x in range(0, 3):
            id = str(x)
            value = bacnet.read(
                "192.168.18.10:53522 analogInput "+id+" presentValue")
            value = str(value)
            data["Analog_input"+id] = value

        print(json.dumps(data, indent=2))
        time.sleep(5)


if __name__ == '__main__':
    main()
