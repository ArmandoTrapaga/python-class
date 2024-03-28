# Conteo de ATCG

Este es un script de Python diseñado para contar las ocurrencias de los símbolos "A", "G", "C", "T" en una cadena de ADN que se lee desde un archivo..

## Uso

El script se puede usar de la siguiente manera:

´´´bash
    python contar_atcg.py <archivo>
´´´
Donde <archivo> es la ruta del archivo que contiene la cadena de ADN a analizar.

## Salida

El script imprimirá el número de ocurrencias de cada símbolo "A", "T", "C" y "G" en la cadena de ADN.

## Control de errores

Si el archivo proporcionado no existe o no se puede abrir, el script imprimirá "Error: Archivo no encontrado.". Del mismo modo, si ocurre un error al leer el archivo o si el archivo no contiene una cadena de ADN adecuada, el script imprimirá "Error: Archivo no apropiado."

## Pruebas

El script incluye un conjunto de pruebas unitarias. Puede ejecutar estas pruebas con:

```
python -m unittest contar_atcg.py
```

## Datos

El script está diseñado para operar con archivos de texto que contienen una cadena de ADN.

## Metadatos y documentación

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte la documentación del código fuente.

## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia APACHE. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [información de citación].

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: aggonzal@lcg.unam.mx
