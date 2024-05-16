"""
incidencia_codones.py: Módulo para calcular la incidencia de codones en una secuencia de ADN.

Este módulo proporciona una función para calcular la incidencia de codones en una secuencia de ADN dada.

Funciones:
- calculate_codon_incidence(sequence, frame=3): Calcula la incidencia de codones en la secuencia de ADN.
"""

def calculate_codon_incidence(sequence, frame=3):
    """
    Calcula la incidencia de codones en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN a analizar.
        frame (int): El marco de lectura a utilizar para la búsqueda de codones. Por defecto es 3.

    Returns:
        dict: Un diccionario que contiene la incidencia de cada codón encontrado en la secuencia.

    Raises:
        ValueError: Si la secuencia está vacía.
    """

    # Validación básica de la secuencia
    if not sequence:
        raise ValueError("La secuencia proporcionada está vacía.")

    sequence = sequence.upper().replace(' ', '')
    codon_incidence = {}

    for bases in range(frame, len(sequence), frame):
        codon = sequence[bases:bases+frame]
        if len(codon) == frame:
            if codon not in codon_incidence:
                codon_incidence[codon] = 0
            codon_incidence[codon] += 1

    return codon_incidence

if __name__ == "__main__":
    # Prueba de funcionalidad.
    test_sequence = "ATCATCATCATC"
    print("Incidencia de codones en la secuencia de prueba:")
    print(calculate_codon_incidence(test_sequence))
