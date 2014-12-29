import time

from RPIO import PWM
servo = PWM.Servo()
#min 600, max 2500
#servo.set_servo(18, 2500)


#delay_period = 0.02
delay_period = 0.035

while True:
	for angle in range(7, 24):
		#servo.set_servo(18, (31-angle)*100)
		servo.set_servo(18, angle*100)
		time.sleep(delay_period)
	for angle in range(7, 24):
		servo.set_servo(18, (31-angle)*100)
		time.sleep(delay_period)
