import dash  
import dash_core_components as dcc  
import dash_html_components as html 
from covid19MX import fechas_mexico, confirmados_mexico, muertes_mexico, recuperados_mexico, activos_mexico
from covidgob import fecha_ingreso, edad, positivo, negativo, fecha_def, inmusupr, entidad_res, tipo_paciente, cardiovascular, neumonia, hipertension, otra_com, epoc, asma, fecha_sintomas, nacionalidad, pais_origen, rango_edad, embarazo, municipio_res, sexo, obesidad, habla_lengua_indi, intubado, tabaquismo, diabetes, edad, num_hospitalizados, pais_nacionalidad, migrante, entidad_nac, otro_caso, renal_cronica




app = dash.Dash(__name__)
server = app.server

colors = {
    'fondo': "#FDFEFE",
    'texto': "#21618C"
}

app.layout = html.Div(style={'backgroundColor': colors['fondo']}, children=[
    html.H1(
        children=["México 2020: Casos COVID-19"],
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
                'title': 'Casos República Mexicana',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors["texto"]
                }
            }
        }
        
    ),
    dcc.Graph(
        id="graph2",
        figure={
            'data': [
                {'x': fechas_mexico[:-1], 'y': edad[:-1], 'type': 'line', 'name': 'Casos Confirmados'},
                
               ],
            'layout': {
                'title': 'Casos Ciudad de México',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors["texto"]
                }
            }
        }
    ),
    dcc.Graph(
        id="graph3",
        figure={
            'data': [
                {'x': [positivo], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [negativo], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Markdown(children="""
    ## Elaboración propia con datos de COVID 19 API https://covid19api.com/ y Gobierno de la Ciudad de México https://datos.cdmx.gob.mx/
    

    """, style={
        'color': colors['texto'],
        "font-size": 10
    })
])

if __name__ == "__main__":
    app.run_server(debug=True)