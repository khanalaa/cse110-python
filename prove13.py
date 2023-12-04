print("--------Wind Chill calculator--------\n")

temp = float(input("What is the temperature? "))
f_c = input("Fahrenheit or Celsius (F/C)?").lower()
print()

def wind_chill(t):
    v = 5
    while v < 65: 
        chill = 35.74 + (0.6215 * t) - (35.75 *(v ** 0.16)) + (0.4275 * t * (v ** 0.16))
        print(f"At temperature {t}F, and wind speed {v} mph, the windchill is: {chill:.2f}F")
        v += 5
        

def tempconverter_fah(x):
    cel = x * (9/5) + 32
    return cel


if f_c == "c":
    wind_chill(tempconverter_fah(temp))
else:
    wind_chill(temp)


    
    
    