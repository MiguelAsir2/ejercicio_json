import json
with open ('bibliobuses.json','r') as fichero:
    doc=json.load(fichero)
autobuses=[]
cod_postales=[]
calle=[]
descripcion=[]
cont_biblio=0
cont_bus=0
servicios=[]
for i in doc["@graph"]:
    autobuses.append(i["title"])
    cod_postales.append(i["address"]["postal-code"])
    calle.append(i["address"]["street-address"])
    descripcion.append(i["organization"]["schedule"])
    servicios.append(i["organization"]["services"])
#MENU
while True:
    print()
    print(''' 1. Lista los autobuses y bibliotecas
    2. Cuenta cuantos bibliobuses y bibliotecas hay
    3. Introduce nombre de la biblioteca y muestra la dirección
    4. Introduce nombre de una biblioteca y muetra los horarios
    5. Introduce nombre de biblioteca y muestra servicios y características
    0. Salir''')
    opcion=int(input("Selecciona una opcion en el menú: "))
    print()
    if opcion==1:
        print("LISTA DE AUTOBUSES:")
        print()
        for i in autobuses[:7]:
            print(i)
        print()
        print("LISTA DE BIBLIOTECAS:")
        print()
        bibliotecas=autobuses[7:-2]
        for i in bibliotecas:
            print (i)
    elif opcion==2:
        cont=0
        print("Número de autobuses: ",end="")
        for i in autobuses[:7]:
            cont+=1
        print(cont)
        bibliotecas=autobuses[7:-2]
        cont=0
        print("El número de bibliotecas es: ",end="")
        for i in bibliotecas:
            cont+=1
        print (cont)
    elif opcion==3:
        biblioteca=input("Introduce el nombre de una biblioteca: ")
        print()
        if biblioteca in autobuses[7:-2]:
            print("%s se encuentra en ----> "%(biblioteca),end="")
            for i,j in zip(autobuses,calle):
                if i == biblioteca:
                    print(j)
        else:
            print("Esta biblioteca no existe")
    elif opcion==4:
         biblioteca=input("Introduce el nombre de una biblioteca: ")
         print()
         if biblioteca in autobuses[7:-2]:
            print("%s tiene los siguientes horarios:"%(biblioteca))
            print()
            for i,j in zip(autobuses,descripcion):
                if i == biblioteca:
                    print(j)
         else:
            print("Esta biblioteca no existe")
    elif opcion==5:
         biblioteca=input("Introduce el nombre de una biblioteca: ")
         print()
         if biblioteca in autobuses[7:-2]:
            print("%s tiene los siguientes servicios y caracteristicas:"%(biblioteca))
            print()
            for i,j in zip(autobuses,servicios):
                if i == biblioteca:
                    print(j)
         else:
            print("Esta biblioteca no existe")
    if opcion==0:
        break