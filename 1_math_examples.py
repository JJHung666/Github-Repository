# Date: 9/13/2018
# Descriptions: This program uses what was learned in class
# source: none

print("to find the wind chill")
T = float(input("please enter temperature in Fahrenheit "))
V = float(input("please enter wind speed "))
W = 35.74 + 0.6215*T + (0.4275*T - 35.75)*V**0.16
print("The Wind Speed is:",str(W))