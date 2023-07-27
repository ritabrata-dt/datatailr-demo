import sys
import dash # pylint: disable=no-name-in-module, import-error
from dash import dcc # pylint: disable=no-name-in-module, import-error
from dash import html # pylint: disable=no-name-in-module, import-error
import plotly.graph_objs as go # pylint: disable=no-name-in-module, import-error
import pandas as pd # pylint: disable=no-name-in-module, import-error
import dt.dash


def create_app(port=None):
    df = pd.read_excel(
        "https://github.com/chris1610/pbpython/blob/master/data/salesfunnel.xlsx?raw=True"
    )
    mgr_options = df["Manager"].unique()

    dash_application = dt.dash.Dash('Dash Demo', port=port)

    dash_application.layout = html.Div([
        html.H2("Sales Funnel Report"),
        html.Div(
            [
                dcc.Dropdown(
                    id="Manager",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in mgr_options],
                    value='All Managers'),
            ],
            style={'width': '25%',
                'display': 'inline-block'}),
        dcc.Graph(id='funnel-graph'),
    ])

    @dash_application.callback(
        dash.dependencies.Output('funnel-graph', 'figure'),
        [dash.dependencies.Input('Manager', 'value')])
    def update_graph(Manager):
        if Manager == "All Managers":
            df_plot = df.copy()
        else:
            df_plot = df[df['Manager'] == Manager]

        pv = pd.pivot_table(
            df_plot,
            index=['Name'],
            columns=["Status"],
            values=['Quantity'],
            aggfunc=sum,
            fill_value=0)

        trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
        trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pending')], name='Pending')
        trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presented')], name='Presented')
        trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'won')], name='Won')

        return {
            'data': [trace1, trace2, trace3, trace4],
            'layout':
            go.Layout(
                title='Customer Order Status for {}'.format(Manager),
                barmode='stack')
        }
    return dash_application

def __app_main__():
    return create_app().application

if __name__ == '__main__':
    port = int(sys.argv[1])
    app = create_app(port)
    app.run('0.0.0.0', port=port, debug=True)
