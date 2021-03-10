import pandas

'''
Clase Codes para obtener códigos IATA por ciudad
'''
class Codes:

    '''
    Constructor de la clase. Inicializa un diccionario con los códigos IATA para más
    de 57000 ciudades
    :param codes: Un archivo csv con los códigos IATA por ciudad
    '''
    def __init__(self, codes):
        IATA_CODES = pandas.read_csv(codes, dtype={'municipality': str, 'iata_code': str})
        self._CODES = {}
        for i in range(57420):
            self._CODES[IATA_CODES['iata_code'][i]] = IATA_CODES['municipality'][i]

    '''
    Método para obtener un diccionario con los códigos IATA por su ciudad
    :return: Un diccionario con los códigos IATA y la respectiva ciudad
    '''
    def get_codes(self):
        return self._CODES
