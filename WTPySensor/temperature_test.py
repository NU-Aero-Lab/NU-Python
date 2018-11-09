import time

from envirophat import weather


print("""Temperature Output. Press Ctrl+C to exit""")

try:
    while True:
        temperature = weather.temperature()

        print("{} degrees Celsius".format(temperature))
        time.sleep(5)
except KeyboardInterrupt:
    pass
