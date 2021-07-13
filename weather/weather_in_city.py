from pyowm import OWM

city = input("In which city do you want to find out the weather?\n")
owm = OWM('37ace9ba0da02f3957cb68cae063f86b')  # free OWM API key
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather


def status(town):

   print(w.detailed_status)


def rain(town):

    arr = (list(w.rain))

    if not arr:
        print("It's not raining")
    else:
        print("It's raining,you can take an umbrella")

    return arr


def wind(town):
    wn = w.wind()
    speed_wind = wn['speed']

    return speed_wind


def temperature(town):

    t = w.temperature('celsius')['temp']

    return t


print("In " + city + ", the temperature is " + str(temperature(city)) + " ℃")
print("Speed wind in " + city + " is " + str(wind(city)) + " km/h")

rain(city)
status(city)
