def celcius_to_farenheit(celcius):
    farenheit = (celcius * 9/5) + 32
    return farenheit
   
def farenheit_to_celcius(farenheit):
    celcius = (farenheit - 32) * 5/9
    return celcius

celcius = 25
farenheit = 77
print(celcius_to_farenheit(celcius))
print(farenheit_to_celcius(farenheit))  
