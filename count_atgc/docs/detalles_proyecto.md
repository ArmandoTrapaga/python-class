# Nombre del Proyecto

Fecha:

**Participantes**:

- Armando Trapaga : aggonzal@lcg.unam.mx

## Descripción del Problema

Cuenta las ocurrencias de los símbolos "A", "G", "C", "T" de una cadena de ADN que lee atreves de  un archivo 


## Especificación de Requisitos

Requisitos funcionales

- Requisito 1: El programa necesita de un archivo que contenga la secuencia de ACGT a contar

Requisitos no funcionales

- Requisito 1
- Requisito 2
- Requisito n



## Análisis y Diseño


```
# Logica del codigo

import argparse

#Asignamos los argumentos pasados por la terminal al entorno de python
parser = argparse.ArgumentParser()
parser.add_argument("archivo", type=argparse.FileType('r'), help="El archivo que se desea analizar")
#n se establece como un argumento opcional
parser.add_argument("-n", "--nucleotidos", type=str, nargs="+", default=["A", "T", "C", "G"], help="Ingresa que nucleotidos deseas conocer su incidencia, si no pones nada se te dara el de todos")

#Funcion que calcula el total de ocurrencias de A,C,G,T

def contar_atcg(archivo):

#Se crea un diccionario donde se guardara el total de ocurrencias de cada caso

  num_bases = {'A': 0, 'T': 0, 'C': 0, 'G': 0} 
  
  #Caso general
  try:
    with open(archivo, 'r') as txt:
    #Se lee el archivo, elimina los espacios y vuelve mayusculas a las letras
      adn = txt.read().replace(' ', '').upper()
      #Caso de excepcion por si el archivo dado esta vacio
      if not adn:
        raise ValueError("sorry, this file is empty")
      
      #Se itera en la variable adn 
      for base in adn:
      #Caso excepcion por si el archivo contiene un caracter invalido en la secuencia
        if base not in 'ATCG':
          raise ValueError(f"Sequence contains '{base}', it is invalid character")
        num_bases[base] += 1
      
      #Se imprime el total de ocurrencias
      for base, numero in num_bases.items():
        print(f"{base}: {numero}")
  
  except IOError:
  #Caso excepcion
    print("sorry, couldn't find the file")

#Se llama a la funcion con un archivo de tipo texto como argumento
contar_atcg('adn.txt')

```

Formato de los archivos input que recibe el programa, asi como el formato de los archivos output o mensajes a imprimir en pantalla
Archivos:
-Tipo texto
Output:
-Se imprime el total de ocurrencias

#### Caso de uso: Contar el total de ocurrencias de A,T,G y C

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-------+-------+
         |   Programa    |
         |Cuenta el total|
         |   de A,T,C,G  |
         |Regresa impreso|
         | el total de   |
         |     bases     |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona un archivo de entrada...
- **Flujo principal**:

	1. El usuario carga un archivo en el entorno de python
	2. El usuario llama a la funcion 
	
- **Flujos alternativos**:
	- Si no se proporciona un archivo entonces el programa debera imprimir 'Error: Archivo inexistente u no apropiado'
	- Si el formato del archivo no es correcto, imprimir a pantalla mensaje de error el mismo error
                

