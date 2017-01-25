import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF


def piePlot(n,p,neg):
    fig = {
        'data': [{'labels': ['Positive', 'Negative', 'Neutral'],
                  'values': [p, neg, n],
                  'type': 'pie',
                  'hoverinfo': 'label+percent+name',
                  'marker': {'colors': ['rgb(0,128,0)',
                                        'rgb(220,20,60)',
                                        'rgb(211,211,211)']}
                  }],
        'layout': {'title': 'tweets senitment analysis'}
         }

    py.image.save_as(fig, filename='pie.png')

def dataTable(df):
    table = FF.create_table(df)
    py.image.save_as(table, filename='dataTable.png')
    #py.iplot(table, filename='index_table_pd')


