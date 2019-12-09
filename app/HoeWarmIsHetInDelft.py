import sys
import requests

url = "https://www.weerindelft.nl/clientraw.txt"

try:
    response = requests.get(url)
    data = response.text.split(" ")
except requests.exceptions.HTTPError as e:
    print('Error code: ', e.code)
except requests.exceptions.Timeout:
    print('Timeout')
except requests.exceptions.RequestException as e:
    print('Exception: ', e)
    sys.exit(1)
# get data
try:
    print(round(float(data[4])), "degrees Celsius")
except TypeError:
    print("No weather data")
except ValueError:
    print("The value is wrong")
except NameError:
    print("There is no data")
