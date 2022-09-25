#1) Crear 5 variables con 5 notas numéricas y realizar la media aritmética. Mostrar el resultado final con un mensaje como este: "La nota media es 6.0"
nota1=6.1
nota2=3.8
nota3=9.4
nota4=7.4
nota5=5.3

media=(nota1+nota2+nota3+nota4+nota5)/5
print("La nota media es",media)

#2) Busca en la documentación la forma correcta de redondear el siguiente resultado a tan solo 2 decimales: operacion = (365 / 12) * 14.7
operacion=(365 /12) * 14.7
print("{:.2f}".format(operacion))

#3) Crea dos variables que almacenen 2 strings (username y password). Realizar las siguientes comprobaciones utilizando operadores lógicos:

username=input("Introduce el nombre de usuario: ")
password=input("Introduce la contraseña: ")
#Que la longitud de username sea mayor o igual que tres y menor que diez
print("Username:", len(username) >= 3 and len(username) < 10)
#Que la password sea igual a "Tokio" o que sea igual a "Python".
print("Password:", password=="Tokio" or password=="Python")
#La salida por pantalla tiene que ser:
#Username: True o False (según se haya evaluado)
#Password: True o False (según se haya evaluado)


#4) Practiquemos con los operadores de asignación (=, +=, -=, etc.):
#Crea dos variables y asignales los números que quieras
num1=1
num2=2
#Incrementale a num1 su valor en 1
num1+=1
print(num1)
#Decrementale a num2 su valor en 2
num2-=2
print(num2)
#Multiplica num1 por 3 y actualiza su valor
num1*=3
print(num1)
#Dividide num2 por 2 y actualiza su valor
num2/=2
print(num2)
#Muestra los resultados