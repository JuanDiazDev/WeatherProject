import pyowm

'''
Clase City para manejar la información del clima de una ciudad
'''
class City:
    '''
    diccionario para guardar el reporte del clima por ciudad
    '''
    weather_info = {}

    '''
    Constructor de la clase.
    :param name: El nombre de la instancia
    '''
    def __init__(self, name):
        self._name = name

    '''
    Cambia el nombre a una instancia de City
    :param: El nuevo nombre para la instancia
    '''
    def set_name(self, name):
        self._name = name

    '''
    Regresa el nombre de una instancia de City
    :return: El nombre de una instancia de City
    '''
    def get_name(self):
        return self._name

    '''
    Método para darle el formato que queremos al reporte del clima
    :param temperature: Un diccionario con información sobre la temperatura
    :param humidity: Nivel de humedad
    :param status: El estado general del clima 
    :return: Una cadena con el reporte del clima
    '''
    @staticmethod
    def format_weather(temperature, humidity, status):
        max_temperature = temperature['temp_max']
        min_temperature = temperature['temp_min']
        return f'Weather: {status}, Temperature: Max: {max_temperature} Min: {min_temperature}, Humidity: {humidity}'

    '''
    Solicitamos el reporte del clima al API wrapper pyowm
    :param name: Nombre de la ciudad para la que solicitaremos la info del clima
    :return: True si hay un error
    :except NotFoundError, TimeoutError
    '''
    @staticmethod
    def request_weather(report, name):
        owm = pyowm.OWM('4f35f6733973b80abe4d8a18ded3a52e')
        manager = owm.weather_manager()
        try:
            weather_report = manager.weather_at_place(name).weather
            temperature = weather_report.temperature('celsius')
            humidity = weather_report.humidity
            status = weather_report.detailed_status
            report[name] = City.format_weather(temperature, humidity, status)
        except (pyowm.commons.exceptions.NotFoundError, pyowm.commons.exceptions.TimeoutError):
            return True

    '''
    Método para solicitar desde fuera de la clase
    el reporte del clima de una instancia de City
    :return: El reporte del clima para una instancia de City
    '''
    def get_weather(self):
        if self._name in self.weather_info:
            return self.weather_info[self._name]
        error = City.request_weather(self.weather_info, self._name)
        if error:
            return 'Weather unavailable'
        return self.weather_info[self._name]
