from evdev import InputDevice, ecodes
gamepad = InputDevice('/dev/input/event1')
import RPi.GPIO as gpio

#setup gpio pins
gpio.setmode(gpio.BCM)
gpio.setup(6, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.setup(26, gpio.OUT)
gpio.setup(13, gpio.OUT)

#Define variables
aBtn = 304 #'A' button is the button with the identity '304'
bBtn = 305 #'B' button is the button with the identity '305'
xBtn = 307
yBtn = 308

lB = 310
rB = 311

rJ = 05
lJ = 02

#start of main code loop
print(gamepad)

for event in gamepad.read_loop():
    #Code loop for button controls
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            p = gpio.PWM(6, 600)
            if event.code == aBtn:
                print("A")
                p.start(20)
                gpio.output(5, 0)
            elif event.code == bBtn:
                print("B")
                p.start(20)
                gpio.output(5, 1)
            elif event.code == xBtn:
                print("X")
                p.start(100)
                gpio.output(5, 0)
            elif event.code == yBtn:
                print("Y")
                p.start(100)
                gpio.output(5, 1)
        elif event.value == 0:
            p.stop()
    #Code loop for trigger controls
    elif event.type == ecodes.EV_ABS:
        if event.code == rJ:
            print(event.value/2.55)
            z = gpio.PWM(26, 200)
            z.start(event.value/2.55)
            gpio.output(13, 0)
        elif event.code == lJ:
            print(event.value/2.55)
            z = gpio.PWM(26, 200)
            z.start(event.value/2.55)
            gpio.output(13, 1)
        elif event.code != rJ or lJ:
            z.stop()

gpio.cleanup()
command.mainloop()
