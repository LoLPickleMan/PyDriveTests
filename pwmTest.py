import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

t1 = GPIO.PWM(7, 50)

t1.start(0)
#some changed
t1.ChangeDutyCycle(7.5)
time.sleep(30)

t1.stop()

GPIO.cleanup()
quit()
