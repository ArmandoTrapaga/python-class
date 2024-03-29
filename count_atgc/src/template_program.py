'''
NAME

Conteo de ATCG

VERSION
        
1.0

AUTHOR

[Su nombre aquí]       

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
# ===========================================================================





# ===========================================================================
# =                            Command Line Options
# ===========================================================================






# ===========================================================================
# =                            functions


def contar_atcg(archivo):
  num_bases = {'A': 0, 'T': 0, 'C': 0, 'G': 0} 
  try:
    with open(archivo, 'r') as txt:
      adn = txt.read().replace(' ', '').upper()
      for base in adn:
        num_bases[base] += 1
      for base, numero in num_bases.items():
        print(f"{base}: {numero}")
  except:
    print('Error: Archivo no existente u no apropiado')

# ===========================================================================





# ===========================================================================
# =                            main
contar_atcg('adn.txt')
# ===========================================================================


# step 1.


# step 2.


# step 3.



