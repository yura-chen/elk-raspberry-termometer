from jsonsocket import Client
import time
import socket
import json
import random
from thermostat import get_temperature

# Logstash TCP/JSON Host
JSON_PORT = 5000
# JSON_HOST = '192.168.3.177'

JSON_HOST = socket.gethostname()

CM_PER_SEC_AIR = 34300


if __name__ == '__main__':
    try:

        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect((JSON_HOST, JSON_PORT))
        client = Client()

        devices = ['device1', 'device2', 'device3', 'device4', 'device5']

        while True:

            for device in devices:
                temperature = get_temperature()
                data = {'message': 'temperature %.1f C' % temperature, 'temperature': temperature, 'device' : device, 'hostname': socket.gethostname()}
                print(json.dumps(data))

                client.connect(JSON_HOST, JSON_PORT).send(data)

                print ("Received temperature = %.1f C" % temperature)
            time.sleep(1)

    # interrupt
    except KeyboardInterrupt:
        print("Programm interrupted")
        client.close()
