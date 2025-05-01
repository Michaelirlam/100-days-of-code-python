import csv
import pandas


with open("weather_data.csv") as weather:
    data = csv.reader(weather)
    
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    
    print(temperatures)