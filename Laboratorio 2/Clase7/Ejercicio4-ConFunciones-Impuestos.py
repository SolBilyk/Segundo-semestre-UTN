# Ejercicio 4: Calculadora de impuestos
# crear una guncion para calcular el total de un pago incluyendo
# un impuesto aplicado. (IVA)
# Formula: pago_total= pago_sin_impuesto+pago_sin_impuesto*(impuesto/100)
# proporciones el pago sin impuesto: 1000
# proporciones el monto del impuesto: 21%
# pago con impuesto: ????

def pagoTotal(pagoSinImpuesto,impuesto):
    pagoTotal=pagoSinImpuesto+pagoSinImpuesto*(impuesto/100)
    return pagoTotal
pagoSinImpuesto=float(input("Ingrese el pago sin impuesto: "))
impuesto=int(input("ingrese el valor del impuesto a aplicar: "))
pagoConImpuesto=pagoTotal(pagoSinImpuesto,impuesto)
print(f"El pago con impuesto es {pagoConImpuesto}")