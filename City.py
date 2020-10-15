import pyowm


class City:
    dic = {}

    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    # Regresa una cadena para mostrar la informacion del clima
    @staticmethod
    def format_weather(tem, humidity, status):
        maxi = tem['temp_max']
        mini = tem['temp_min']
        return f'Weather: {status}, Temperature: Max: {maxi} Min: {mini}, Humidity: {humidity}'

    # Solicita a OWM API el informe del clima
    @staticmethod
    def request_weather(dic, name):
        owm = pyowm.OWM('4f35f6733973b80abe4d8a18ded3a52e')
        mgr = owm.weather_manager()
        try:
            weather_report = mgr.weather_at_place(name).weather
            temperature = weather_report.temperature('celsius')
            humidity = weather_report.humidity
            status = weather_report.detailed_status
            dic[name] = City.format_weather(temperature, humidity, status)
        except (pyowm.commons.exceptions.NotFoundError, pyowm.commons.exceptions.TimeoutError):
            return True

    # Regresa el informe del clima de una instancia de la clase
    def get_weather(self):
        if self._name in self.dic:
            return self.dic[self._name]
        err = City.request_weather(self.dic, self._name)
        if err:
            return 'Weather unavailable'
        return self.dic[self._name]
