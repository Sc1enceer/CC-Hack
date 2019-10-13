import os
from flask import Flask
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import json

bucket = "Database"
client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token="Jj1BNzx75RudUoWlu8zuK8GNg5JoTpS5m-u0E-HeMKWvOnUzNa_0ZvO0JMxgSaYNqEQ1LJEZnVL1a1E-Rzg85w==", org="cchack")
query_api = client.query_api()


name_list = ['humidity', 'temperature', 'sunlight', 'wind']
temperatureList = []
humidityList = []
sunlightList = []
windList = []
list = [humidityList, temperatureList, sunlightList, windList]

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) # this creates the flask instance
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # @app.route('/hello')
    # def hello():
    #     a = ""
    #     tables = query_api.query('from(bucket:"Database") |> range(start: -60m)')
    #     for table in tables:
    #         for row in table.records:
    #             a += (str(row.values['_value']) + ' ')
    #     return a


    @app.route('/humidity')
    def humidityValues():
        humidityList = []
        tables = query_api.query('from(bucket:"Database") |> range(start: -300m)')
        for table in tables:
            for row in table.records:
                if str(row.values['_measurement']) == "humidity":
                    humidityList.append(row.values)
        result = ''
        if humidityList.__len__() != 0:
            value_list = []
            time_list = []
            for list in humidityList:
                value_list.append(list['_value'])
                time_list.append(list['_time'])
            zip_list = zip(value_list, time_list)
            dictionary = [{'x' : str(value), 'y' : str(time)} for time,value in zip_list]
            couples = {'id':'humidity', 'color':'hsl(130, 70%, 50%)', 'data' : dictionary}
            result = json.dumps(couples)
            print(result)
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
            result = jsons.dumps(couples)
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


    @app.route('/temperature')
    def temperatureValues():
        temperatureList = []
        tables = query_api.query('from(bucket:"Database") |> range(start: -200m)')
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

    @app.route('/currentValues')
    def currentValues():
        tables = query_api.query('from(bucket:"Database") |> range(start: -200m)')
        for table in tables:
            # print(table)
            for row in table.records:
                if str(row.values['_measurement']) == "humidity":
                    # print (row.values)
                    humidityList.append(row.values)
                elif str(row.values['_measurement']) == "temperature":
                    temperatureList.append(row.values)
                elif str(row.values['_measurement']) == "sunlight":
                    sunlightList.append(row.values)
                elif str(row.values['_measurement']) == "wind":
                    windList.append(row.values)
                else:
                    print('errors wrong measurement')

        counter = 0
        result = ''

        for l in list:
            n = l.__len__()
            result += name_list[counter] + ' ' + str(l[n - 1]['_value']) + ' ' + str(l[n - 1]['_time']) + '\n'
            counter += 1
        return result
    return app





