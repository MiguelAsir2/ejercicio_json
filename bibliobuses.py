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
  
