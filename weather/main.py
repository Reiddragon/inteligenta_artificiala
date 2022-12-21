import requests
from os import environ


API_KEY = environ['API_KEY']
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


def init_file():
    pass


def init_file():
    pass


def main():
    city = input('City Name: ')
    request_url = f'{BASE_URL}?appid={API_KEY}&q={city}&units=metric'
    response = requests.get(request_url)

    if response.status_code != 200:
        print(f'There was a problem, HTTP response was {response.status_code}')
        raise Exception('BadReturnCode')

    data = response.json()

    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'], 2)
    wind = f'{data["wind"]["speed"]}m/s {["N", "NE", "E", "SE", "S", "SW", "W", "NW"][int(((data["wind"]["deg"] + 22.5) % 360) // 45)]}'

    print(f'Weather: {weather}\nTemperatura: {temperature}°C\nWind = {wind}\n')


if __name__ == '__main__':
    main()
