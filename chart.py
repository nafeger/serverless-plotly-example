from datetime import datetime, timedelta
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objs as go
import plotly.plotly as py
import yaml



def config():
    with open("config.yaml", 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def publish(event, context):
    c = config()['plotly_auth']
    py.sign_in(username=c['username'],api_key=c['api_key'])

    # borrowed from here: https://plot.ly/numpy/array/

    x = np.array([1, 2, 3])
    y = np.array([4, 7, 2])

    trace = go.Scatter(x=x, y=y)
    py.plot([trace], filename='numpy-array-ex1')
