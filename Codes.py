import pandas


class Codes:

    #Inicializamos un objeto Codes leyendo el csv que pase como parámetro y llenamos su diccionario
    def __init__(self, codes):
        IATA_CODES = pandas.read_csv(codes, dtype={'municipality': str, 'iata_code': str})
        self._CODES = {}
        for i in range(57420):
            self._CODES[IATA_CODES['iata_code'][i]] = IATA_CODES['municipality'][i]

    #Regresa la propiedad CODES la cual es el diccionario con codigos IATA y la respectiva ciudad
    def get_codes(self):
        return self._CODES
