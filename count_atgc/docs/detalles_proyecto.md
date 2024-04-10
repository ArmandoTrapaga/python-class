# Nombre del Proyecto

Fecha:

**Participantes**:

- Armando Trapaga : aggonzal@lcg.unam.mx

## Descripción del Problema

Cuenta las ocurrencias de los símbolos "A", "G", "C", "T" de una cadena de ADN que lee atreves de  un archivo 


## Especificación de Requisitos

Requisitos funcionales

- Requisito 1: El programa necesita de un archivo que contenga la secuencia de ACGT a contar
- The program should accept a path to a DNA sequence file as a command line argument.
- The nucleotides to be counted should be passed as an optional command line argument.
- If the optional nucleotide argument is omitted, the program should default to counting all 4 nucleotides: 'A', 'C', 'G', and 'T'.

Requisitos no funcionales

- The program will be developed in the Python programming language to ensure widespread compatibility and ease of use.
- Reading of command line arguments should be implemented using the argparse library for Python to allow for flexible and user-friendly command-line interfaces.
- ...



## Análisis y Diseño


```
# Logica del codigo

#Funcion que calcula el total de ocurrencias de A,C,G,T

def contar_atcg(archivo):

#Se crea un diccionario donde se guardara el total de ocurrencias de cada caso

  num_bases = {'A': 0, 'T': 0, 'C': 0, 'G': 0} 
  
  #Caso general
  try:
    with open(archivo, 'r') as txt:
    #Se lee el archivo, elimina los espacios y vuelve mayusculas a las letras
      adn = txt.read().replace(' ', '').upper()
      
      #Se itera en la variable adn 
      for base in adn:
        num_bases[base] += 1
      
      #Se imprime el total de ocurrencias
      for base, numero in num_bases.items():
        print(f"{base}: {numero}")
  
  except:
  #Caso excepcion
    print('Error: Archivo no existente u no apropiado')

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
                

