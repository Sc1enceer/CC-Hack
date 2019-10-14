from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "Database"
client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token="Jj1BNzx75RudUoWlu8zuK8GNg5JoTpS5m-u0E-HeMKWvOnUzNa_0ZvO0JMxgSaYNqEQ1LJEZnVL1a1E-Rzg85w==", org="cchack")
# write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
name_list = ['humidity', 'temperature', 'sunlight', 'wind']
temperatureList = []
humidityList = []
sunlightList = []
windList = []
list = [humidityList, temperatureList, sunlightList, windList]
# p = Point("sunlight").field("value", 5000)
#
# write_api.write(bucket=bucket, org="cchack", record=p)

# using Table structure
tables = query_api.query('from(bucket:"Database") |> range(start: -60m)')
#
#
for table in tables:
    #print(table)
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
result=''

for l in list:
    n = l.__len__()
    result += name_list[counter] + ' ' + str(l[n-1]['_value']) + '\n'
    counter += 1

print(result)
