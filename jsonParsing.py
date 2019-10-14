from influxdb_client import InfluxDBClient, Point, WriteOptions
# from influxdb_client.client.write_api import SYNCHRONOUS
import json

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

tables = query_api.query('from(bucket:"Database") |> range(start: -300m)')



def spectrumData():
    for table in tables:
        # print(table)
        for row in table.records:
             if (str(row.values['_measurement']) == "spectrum"):
                 print(row.values)
                 if(str(row.values['_field']) == "Green"):
                     greenList.append(row.values)
                 elif (str(row.values['_field']) == "Blue"):
                     blueList.append(row.values)
                 elif (str(row.values['_field']) == "Orange"):
                     orangeList.append(row.values)
                 elif (str(row.values['_field']) == "Red"):
                     redList.append(row.values)
                 elif (str(row.values['_field']) == "Violet"):
                     violetList.append(row.values)
                 elif (str(row.values['_field']) == "Yellow"):
                     yellowList.append(row.values)

        # print(yellowList[0])
    # color set
        if blueList.__len__() != 0:
            blue_value_list = []
            blue_time_list = []
            for list in blueList:
                blue_value_list.append(list['_value'])
                blue_time_list.append(list['_time'])
            zip_list = zip(blue_value_list, blue_time_list)
            dictionary = [{'x' : str(time), 'y' : str(value)} for value,time in zip_list]
            blue_couples = {'id':'blue', 'color':'hsl(52, 70%, 50%)', 'data' : dictionary}
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
            green_couples = {'id':'green', 'color':'hsl(293, 70%, 50%)', 'data' : dictionary}
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
            # result = json.dumps(yellow_couples)
            # print(result)


            spectrumDic = [ blue_couples, green_couples,  orange_couples, red_couples, violet_couples, yellow_couples]
            return (json.dumps(spectrumDic))

    print(spectrumData())

