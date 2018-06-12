import mraa
import time

print "About to test mraa"
print mraa.getVersion()

# initialise gpio 23
gpio_pin = mraa.Gpio(12)

# set gpio 23 to output
gpio_pin.dir(mraa.DIR_OUT)

# toggle both gpio's
while True:
    gpio_pin.write(1)
    print "On"

    time.sleep(1)

    gpio_pin.write(0)
    print "Off"

    time.sleep(1)
