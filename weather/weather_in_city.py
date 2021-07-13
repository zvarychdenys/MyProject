from pyowm import OWM

city = input("In which city do you want to find out the weather?\n")
owm = OWM('37ace9ba0da02f3957cb68cae063f86b')  # free OWM API key
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather


def wind(town):
    wn = w.wind()
    speed_wind = wn['speed']

    return speed_wind


def temperature(town):

    t = w.temperature('celsius')['temp']

    return t


print("In " + city + ", the temperature is " + str(temperature(city)) + " ℃")
print("Speed wind in " + city + " is " + str(wind(city)) + " km/h")
