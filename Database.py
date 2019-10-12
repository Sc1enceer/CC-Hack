from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "Database"
client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token="Jj1BNzx75RudUoWlu8zuK8GNg5JoTpS5m-u0E-HeMKWvOnUzNa_0ZvO0JMxgSaYNqEQ1LJEZnVL1a1E-Rzg85w==", org="cchack")
write_api = client.write_api(write_options=SYNCHRONOUS)
# query_api = client.query_api()

p = Point("my_measurement").field("value", 11.5)

write_api.write(bucket=bucket, org="cchack", record=p)

# using Table structure
# tables = query_api.query('from(bucket:"Testing") |> range(start: -10m)')
#
# for table in tables:
#     #print(table)
#     for row in table.records:
#         print (row.values)
#         print (row.values['_value'])
