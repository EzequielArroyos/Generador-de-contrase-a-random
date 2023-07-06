# Un generador de contraseña simple

print("\t\tGenerador de Contraseña Random")

password_ingresado = int(input("Agrega una contraseña con varios caracteres numericos:\n"))


def Contraseña_random(num):
    password = num 
    abc = "abcdefghijklmnopqrstuvwxyz#&$°"
    numero_entero = str(num)
    num = int(numero_entero[2])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{abc[c1]}{abc[c2]}{abc[c3]}{num*2}{c3}"
    return contraseña,password
    
nueva_contraseña, contraseña = Contraseña_random(password_ingresado)

print(f"Contraseña nueva es: {nueva_contraseña}")
print(f"Contraseña agregada: {contraseña}")