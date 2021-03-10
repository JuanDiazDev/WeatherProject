import pandas
import City
import threading
import time
import Codes

#Creamos un objeto Codes a partir de los codigos IATA de la base de datos airportcodes
IATA = Codes.Codes('airportcodes.csv')
CODES = IATA.get_codes()

#Lee el primer dataset y va imprimiendo en pantalla la información a partir del archivo
def read1():
    df = pandas.read_csv('dataset1.csv')
    for i in range(3000):
        if i % 150 == 0:
            time.sleep(30)
        origin_name = CODES[df['origin'][i]]
        destination_name = CODES[df['destination'][i]]
        origin = City.City(origin_name)
        origin_weather = origin.get_weather()
        destination = City.City(destination_name)
        destination_weather = destination.get_weather()
        print(f'DEPARTURE: {origin_name}: {origin_weather}\nARRIVAL: {destination_name}: {destination_weather}')

#Lee el segundo dataset e imprime en pantalla la salida generada por la entrada del dataset
def read2():
    df = pandas.read_csv('dataset2.csv')
    for i in range(1002):
        if i % 100 == 0:
            time.sleep(60)
        destination_name = df['destino'][i]
        destination = City.City(destination_name)
        destination_weather = destination.get_weather()
        MEX = City.City('Mexico City')
        MEX_WEATHER = MEX.get_weather()
        print(f'DEPARTURE: Mexico City: {MEX_WEATHER}\nARRIVAL: {destination_name}: {destination_weather}')


t1 = threading.Thread(target=read1)
t2 = threading.Thread(target=read2)

t1.start()
t2.start()
t1.join()
t2.join()
