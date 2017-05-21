#!/usr/local/bin/python
# -*- coding: latin-1 -*-

# Este programa hace pings a un servidor, ping es un comando envia paquetes de
# datos a un servodor para verificar si hay conexionsel.
# De acuerdo a la respuesta, el programa lee y modifica el texto contenido en unos
# archivos, creando nuevos archivos con el texto
# resultante de estos procesos

import os
import glob
import random
import time

# tiempo de pausa entre pings, en segundos
pausa = 10
#carpeta con los archivos a procesar, el / es necesario
directiorio = "textos/"
#directiorio mas extension es la ruta del archivos
# *.txt quiere decir seleccionar todo archivo con extension .txt
ruta = directiorio + "*.txt"
#servidor al cual hacerle ping
servidor = "www.google.com"


#proceso infinito
while True:
    # listar archivos de la ruta
    archivos = glob.glob(ruta)
    # ordenar los archivos por fecha de modificacion
    archivos.sort(key=os.path.getmtime)
    # numero de archivos en la carpeta
    num_archivos = len(archivos)
    # el primer archivo o la fuente de texto para construir
    # los otros archivos
    primer_archivo = archivos[0]
    # el ultimo archivo de la lista, el que se va a procesar
    archivo = archivos[num_archivos - 1]
    # comando que hace ping·
    # si hay conexion con el servidor, response es igual a 0
    # si no, response es igual a 1
    response = os.system("ping -c 1 " + servidor)
    # evaluamos el valor de response en un if
    if response == 0:
        # Si hay conexion con el servidor hacemos lo siguiente:
        print("Network Active")
        # abrimos el primer archivo y extraemos sus lineas
        with open(primer_archivo, 'r') as primer_archivo:
            lineas = primer_archivo.read().splitlines(True)
        # abrimos el ultimo archivo
        with open(archivo, 'r') as archivo:
            # nuevas lineas representa el texto del nuevo archivo
            nuevas_lineas = archivo.read().splitlines(True)
            # seleccionamos una linea aleatoria del primer archivo
            linea_aleatoria = random.choice(lineas)
            # la agregamos a las nuevas lineas
            nuevas_lineas.extend(linea_aleatoria)
            # creamos la ruta del nuevo archivo
            # usando el numero del ultimo archivo + 1
            nueva_ruta = directiorio + str(num_archivos) + ".txt"
            # creamos el nuevo archivo y lo escribimos con las nuevas lineas
        with open(nueva_ruta, 'w') as nuevo_archivo:
            nuevo_archivo.writelines(nuevas_lineas)


    else:
        # si no hay conexion
        print("Network Error")
        # abrimos el ultimo archiov
        with open(archivo, 'r') as archivo:
            # extraemos las lineas del archivo
            lineas = archivo.read().splitlines(True)
            # creamos la ruta del nuevo archivo
            nueva_ruta = directiorio + str(num_archivos) + ".txt"
            # creamos el nuevo archivo
        with open(nueva_ruta, 'w') as nuevo_archivo:
            # en el nuevo archivo escribimos las lineas
            # del ultimo archivo, excluyendo la ultima
            nuevo_archivo.writelines(lineas[1:])
    # hacemos una pausa, por el tiempo determinado en
    # la varible pausa
    time.sleep( pausa )
