import RPi.GPIO as GPIO
import time

# BCM pin numbers for R, G, B
R, G, B = 17, 18, 27

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

# Create PWM objects at 100Hz (enough for smooth fades, not flicker)
pR = GPIO.PWM(R, 100)
pG = GPIO.PWM(G, 100)
pB = GPIO.PWM(B, 100)

# Start with LEDs off
pR.start(0)
pG.start(0)
pB.start(0)

def fade_channel(pwm, delay=0.02):
    """Fade one channel up and down"""
    for duty in range(0, 101, 5):   # 0% -> 100%
        pwm.ChangeDutyCycle(duty)
        time.sleep(delay)
    for duty in range(100, -1, -5): # 100% -> 0%
        pwm.ChangeDutyCycle(duty)
        time.sleep(delay)

try:
    while True:
        # Fade Red
        fade_channel(pR)
        # Fade Green
        fade_channel(pG)
        # Fade Blue
        fade_channel(pB)
        # Fade mixes (two at once)
        # Yellow
        for duty in range(0, 101, 5):
            pR.ChangeDutyCycle(duty)
            pG.ChangeDutyCycle(duty)
            time.sleep(0.02)
        for duty in range(100, -1, -5):
            pR.ChangeDutyCycle(duty)
            pG.ChangeDutyCycle(duty)
            time.sleep(0.02)
        # Cyan
        for duty in range(0, 101, 5):
            pB.ChangeDutyCycle(duty)
            pG.ChangeDutyCycle(duty)
            time.sleep(0.02)
        for duty in range(100, -1, -5):
            pB.ChangeDutyCycle(duty)
            pG.ChangeDutyCycle(duty)
            time.sleep(0.02)
        # Magenta
        for duty in range(0, 101, 5):
            pR.ChangeDutyCycle(duty)
            pB.ChangeDutyCycle(duty)
            time.sleep(0.02)
        for duty in range(100, -1, -5):
            pB.ChangeDutyCycle(duty)
            pR.ChangeDutyCycle(duty)
            time.sleep(0.02)
        # Fade White (all together)
        for duty in range(0, 101, 5):
            pR.ChangeDutyCycle(duty)
            pG.ChangeDutyCycle(duty)
            pB.ChangeDutyCycle(duty)
            time.sleep(0.02)
        for duty in range(100, -1, -5):
            pR.ChangeDutyCycle(duty)
            pG.ChangeDutyCycle(duty)
            pB.ChangeDutyCycle(duty)
            time.sleep(0.02)

except KeyboardInterrupt:
    pass
finally:
    pR.stop(); pG.stop(); pB.stop()
    GPIO.cleanup()
