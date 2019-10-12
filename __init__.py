import os
from flask import Flask
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "Database"
client = InfluxDBClient(url="http://localhost:9999", token="_OE7L3Ayc6ZXEIC8Yva9SllcihnaqANWdH2NAEHRy3mO4P6cfg3WIvSUMDtYWhz_COsATmhhdbHsFBGsw4CG5g==", org="cchack")
query_api = client.query_api()

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



    # data analysis
    @app.route('/hello')
    def hello():
        a = ""
        tables = query_api.query('from(bucket:"Testing") |> range(start: -10m)')
        for table in tables:
            for row in table.records:
                a += (str(row.values['_value']) + ' ')
        return a

    return app