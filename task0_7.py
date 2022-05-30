celcius = 25
def celcius_to_farenheit(celcius):
    farenheit = (celcius * 9/5) + 32
    return farenheit
   
print(celcius_to_farenheit(celcius))


farenheit = 77
def farenheit_to_celcius(farenheit):
    celcius = (farenheit - 32) * 5/9
    return celcius

print(farenheit_to_celcius(farenheit))  
