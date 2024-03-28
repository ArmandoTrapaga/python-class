'''
NAME

Conteo de atcg

VERSION
        
1.0

AUTHOR

Armando Gael Gonzalez Trapaga        

DESCRIPTION

Cuenta las ocurrencias de los símbolos "A", "G", "C", "T" de una cadena de ADN que lee atreves de  un archivo 

CATEGORY
        

USAGE

    % python programName
    

ARGUMENTS


METHOD


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



