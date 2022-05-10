import datetime as dt
import requests

class Weather:

    def __init__(self, city) -> None:
        """
        Sets up the structure for retrieving
        the weather data of the given city
        """
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "f737a22e7c92a28c78c8296f9fe066d6"
        self.__url = BASE_URL + "appid=" + API_KEY + "&q=" + city
        self.__response = requests.get(self.__url).json()

    def result_check(self):
        if str(self.__response.items())[14:17] == 'cod':
            return f'Invalid'
        else:
            return f'Valid'

    def temp(self) -> str:
        """
        Gives the temperatures of the
        area specified by the user
        :return: The temperature status
        """
        cel = self.__response['main']['temp'] - 273.15
        fah = cel * (9//5) + 32
        return f'Kelvin: {self.__response["main"]["temp"]:.0f}\nCelsius: {cel:.0f}\n' \
               f'Fahrenheit: {fah:.0f}'

    def wind(self) -> str:
        """
        Gives the wind speed of the area
        specified by the user
        :return:
        """
        describe = ''
        if self.__response["wind"]["speed"] < 1:
            describe = 'Calm'
        elif self.__response["wind"]["speed"] < 18:
            describe = 'Light Breeze'
        elif self.__response["wind"]["speed"] < 47:
            describe = 'Moderate Gale'
        elif self.__response["wind"]["speed"] < 74:
            describe = 'Storm'
        else:
            describe = 'Hurricane'
        return f'Wind Speed: {self.__response["wind"]["speed"]:.0f} mph\nDescription: {describe}'

    def humid(self) -> str:
        """
        Gives the humidity of the area
        specified by the user
        :return: Humidity status
        """
        describe = ''
        if self.__response['main']['humidity'] < 45:
            describe = 'Comfortable'
        elif self.__response['main']['humidity'] < 66:
            describe = "Muggy"
        else:
            describe = "Oppressive"
        return f'Humidity: {self.__response["main"]["humidity"]}%\nVision: {describe}'

    def suntime(self) -> str:
        """
        Gives the sunrise and sunset times
        of the area specified by the user
        :return: Sunrise and sunset times
        """

        sunrise = dt.datetime.utcfromtimestamp(self.__response['sys']['sunrise'] + self.__response['timezone'])
        sunset_mil = dt.datetime.utcfromtimestamp(self.__response['sys']['sunset'] + self.__response['timezone'])
        return f'Sunrise: {sunrise}\nSunset: {sunset_mil}'
