from pyowm import OWM

city = input("In which city do you want to find out the weather?\n")
owm = OWM('37ace9ba0da02f3957cb68cae063f86b')  # free OWM API key
mgr = owm.weather_manager()


class WeatherInCity():

    def __init__(self, town):
        observation = mgr.weather_at_place(town)
        self.w = observation.weather
        status = self.w.detailed_status

        print(status + " in " + town)

    def rain(self):
        raining = (list(self.w.rain))

        if not raining:
            print("It's not raining")
        else:
            print("It's raining,you need take an umbrella")

        return raining

    def wind(self):
        wn = self.w.wind()
        speed_wind = wn['speed']

        return speed_wind

    def temperature(self):

        t = self.w.temperature('celsius')['temp']

        return t


weather = WeatherInCity(city)

(weather.rain())
print("In " + city + ", the temperature is " + str(weather.temperature()) + " ℃")
print("Speed wind in " + city + " is " + str(weather.wind()) + " km/h\n")


input('Press ENTER to exit')
