#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares=0
impares=0
positivos=0
negativos=0

for i in range(10):
    num = int(input(f"Ingrese el número entero {i+1}/{10}: "))
    
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
        
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"numeros pares:{pares}\nnumeros impares:{impares}\nnumeros positivos:{positivos}\nnumeros negativos:{negativos}")