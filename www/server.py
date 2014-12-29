import time
import BaseHTTPServer
import subprocess
import os.path
import json
from sys import stderr
import RPi.GPIO as GPIO

HOST_NAME = subprocess.check_output("hostname -I | sed \"s/ .*//g\" | tr -d '\n'", shell=True)
PORT_NUMBER = 9000
rootpath = os.getcwd()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 20)
pwm.start(5)

def set_angle(angle):
    min_angle = 0
    max_angle = 90
    if angle<min_angle:
        angle=min_angle
    if angle>max_angle:
        angle=max_angle

    max_duty = 5.3
    min_duty = 0.1
    print >> stderr, "angle = %g" % angle
    duty = (float(angle) - min_angle)/(max_angle-min_angle)*(max_duty-min_duty)+min_duty
    pwm.ChangeDutyCycle(duty)

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        """Respond to a GET request."""

        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        localfilename = rootpath + s.path
        if s.path=="/":
            localfilename = rootpath + "/index.html"
        if not os.path.isfile(localfilename):
            s.send_response(404)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write("<html><head><title>File not found.</title></head>")
            s.wfile.write("<body><p>File not found.</p>")
            s.wfile.write("<p>You accessed path: %s</p>" % s.path)
            s.wfile.write("</body></html>")
        else:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()

            with open(localfilename,'r') as f:
                 s.wfile.write(f.read())

    def do_PUT(self):
        #print >> stderr, "----- SOMETHING WAS PUT!! ------"
        #print self.headers
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self.send_response(200)
        print >> stderr, content

        try:
            v = json.loads(content)
            set_angle(v["value"])
        except Exception as x:
            print >> stderr, x
            pass

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print >> stderr, time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print >> stderr, time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
