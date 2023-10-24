# Ejercicio 5: conversor de temperaturas
# Realizar dos funciones para convertir de grados celcius a farenhait
# y visceversa

#C° a F°
def celsiusFarenheit(celcius):
    return celcius * 9 / 5 + 32

#F° a C°
def farenheitCelcius(farenheit):
    return (farenheit - 32) * 5 / 9

celcius=float(input("Ingrese temperatura en celcius: "))
res=celsiusFarenheit(celcius)
print(f"La temperatura de {celcius}C° equivale a {res}°F")

farenheit=float(input("Ingrese temperatura en Farenheit: "))
res2=farenheitCelcius(farenheit)
print(f"La temperatura de {celcius}F° equivale a {res2}°C")