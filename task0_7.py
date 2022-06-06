def celcius_to_farenheit(celcius):
    farenheit = (celcius * 9/5) + 32
    return farenheit
   
def farenheit_to_celcius(farenheit):
    celcius = (farenheit - 32) * 5/9
    return celcius

print(celcius_to_farenheit(25))
print(farenheit_to_celcius(77))  
