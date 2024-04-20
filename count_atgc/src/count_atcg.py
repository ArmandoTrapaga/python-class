'''
NAME

Conteo de ATCG

VERSION
        
1.5

AUTHOR

Armando Gael Gonzalez Trapaga       

DESCRIPTION

Cuenta las ocurrencias de los símbolos "A", "T", "C", "G" de una cadena de ADN que lee a través de un archivo.

CATEGORY

Biología Computacional

USAGE

    % python contar_atcg.py
    

ARGUMENTS

- archivo: La ruta del archivo que contiene la cadena de ADN a analizar.

METHOD

1. contar_atcg(archivo)
   Esta función toma un archivo de texto que contiene una cadena de ADN y cuenta las ocurrencias de los símbolos "A", "T", "C", "G" en la cadena. Si el archivo no existe o no es adecuado, imprime un mensaje de error.

SEE ALSO
'''




# ===========================================================================
# =                            imports
import argparse 
# ===========================================================================





# ===========================================================================
# =                            Command Line Options
# ===========================================================================






# ===========================================================================
# =                            functions

#Asignamos los argumentos pasados por la terminal al entorno de python
parser = argparse.ArgumentParser()
parser.add_argument("archivo", type=argparse.FileType('r'), help="El archivo que se desea analizar")
#n se establece como un argumento opcional
parser.add_argument("-n", "--nucleotidos", type=str, nargs="+", default=["A", "T", "C", "G"], help="Ingresa que nucleotidos deseas conocer su incidencia, si no pones nada se te dara el de todos")

#los argumentos de la funcion es una archivo de texto y las bases que se desea conocer la ocurrencia
def contar_atcg(archivo, n):
  #Se crea un diccionario donde se guardara el total de ocurrencias de cada caso
  num_bases = {'A': 0, 'T': 0, 'C': 0, 'G': 0} 
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
      #Se imprime el total de ocurrencias de las bases deseadas
      for base in n:
        print(f"{base}: {num_bases.get(base, 0)}")
  except IOError:
    print("sorry, couldn't find the file")
# ===========================================================================





# ===========================================================================
# =                            main
args = parser.parse_args()
contar_atcg(args.archivo.name, args.nucleotidos)
# ===========================================================================


# step 1.


# step 2.


# step 3.



