from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import json

bucket = "Database"
client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token="Jj1BNzx75RudUoWlu8zuK8GNg5JoTpS5m-u0E-HeMKWvOnUzNa_0ZvO0JMxgSaYNqEQ1LJEZnVL1a1E-Rzg85w==", org="cchack")
query_api = client.query_api()
humidityList = []
tables = query_api.query('from(bucket:"Database") |> range(start: -300m)')

for table in tables:
    #print(table)
    for row in table.records:
         if str(row.values['_measurement']) == "humidity":
              humidityList.append(row.values)

class App(dict):
    def __str__(self):
        return json.dumps(self)

value_list = []
time_list = []
for list in humidityList:
    value_list.append(list['_value'])
    time_list.append(list['_time'])
zip_list = zip(value_list,time_list)
dictionary = str(dict([(str(time), str(value)) for time, value in zip_list]))

couples = [['id', 'humidity'],
           ['color', 'hsl(130, 70%, 50%)'],
           ['data', dictionary]]

toParse = App(couples)
print(toParse)
