# rainbow_rgb.py
import RPi.GPIO as GPIO
import time, colorsys
import math

# === CONFIG ===
R, G, B = 17, 18, 27        # BCM pins for Red, Green, Blue
FREQ_HZ = 400               # PWM frequency (smooth enough, low CPU)
STEP = 0.002                # Hue step (smaller = smoother/slower)
SLEEP = 0.01                # Delay between updates (smaller = smoother)
GAMMA = 2.2                 # Gamma correction (perceived brightness)
COMMON_ANODE = False        # You have common-cathode, so keep False

def to_duty(x01):
    """Map 0..1 ? 0..100 with gamma correction; invert if common anode."""
    # Clamp
    x = 0.0 if x01 < 0 else (1.0 if x01 > 1 else x01)
    # Gamma correction (optional but makes fades look nicer)
    if GAMMA:
        x = math.pow(x, 1.0 / GAMMA)
    duty = x * 100.0
    if COMMON_ANODE:
        duty = 100.0 - duty
    return duty

def set_rgb(pR, pG, pB, r, g, b):
    """r,g,b in 0..1"""
    pR.ChangeDutyCycle(to_duty(r))
    pG.ChangeDutyCycle(to_duty(g))
    pB.ChangeDutyCycle(to_duty(b))

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R, GPIO.OUT); GPIO.setup(G, GPIO.OUT); GPIO.setup(B, GPIO.OUT)
    pR = GPIO.PWM(R, FREQ_HZ); pG = GPIO.PWM(G, FREQ_HZ); pB = GPIO.PWM(B, FREQ_HZ)
    pR.start(0); pG.start(0); pB.start(0)

    try:
        hue = 0.0
        while True:
            # colorsys: hsv(h, s, v) with h?[0,1)
            r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            set_rgb(pR, pG, pB, r, g, b)
            hue += STEP
            if hue >= 1.0:
                hue -= 1.0
            time.sleep(SLEEP)
    except KeyboardInterrupt:
        pass
    finally:
        pR.stop(); pG.stop(); pB.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
