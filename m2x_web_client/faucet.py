import os
import datetime
from models import StreamParser, FlowStream
from m2x.client import M2XClient
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')

client = M2XClient(os.environ['MASTER_API_KEY'])
device = client.device(os.environ['DEVICE_ID'])


@app.route('/')
def main():
    temp_stream = StreamParser(device.stream('temperature'))
    flow_stream = FlowStream(device.stream('water_use'))
    return render_template('body.html', temp_stream=temp_stream, flow_stream=flow_stream)
