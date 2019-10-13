import os
from flask import Flask
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import json
from flask_cors import CORS

bucket = "Database"
client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token="Jj1BNzx75RudUoWlu8zuK8GNg5JoTpS5m-u0E-HeMKWvOnUzNa_0ZvO0JMxgSaYNqEQ1LJEZnVL1a1E-Rzg85w==", org="cchack")
query_api = client.query_api()

# spectrum lists
blueList = []
greenList = []
orangeList = []
redList = []
violetList = []
yellowList = []

blue_couples = {}
orange_couples = {}
red_couples = {}
green_couples = {}
violet_couples = {}
yellow_couples = {}
# humidityList = []


name_list = ['Humidity', 'Temperature', 'Sunlight', 'Wind Speed']
temperatureList = []
humidityList = []
sunlightList = []
windList = []
list = [humidityList, temperatureList, sunlightList, windList]
app = Flask(__name__)
CORS(app)

@app.route('/Humidity')
def humidityValues():
    humidityList = []
    tables = query_api.query('from(bucket:"Database") |> range(start: -600m)')
    for table in tables:
        for row in table.records:
            if str(row.values['_measurement']) == "humidity":
                humidityList.append(row.values)
    result = ''
    print(humidityList)
    if humidityList.__len__() != 0:
        value_list = []
        time_list = []
        for list in humidityList:
            value_list.append(list['_value'])
            time_list.append(list['_time'])
        zip_list = zip(value_list, time_list)
        dictionary = [{'x' : str(value), 'y' : str(time)} for time,value in zip_list]
        couples = {'id':'humidity', 'color':'hsl(130, 70%, 50%)', 'data' : dictionary}
        # result = json.dumps(couples)
        # print(result)
    return json.dumps(couples)

@app.route('/wind')
def windValues():
    windList = []
    tables = query_api.query('from(bucket:"Database") |> range(start: -200m)')
    for table in tables:
        for row in table.records:
            if str(row.values['_measurement']) == "wind":
                windList.append(row.values)
    result = ''
    if windList.__len__() != 0:
        value_list = []
        time_list = []
        for list in windList:
            value_list.append(list['_value'])
            time_list.append(list['_time'])
        zip_list = zip(value_list, time_list)
        dictionary = str(dict([(str(time), str(value)) for time, value in zip_list]))
        couples = [['id', 'wind'],
                   ['color', 'hsl(130, 70%, 50%)'],
                   ['data', dictionary]]
        result = json.dumps(couples)
    return result

@app.route('/sunlight')
def sunlightValues():
    windList = []
    tables = query_api.query('from(bucket:"Database") |> range(start: -200m)')
    for table in tables:
        for row in table.records:
            if str(row.values['_measurement']) == "sunlight":
                sunlightList.append(row.values)
    result = ''
    if sunlightList.__len__() != 0:
        value_list = []
        time_list = []
        for list in sunlightList:
            value_list.append(list['_value'])
            time_list.append(list['_time'])
        zip_list = zip(value_list, time_list)
        dictionary = str(dict([(str(time), str(value)) for time, value in zip_list]))
        couples = [['id', 'wind'],
                   ['color', 'hsl(130, 70%, 50%)'],
                   ['data', dictionary]]
        result = json.dumps(couples)
    return result


@app.route('/Temperature')
def temperatureValues():
    temperatureList = []
    tables = query_api.query('from(bucket:"Database") |> range(start: -900m)')
    for table in tables:
        for row in table.records:
            if str(row.values['_measurement']) == "temperature":
                temperatureList.append(row.values)
    result = ''
    if temperatureList.__len__() != 0:
        value_list = []
        time_list = []
        for list in temperatureList:
            value_list.append(list['_value'])
            time_list.append(list['_time'])
        zip_list = zip(value_list, time_list)
        dictionary = [{'x' : str(value), 'y' : str(time)} for time, value in zip_list]
        couples = {'id' :'temperature', 'color': 'hsl(130, 70%, 50%)', 'data': dictionary}
        result = json.dumps(couples)
    return result


