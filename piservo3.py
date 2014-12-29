import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

def set_angle(angle):
	if angle<20:
		angle=20
	if angle>90:
		angle=90

	duty = float(angle) / 10.0 + 2.5
	pwm.ChangeDutyCycle(duty)

set_angle(0)
time.sleep(1)

set_angle(180)
time.sleep(1)

#def elasped_since_start():
#	n2=dt.datetime.now()
#	return (n2-n1).microseconds/1e6

#class App:
pwm.stop()
