print ("Convertidor de Grados °C a grados °F - CelToFah \nJavier Guaregua - 2018")
print ("")
print ("1 °C equivale a 33.8 °F")
print("")




while True:
    cel = float(input("Escriba aqui la cantidad\nNota: Solo numeros, de lo contrario el programa fallara\n"))
    print(cel,"°C son", cel * -17.222, "°F\n")
    #print(f"{cel} °C son aproximadamente {round(cel * -17.222)} °F\n")



#Posible uso futuro
    #celtofah = cel * 33.8
    #print("Son aproximadamente" celtofah )