@app.route('/spectrumData')
def spectrumData():
    tables = query_api.query('from(bucket:"Database") |> range(start: -150)')
    for table in tables:
        for row in table.records:
            row_values = row.values
            if (str(row_values['_measurement']) == "spectrum"):
                 if(str(row_values['_field']) == "Green"):
                     greenList.append(row_values)
                 elif (str(row_values['_field']) == "Blue"):
                     blueList.append(row_values)
                 elif (str(row_values['_field']) == "Orange"):
                     orangeList.append(row_values)
                 elif (str(row_values['_field']) == "Red"):
                     redList.append(row_values)
                 elif (str(row_values['_field']) == "Violet"):
                     violetList.append(row_values)
                 elif (str(row_values['_field']) == "Yellow"):
                     yellowList.append(row_values)

    # color set
    if blueList.__len__() != 0:
        # print ("Hi I am here")
        blue_value_list = []
        blue_time_list = []
        for list in blueList:
            blue_value_list.append(list['_value'])
            blue_time_list.append(list['_time'])
        zip_list = zip(blue_value_list, blue_time_list)
        dictionary = [{'x' : str(time), 'y' : str(value)} for value,time in zip_list]
        blue_couples = {'id':'blue', 'color':'hsl(52, 70%, 50%)', 'data': dictionary}
        # result = json.dumps(blue_couples)
        # print(result)

# color set
    if greenList.__len__() != 0:
        green_value_list = []
        green_time_list = []
        for list in greenList:
            green_value_list.append(list['_value'])
            green_time_list.append(list['_time'])
        zip_list = zip(green_value_list, green_time_list)
        dictionary = [{'x' : str(time), 'y' : str(value)} for value,time in zip_list]
        green_couples = {'id':'green', 'color':'hsl(293, 70%, 50%)','data': dictionary}
        # result = json.dumps(green_couples)
        # print(result)

# color set
    if orangeList.__len__() != 0:
        orange_value_list = []
        orange_time_list = []
        for list in orangeList:
            orange_value_list.append(list['_value'])
            orange_time_list.append(list['_time'])
        zip_list = zip(orange_value_list, orange_time_list)
        dictionary = [{'x' : str(time), 'y' : str(value)} for value,time in zip_list]
        orange_couples = {'id':'orange', 'color':'hsl(358, 70%, 50%)', 'data' : dictionary}
        # result = json.dumps(orange_couples)
        # print(result)

# color code set
    if redList.__len__() != 0:
        red_value_list = []
        red_time_list = []
        for list in redList:
            red_value_list.append(list['_value'])
            red_time_list.append(list['_time'])
        zip_list = zip(red_value_list, red_time_list)
        dictionary = [{'x' : str(time), 'y' : str(value)} for value,time in zip_list]
        red_couples = {'id':'red', 'color':'hsl(74, 70%, 50%)', 'data' : dictionary}
        # result = json.dumps(red_couples)
        # print(result)

    if violetList.__len__() != 0:
        violet_value_list = []
        violet_time_list = []
        for list in violetList:
            violet_value_list.append(list['_value'])
            violet_time_list.append(list['_time'])
        zip_list = zip(violet_value_list, violet_time_list)
        dictionary = [{'x': str(time), 'y': str(value)} for value, time in zip_list]
        violet_couples = {'id': 'violet', 'color': 'hsl(275, 86%, 29%)', 'data': dictionary}
        # result = json.dumps(violet_couples)
        # print(result)

# color code set
    if yellowList.__len__() != 0:
        yellow_value_list = []
        yellow_time_list = []
        for list in violetList:
            yellow_value_list.append(list['_value'])
            yellow_time_list.append(list['_time'])
        zip_list = zip(yellow_value_list, yellow_time_list)
        dictionary = [{'x': str(time), 'y': str(value)} for value, time in zip_list]
        yellow_couples = {'id': 'yellow', 'color': 'hsl(314, 70%, 50%)', 'data': dictionary}
        spectrumDic = [blue_couples, green_couples,  orange_couples, red_couples, violet_couples, yellow_couples]
        return (json.dumps(spectrumDic))


@app.route('/currentValues')
def currentValues():
    tables = query_api.query('from(bucket:"Database") |> range(start: -900m)')
    for table in tables:
        for row in table.records:
            if str(row.values['_measurement']) == "humidity":
                humidityList.append(row.values)
            elif str(row.values['_measurement']) == "temperature":
                temperatureList.append(row.values)
            elif str(row.values['_measurement']) == "sunlight":
                sunlightList.append(row.values)
            elif str(row.values['_measurement']) == "wind":
                windList.append(row.values)

    counter = 0
    result = {}

    for l in list:
        n = l.__len__()
        result[name_list[counter]] = str(l[n - 1]['_value'])
        counter += 1
    return json.dumps(result)

if __name__ == '__main__':
    app.run()





