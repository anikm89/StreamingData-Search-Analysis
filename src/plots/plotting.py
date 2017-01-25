from bokeh.charts import Bar,HeatMap
from bokeh.charts import output_file, show
from bokeh.layouts import row
from pandas import DataFrame

from datetime import date
from random import randint

from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.io import output_file, show, vform
from bokeh.models.widgets import Slider
from bokeh.models import CustomJS


def makePlots(tweetdict,commonTweets):

    # best support is with data in a format that is table-like
    data = {
        'sample': ['1st', '2nd', '1st', '2nd', '1st', '2nd'],
        'interpreter': ['python', 'python', 'pypy', 'pypy', 'jython', 'jython'],
        'timing': [-2, 5, 12, 40, 22, 30]
    }

    hm_df =DataFrame(commonTweets, columns=["Text", "Counts"])

    # x-axis labels pulled from the interpreter column, stacking labels from sample column
    bar = Bar(data, values='timing', label='interpreter', stack='sample', agg='mean',
              title="Python Interpreter Sampling", legend='top_right', plot_width=400)

    # table-like data results in reconfiguration of the chart with no data manipulation
    bar2 = Bar(data, values='timing', label=['interpreter', 'sample'],
               agg='mean', title="Python Interpreters", plot_width=400)

    bar3 = Bar(tweetdict, values='QueryScore', label='QueryList', agg='count',
              title="Python Interpreter Sampling", legend='top_right', plot_width=400)




    print hm_df

    source = ColumnDataSource(hm_df)
    columns = [
        TableColumn(field="Text", title="Text"),
        TableColumn(field="Counts", title="Counts"),
    ]
    data_table = DataTable(source=source, columns=columns, width=500, height=300)

    callback = CustomJS(args=dict(source=source), code="""
            var data = source.get('data');
            var f = cb_obj.get('value')
            x = data['x']
            y = data['y']
            for (i = 0; i < x.length; i++) {
                y[i] = Math.pow(x[i], f)
            }
            source.trigger('change');
        """)

    slider = Slider(start=0, end=10, value=1, step=1, title="Stuff", callback=callback)
    #output_file("stacked_bar.html")
    #show(row(data_table))
    #show(vform(data_table,slider))

