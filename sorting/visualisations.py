import json
import plotly.graph_objects as go

from sorting.research import ORDERED, RESERVED, RANDOM


def show_algorithm_complexities(filename):
    with open(filename) as f:
        result = json.load(f)

    domain = result[ORDERED].keys()

    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(domain), y=list(result[ORDERED].values()), mode='lines+markers', name=ORDERED))
    figure.add_trace(go.Scatter(x=list(domain), y=list(result[RESERVED].values()), mode='lines+markers', name=RESERVED))
    figure.add_trace(go.Scatter(x=list(domain), y=list(result[RANDOM].values()), mode='lines+markers', name=RANDOM))
    figure.show()


def show_complexities(filenames, order_type):
    figure = go.Figure()
    for filename in filenames:
        with open(filename) as f:
            result = json.load(f)

        domain = result[ORDERED].keys()
        figure.add_trace(go.Scatter(x=list(domain), y=list(result[order_type].values()), mode='lines+markers',
                                    name=f"{filename.split('_')[0]}_{order_type}"))

    figure.show()


def show_complexities_types(filenames, types):
    figure = go.Figure()
    for filename in filenames:
        for order_type in types:
            with open(filename) as f:
                result = json.load(f)

            domain = result[ORDERED].keys()
            figure.add_trace(go.Scatter(x=list(domain), y=list(result[order_type].values()), mode='lines+markers',
                                        name=f"{filename.split('_')[0]}_{order_type}"))

    figure.show()


if __name__ == '__main__':
    # show_algorithm_complexities('BubbleSort_100.json')
    # show_algorithm_complexities('QuickSort_100.json')

    filenames = ['BubbleSort_100.json', 'QuickSort_100.json']
    show_complexities_types(filenames, [ORDERED, RESERVED, RANDOM])
    # show_complexities(filenames, ORDERED)
    # show_complexities(filenames, REVERSED)
    # show_complexities(filenames, RANDOM)