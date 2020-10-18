import json
import plotly.graph_objects as go

from sorting.research import ORDERED, RANDOM, RESERVED


def show_algorithm_complexities(filename):
    with open(filename) as f:
        result = json.load(f)

    domain = result[ORDERED].keys()

    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(domain), y=list(result[ORDERED].values()), mode='lines+markers', name=ORDERED))
    figure.add_trace(go.Scatter(x=list(domain), y=list(result[RESERVED].values()), mode='lines+markers', name=RESERVED))
    figure.add_trace(go.Scatter(x=list(domain), y=list(result[RANDOM].values()), mode='lines+markers', name=RANDOM))
    figure.show()
    print(result)


if __name__ == '__main__':
    show_algorithm_complexities('BubbleSort_100.json')
