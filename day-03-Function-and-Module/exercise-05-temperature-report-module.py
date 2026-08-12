from temperature_utils import celsius_to_fahrenheit, fahrenheit_to_celsius, MODULE_VERSION
import random, datetime

module_code = '''
def celsius_to_fahrenheit(c):
    pass

def fahrenheit_to_celsius(f):
    pass

MODULE_VERSION = "1.0"
'''

# with open("temperature_utils.py", "w") as f:
#     f.write(module_code)

today_date = datetime.date.today().strftime("%d-%m-20%y")
print(f"Temperature Report - {today_date}")
celsius_temperatures = [random.randrange(15, 41) for temp in range(5)]
print(f"Celsius: {celsius_temperatures}")

fahrenheit_temp = list(map(celsius_to_fahrenheit, celsius_temperatures))
print(f"Fahrenheit: {fahrenheit_temp}")

module_version = MODULE_VERSION
print(f"Module version: {module_version}")