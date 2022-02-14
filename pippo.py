# https://www.youtube.com/watch?v=-nh9rCzPJ20   Visual Studio Code (Windows)
# https://www.youtube.com/watch?v=APOPm01BVrk   VENV (Windows)
import math
import os
import sys

import requests

print (sys.version)
print(sys.executable)

def greet(who_to_greet):
    test = "test"
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

#print(greet("World!"))

r = requests.get('https://coreyms.com')
print(r.status_code)

### name = input("Your name? ")
### print("Hello,", name)
