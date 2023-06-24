'''
Un NIF, es un NÚMERO DE IDENTIFICACIÓN FISCAL (NIF) otorgado por la Unión Europea a los ciudadanos mayores de 15
años. Es el equivalente o similar al Rut o número de identificación chileno.
Este NIF tiene ciertos beneficios para quien lo obtiene.

1- Grabar
2- Buscar
3- Imprimir certificados
4- Salir

1. Diseñe un menú con las opciones para acceder a cada función requerida.

2. Cree las funciones solicitadas por cada requerimiento

3. Considere el ingreso de datos y el despliegue de información.

'''
versionPrograma = "3.11.2"

print("Bienvenidos al Registro de Ciudadanos de la Unión Europea\n")
print()
print("Menú de Registro\n")
print()
print("1- Grabar")
print("2- Buscar")
print("3- Imprimir Certificados")
print("4- Salir")
print()

opcion1 = int(input("Selecciones una opción del menú: "))


# #************************************
# def validarNif(NIF):
#     if NIF < 8:
#         print("NIF invalido!, porfavor ingrese un NIF valido.")
#         return False
#     else:
#         return True
# #************************************
# def validarNombre(nombre):
#     if (len(nombre<8)):
#         print("El nombre no supera los 8 carácteres, porfavor ingresar un nombre valido.")
#         return False
#     else:
#         return True
# #************************************
# def validarEdad(edad):
#     if edad < 0:
#         print("Edad Ingresada es menor a '0', porfavor ingresar una edad valida.")
#         return False
#     else:
#         return True
# #************************************
# '''
# Menú
# '''

while opcion1 == 1:
    NIF = input("Ingrese su Numero de Identificación Fiscal NIF: ")
    if NIF < 8:
        print("NIF invalido!, porfavor ingrese un NIF valido.")
    else:
        print(NIF,"Ingresado correctamente.")
    nombre = input("Ingrese su nombre completo: ")

    if (len(nombre < 8)):
         print("El nombre no supera los 8 carácteres, porfavor ingresar un nombre valido.")
    else:
        print(nombre,"Ingresado correctamente.")
    edad = int(input("Ingrese su edad: "))
    if edad < 0:
        print("Edad Ingresada es menor a '0', porfavor ingresar una edad valida.")
    else:
        print(edad,"Ingresada correctamente.")

while opcion1 == 2:
    Buscar = input("Ingrese el NIF que desee bucar: ")
    

while opcion1 == 3:
    def certificado(NIF,nombe,edad):
        certi = certificado()
        return certi

while opcion1 == 4:
    print("Gracias por utilizar el Registro de Ciudadanos de la Unión Europea",nombre)

