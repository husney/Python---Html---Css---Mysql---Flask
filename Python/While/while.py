
i = 0 # iterador

#while i <= 5: # condición   
#   if(i == 3):
#        i += 1
#        continue
#    else:
#        print(i)  
#    i += 1
    

# break rompe el ciclo
# continue salta una iteración 


edad = int(input("Por favor ingrese su edad:... "))

while edad <0 or edad > 100:
    print("Error edad no valida")
    edad = (int(input("Por favor ingrese su edad: ...")))
else:
    print("Edad valida")