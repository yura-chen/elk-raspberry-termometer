from time import sleep

while True:
  sleep(300)
  with open('/sys/class/thermal/thermal_zone0/temp') as temp:
    curCtemp = float(temp.read()) / 1000
    print ("C:", curCtemp)
