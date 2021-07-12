from pyowm import OWM

city = input("In which city do you want to find out the weather?")
owm = OWM('37ace9ba0da02f3957cb68cae063f86b')  # free OWM API key
mgr = owm.weather_manager()


def foo(town):
    observation = mgr.weather_at_place(town)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']

    return temperature


print(foo(city))


