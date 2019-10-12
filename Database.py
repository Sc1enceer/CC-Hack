from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "Database"
client = InfluxDBClient(url="http://localhost:9999", token="_OE7L3Ayc6ZXEIC8Yva9SllcihnaqANWdH2NAEHRy3mO4P6cfg3WIvSUMDtYWhz_COsATmhhdbHsFBGsw4CG5g==", org="cchack")
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

p = Point("my_measurement").tag("location", "Prague").field("value", 25.3)

write_api.write(bucket=bucket, org="cchack", record=p)


# using Table structure
tables = query_api.query('from(bucket:"Database") |> range(start: -10m)')

for table in tables:
    #print(table)
    for row in table.records:
        print (row.values)
        print (row.values['_value'])




