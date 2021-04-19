import dash  
import dash_core_components as dcc  
import dash_html_components as html 
from covid19MX import fechas_mexico, confirmados_mexico, muertes_mexico, recuperados_mexico, activos_mexico





app = dash.Dash(__name__)
server = app.server

colors = {
    'fondo': "#FDFEFE",
    'texto': "#21618C"
}

app.layout = html.Div(style={'backgroundColor': colors['fondo']}, children=[
    html.H1(
        children=["México 2021: Casos COVID-19"],
        style={
            'textAlign': 'center',
            'color': colors['texto'],
             "font-size": 50
           
        
        }
    ),
    dcc.Graph(
        id="graph1",
        figure={
            'data': [
                {'x': fechas_mexico[:-1], 'y': confirmados_mexico[:-1], 'type': 'line', 'name': 'Casos Confirmados'},
                {'x': fechas_mexico[:-1], 'y': muertes_mexico[:-1], 'type': 'line', 'name': 'Muertes'},
                {'x': fechas_mexico[:-1], 'y': recuperados_mexico[:-1], 'type': 'line', 'name': 'Recuperados'},
                {'x': fechas_mexico[:-1], 'y': activos_mexico[:-1], 'type': 'line', 'name': 'Activos'},
               ],
            'layout': {
                'title': 'Casos al 18 de Abril',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors["texto"]
                }
            }
        }

    ),
    dcc.Markdown(children="""
    ## Elaboración propia con datos de COVID 19 API https://covid19api.com/
    

    """, style={
        'color': colors['texto'],
        "font-size": 10
    })
])

if __name__ == "__main__":
    app.run_server(debug=True)