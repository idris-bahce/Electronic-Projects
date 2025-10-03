import RPi.GPIO as GPIO, time

# Physical pins (no 3/5). All need series resistors to GND.
ledPins = [11,12,13,15,16,18,22,29,31,32]  # = GPIO17,18,27,22,23,24,25,5,6,12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
for p in ledPins:
    GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)

def oddLedBarGraph():
    for i in range(0, len(ledPins), 2):
        GPIO.output(ledPins[i], GPIO.HIGH) 
        time.sleep(0.5)
        GPIO.output(ledPins[i], GPIO.LOW)

def evenLedBarGraph():
    for i in range(1, len(ledPins), 2):
        GPIO.output(ledPins[i], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledPins[i], GPIO.LOW)

def allLedBarGraph():
    for p in ledPins:
        GPIO.output(p, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(p, GPIO.LOW)

def fillBarGraph():
    for p in ledPins:
        GPIO.output(p, GPIO.HIGH)
        time.sleep(0.5)
    time.sleep(1)
    for i in range(9, -1, -1):
        GPIO.output(ledPins[i], GPIO.LOW)
        time.sleep(0.5)
    time.sleep(1)
    
try:
    while True:
        #oddLedBarGraph();  time.sleep(0.2)
        #evenLedBarGraph(); time.sleep(0.2)
        #allLedBarGraph();  time.sleep(0.2)
        fillBarGraph()
except KeyboardInterrupt:
    pass
finally:
    for p in ledPins: GPIO.output(p, GPIO.LOW)
    GPIO.cleanup()
