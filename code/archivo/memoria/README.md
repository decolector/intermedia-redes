# Memoria

Este programa hace pings a un servidor, ping es un comando envia paquetes de datos a un servodor para verificar si hay conexionsel.
De acuerdo a la respuesta, el programa lee y modifica el texto contenido en unos archivos, creando nuevos archivos con el texto resultante de estos procesos

## Uso

Antes de ejecutar la primera vez, hay que incluir un archivo de texto plano en la carpeta `textos/` con el nombre `0.txt`.   Este será el archivo inicial a procesar

Abrir una terminal y navegar al direciorio `memoria`.

```bash
cd /path/a/memoria
```
Ejecutar con python

```bash
python memoria.py
```

Para interrumpir el programa usar la combinaciónde teclas:
```
Ctrl+ c
```

Si se obtiene un error de tipo

```bash
Permission denied
```

Dar permisos de ejecución a memoria.py

```bash
chmod +x memoria.py
```
