#list of all the built in modules -> https://docs.python.org/3/py-modindex.html




import math
import mymodule
import requests

print(math.sqrt(64))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)
r1 = requests.get("https://www.linkedin.com/s-mandy")
print(r1.text)