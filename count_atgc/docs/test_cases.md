# Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python desarrollado para contar el total de 
ocurrencias de las bases A, T, C, G de un archivo de texto

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para imprimir el total de ocurrencias de las bases A,T,C,G de un archivo texto

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.
    
    
### Caso de prueba 1: Comprobacion de un correcto conteo 

- Descripción: Verificar que el script realice de manera adecuada el conteo de las bases, en el archivo proporcionado

- Datos de entrada: Archivo de texto, Prueba.txt en la carpeta src junto al templete del programa:

´´´bash
    python count_atcg.py ../docs/Prueba.txt

´´´
- Resultado esperado:
A: 1
T: 2
C: 3
G: 4 

### Caso de prueba 2: Comprobar el argumento opcional 

- Descripción: Verificar que el script pueda regresar solo los nucleotidos que el usuario desee conocer 
- Datos de entrada: Archivo de texto, Prueba.txt en la carpeta docs:
´´´bash
    python count_atcg.py ../docs/Prueba.txt -n A T
´´´
- Resultado esperado: 
A:1
T:2

### Caso de prueba 3: En caso de que el archivo propocionado no exista
- Descripcion: Revisar si el archivo no existe, a lo cual se imprimira el mensaje de error
- Datos de entrada: Dejar vacio la entrada que pide el archivo:

´´´bash
    python count_atcg.py 
´´´
- Resultado esperado:
sorry, couldn't find the file

### Caso de prueba 4: En caso de que el archivo este vacio
- Descripcion: Revisar si el archivo esta vacio, a lo cual se imprimira el mensaje de error
- Datos de entrada: Archivo de texto, Prueba_error_Vacio.txt en la carpeta docs:

´´´bash
    python count_atcg.py ../docs/Prueba_error_Vacio.txt 
´´´
- Resultado esperado:
sorry, this file is empty


### Caso de prueba 5: En caso de que el archivo contenga un caracter invalido
- Descripcion: Revisar si el archivo tiene algun caracter invalido en si contenido, a lo cual se imprimira el mensaje de error
- Datos de entrada: Archivo de texto, Prueba_error_secuencia.txt en la carpeta docs:

´´´bash
    python count_atcg.py ../docs/Prueba_error_secuencia,txt 
´´´

- Resultado esperado:
Sequence contains {base}, it is invalid character
