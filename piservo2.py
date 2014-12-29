#sudo apt-get install python-setuptools
#easy_install -U RPIO

import time
import datetime as dt
n1=dt.datetime.now()

from RPIO import PWM
servo = PWM.Servo()
#min 600, max 2500
#servo.set_servo(18, 2500)


#delay_period = 0.02
delay_period = 0.035
def angle_t( a ):
	min_a = 0
	max_a = 160
	min_t = 1000
	max_t = 2000
	if a < min_a:
		a = min_a
	if a > max_a:
		a = max_a
	return (a-min_a)/(max_a-min_a)*(max_t-min_t) + min_t;

def elasped_since_start():
	n2=dt.datetime.now()
	return (n2-n1).microseconds/1e6

def set_servo_angle(a):
	t = angle_t(a)
	print "Angle: " + repr(a) + ", pulse width = " + repr(t) + " us"
	servo.set_servo(18, t)

while elasped_since_start()<1:
	set_servo_angle(0)

#while elasped_since_start()<2:
#	set_servo_angle(160)

#for a in range(0, 1600):
#	set_servo_angle(a/10)

#for a in range(1600, 0, -1):
#	set_servo_angle(a/10)
