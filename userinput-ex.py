def weather_condition(temp):
    if temp > 6:
        return "warm"
    else:
        return "cold"

user_input = float(input("Enter Temperature : "))
print (weather_condition(user_input))