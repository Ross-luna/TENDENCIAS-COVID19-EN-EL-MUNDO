import dash   # Servidor Flask
import dash_core_components as dcc  # Graficacion
import dash_html_components as html # HTML



from covmun import confirmados_india, muertes_india, fechas_india, total_confirmados_india, total_muertes_india, desvest_india_c, desvest_india_m, mediana_india_c, mediana_india_m, media_india_c, media_india_m
from covmun import confirmados_andorra, muertes_andorra, fechas_andorra, total_confirmados_andorra, total_muertes_andorra, desvest_andorra_c, desvest_andorra_m, mediana_andorra_c, mediana_andorra_m, media_andorra_c, media_andorra_m 
from covmun import confirmados_qatar, muertes_qatar, fechas_qatar, total_confirmados_qatar, total_muertes_qatar, desvest_qatar_c, desvest_qatar_m, mediana_qatar_c, mediana_qatar_m, media_qatar_c, media_qatar_m 
from covmun import confirmados_burundi, muertes_burundi, fechas_burundi, total_confirmados_burundi, total_muertes_burundi, desvest_burundi_c, desvest_burundi_m, mediana_burundi_c, mediana_burundi_m, media_burundi_c, media_burundi_m 
from covmun import confirmados_nigeria, muertes_nigeria, fechas_nigeria, total_confirmados_nigeria, total_muertes_nigeria, desvest_nigeria_c, desvest_nigeria_m, mediana_nigeria_c, mediana_nigeria_m, media_nigeria_c, media_nigeria_m 
from covmun import confirmados_monaco, muertes_monaco, fechas_monaco, total_confirmados_monaco, total_muertes_monaco, desvest_monaco_c, desvest_monaco_m, mediana_monaco_c, mediana_monaco_m, media_monaco_c, media_monaco_m 
from covmun import confirmados_ukraine, muertes_ukraine, fechas_ukraine, total_confirmados_ukraine, total_muertes_ukraine, desvest_ukraine_c, desvest_ukraine_m, mediana_ukraine_c, mediana_ukraine_m, media_ukraine_c, media_ukraine_m
from covmun import confirmados_oman, muertes_oman, fechas_oman, total_confirmados_oman, total_muertes_oman, desvest_oman_c, desvest_oman_m, mediana_oman_c, mediana_oman_m, media_oman_c, media_oman_m 
from covmun import confirmados_russia, muertes_russia, fechas_russia, total_confirmados_russia, total_muertes_russia, desvest_russia_c, desvest_russia_m, mediana_russia_c, mediana_russia_m, media_russia_c, media_russia_m 
from covmun import confirmados_angola, muertes_angola, fechas_angola, total_confirmados_angola, total_muertes_angola, desvest_angola_c, desvest_angola_m, mediana_angola_c, mediana_angola_m, media_angola_c, media_angola_m 

#CASO INDIA ANDORRA
labels_india_andorra ="Confirmados India","Muertes India","Confirmados Andorra","Muertes Andorra"
values_india_andorra = 335022617,6137346,192989,9278


#CASO QATAR BURURNDI
labels_qatar_burundi ="Confirmados  Qatar","Muertes Qatar","Confirmados Burundi","Muertes Burundi"
values_qatar_burundi = 15066851, 21611,44075,179

#CASO NIGERIA MONACO

labels_nigeria_monaco ="Confirmados Nigeria","Muertes Nigeria","Confirmados Monaco","Muertes Monaco"
values_nigeria_monaco = 5500275,114299,24054,620

#CASO UCRANIA OMAN

labels_ukraine_oman ="Confirmados Ucrania","Muertes Ucrania","Confirmados Oman","Muertes Oman"
values_ukraine_oman = 13342085,296008, 8989283, 62867

#CASO RUSIA ANGOLA

labels_rusia_angola ="Confirmados Rusia","Muertes Rusia","Confirmados Angola","Muertes Angola"
values_rusia_angola = 119249816,1894863,241661,9762



app = dash.Dash(__name__)
server = app.server

colors = {
   'fondo': "#FDFEFE",
    'texto': "#21618C"
}

app.layout = html.Div(style={'backgroundColor': colors['fondo']}, children=[
    html.H1(
        children=["2020: Tendencias de COVID-19 en el mundo"],
        style={
            'textAlign': 'center',
            'color': colors['texto'],
            "font-size": 50
        }
    ),
    dcc.Graph(
        id="india_andorra",
        figure={
            'data': [
                {'x': fechas_india[:-1], 'y': confirmados_india[:-1], 'type': 'line', 'name': 'Confirmados India'},
                {'x': fechas_india[:-1], 'y': muertes_india[:-1], 'type': 'line', 'name': 'Muertes India'},
                {'x': fechas_andorra[:-1], 'y': confirmados_andorra[:-1], 'type': 'line', 'name': 'Confirmados Andorra'},
                {'x': fechas_andorra[:-1], 'y': muertes_andorra[:-1], 'type': 'line', 'name': 'Muertes Andorra'},
                
            ],
            'layout': {
                'title': 'Análisis de dos de los países con mayor (India) y menor población (Andorra)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto'],
                    "size" : 15
                }
            }
        }
    ),
    
    
     dcc.Graph(
         
        id="comp1",
        figure={
            'data': [
                {'y': total_confirmados_india, 'type': 'bar', 'name': 'Confirmados India'},
                {'y': total_confirmados_andorra, 'type': 'bar', 'name': 'Confirmados Andorra'},  
                {'y': total_muertes_india, 'type': 'bar', 'name': 'Muertes India'},
                {'y': total_muertes_andorra, 'type': 'bar', 'name': 'Muertes Andorra'},  
            ],
            'layout': {
                'title': 'Comparativo casos confirmados y muertes (India y Andorra)',
                'plot_bgcolor': colors['fondo'],
                "height" : "25%", 
                "width" : "100%",
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    
     dcc.Graph(
         
        id="Estadisticos1",
        figure={
            'data': [
                {'y':  desvest_india_c, 'type': 'bar', 'name': 'DESVEST_india_CONFIRMADOS'},
                {'y':  desvest_andorra_c, 'type': 'bar', 'name': 'DESVEST_andorra_CONFIRMADOS'},
                {'y':  desvest_india_m, 'type': 'bar', 'name': 'DESVEST_india_MUERTES'},  
                {'y':  desvest_andorra_m, 'type': 'bar', 'name': 'DESVEST_andorra_MUERTES'}, 
                {'y':  mediana_india_c, 'type': 'bar', 'name': 'MEDIANA_india_CONFIRMADOS'},
                {'y':  mediana_andorra_c, 'type': 'bar', 'name': 'MEDIANA_andorra_CONFIRMADOS'},
                {'y':  mediana_india_m, 'type': 'bar', 'name': 'MEDIANA_india_MUERTES'},
                {'y':  mediana_andorra_m, 'type': 'bar', 'name': 'MEDIANA_andorra_MUERTES'},
                {'y':  media_india_c, 'type': 'bar', 'name': 'MEDIA_india_CONFIRMADOS'},
                {'y':  media_andorra_c, 'type': 'bar', 'name': 'MEDIA_andorra_CONFIRMADOS'},
                {'y':  media_india_m, 'type': 'bar', 'name': 'MEDIA_india_MUERTES'},
                {'y':  media_andorra_m, 'type': 'bar', 'name': 'MEDIA_andorra_MUERTES'},
               
                
            ],
            'layout': {
                'title': 'Comparativo estadístico (India y Andorra)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    
     dcc.Graph(
        id='pie_india_andorra',
        figure={
            'data': [{
                'values': values_india_andorra,
                'labels': labels_india_andorra,
                'type': 'pie'
            }],
            'layout': {
                'title': 'Porcentaje casos confirmados y muertes (Indía y Andorra)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                     
                    
                }
                
            }
        }
    ),
    
   dcc.Graph(
        id="qatar_burundi",
        figure={
            'data': [
                {'x': fechas_india[:-1], 'y': confirmados_qatar[:-1], 'type': 'line', 'name': 'Confirmados Qatar'},
                {'x': fechas_india[:-1], 'y': muertes_qatar[:-1], 'type': 'line', 'name': 'Muertes Qatar'},
                {'x': fechas_andorra[:-1], 'y': confirmados_burundi[:-1], 'type': 'line', 'name': 'Confirmados Burundi'},
                {'x': fechas_andorra[:-1], 'y': muertes_burundi[:-1], 'type': 'line', 'name': 'Muertes Burundi'},
                
            ],
            'layout': {
                'title': 'Análisis de dos de los países catalogados como el más rico (Qatar) y el más pobre (Burundi)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto'],
                    "size" : 15
                }
            }
        }
    ),
    
     dcc.Graph(
         
        id="comp2",
        figure={
            'data': [
                {'y': total_confirmados_qatar, 'type': 'bar', 'name': 'Confirmados Qatar'},
                {'y': total_confirmados_burundi, 'type': 'bar', 'name': 'Confirmados Burundi'},  
                {'y': total_muertes_qatar, 'type': 'bar', 'name': 'Muertes Qatar'},
                {'y': total_muertes_burundi, 'type': 'bar', 'name': 'Muertes Burundi'},  
            ],
            'layout': {
                'title': 'Comparativo casos confirmados y muertes Qatar y Burundi',
                'plot_bgcolor': colors['fondo'],
                "height" : "25%", 
                "width" : "100%",
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    
     dcc.Graph(
         
        id="Estadisticos2",
        figure={
            'data': [
                {'y':  desvest_qatar_c, 'type': 'bar', 'name': 'DESVEST_qatar_CONFIRMADOS'},
                {'y':  desvest_burundi_c, 'type': 'bar', 'name': 'DESVEST_burundi_CONFIRMADOS'},
                {'y':  desvest_qatar_m, 'type': 'bar', 'name': 'DESVEST_qatar_MUERTES'},  
                {'y':  desvest_burundi_m, 'type': 'bar', 'name': 'DESVEST_burundi_MUERTES'}, 
                {'y':  mediana_qatar_c, 'type': 'bar', 'name': 'MEDIANA_qatar_CONFIRMADOS'},
                {'y':  mediana_burundi_c, 'type': 'bar', 'name': 'MEDIANA_burundi_CONFIRMADOS'},
                {'y':  mediana_qatar_m, 'type': 'bar', 'name': 'MEDIANA_qatar_MUERTES'},
                {'y':  mediana_burundi_m, 'type': 'bar', 'name': 'MEDIANA_burundi_MUERTES'},
                {'y':  media_qatar_c, 'type': 'bar', 'name': 'MEDIA_qatar_CONFIRMADOS'},
                {'y':  media_burundi_c, 'type': 'bar', 'name': 'MEDIA_burundi_CONFIRMADOS'},
                {'y':  media_qatar_m, 'type': 'bar', 'name': 'MEDIA_qatar_MUERTES'},
                {'y':  media_burundi_m, 'type': 'bar', 'name': 'MEDIA_burundi_MUERTES'},
               
                
            ],
            'layout': {
                'title': 'Comparativo estadístico (Qatar y Burundi)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    
        
     dcc.Graph(
        id='pie_qatar_burundi',
        figure={
            'data': [{
                'values': values_qatar_burundi,
                'labels': labels_qatar_burundi,
                'type': 'pie'
            }],
            'layout': {
                'title': 'Porcentaje casos confirmados y muertes (Qatar y Burundi)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                     
                    
                }
                
            }
        }
    ),
    
    dcc.Graph(
        id="nigeria_monaco",
        figure={
            'data': [
                {'x': fechas_india[:-1], 'y': confirmados_nigeria[:-1], 'type': 'line', 'name': 'Confirmados nigeria'},
                {'x': fechas_india[:-1], 'y': muertes_nigeria[:-1], 'type': 'line', 'name': 'Muertes nigeria'},
                {'x': fechas_andorra[:-1], 'y': confirmados_monaco[:-1], 'type': 'line', 'name': 'Confirmados monaco'},
                {'x': fechas_andorra[:-1], 'y': muertes_monaco[:-1], 'type': 'line', 'name': 'Muertes monaco'},
                
            ],
            'layout': {
                'title': 'Análisis de dos de los países catalogados como el más jóven (Nigeria) y el más viejo (Monaco)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto'],
                    "size" : 15
                }
            }
        }
    ),
    
     dcc.Graph(
         
        id="comp3",
        figure={
            'data': [
                {'y': total_confirmados_nigeria, 'type': 'bar', 'name': 'Confirmados nigeria'},
                {'y': total_confirmados_monaco, 'type': 'bar', 'name': 'Confirmados monaco'},  
                {'y': total_muertes_nigeria, 'type': 'bar', 'name': 'Muertes nigeria'},
                {'y': total_muertes_monaco, 'type': 'bar', 'name': 'Muertes monaco'},  
            ],
            'layout': {
                'title': 'Comparativo casos confirmados y muertes Nigeria y Monaco',
                'plot_bgcolor': colors['fondo'],
                "height" : "25%", 
                "width" : "100%",
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    
     dcc.Graph(
         
        id="Estadisticos3",
        figure={
            'data': [
                {'y':  desvest_nigeria_c, 'type': 'bar', 'name': 'DESVEST_nigeria_CONFIRMADOS'},
                {'y':  desvest_monaco_c, 'type': 'bar', 'name': 'DESVEST_monaco_CONFIRMADOS'},
                {'y':  desvest_nigeria_m, 'type': 'bar', 'name': 'DESVEST_nigeria_MUERTES'},  
                {'y':  desvest_monaco_m, 'type': 'bar', 'name': 'DESVEST_monaco_MUERTES'}, 
                {'y':  mediana_nigeria_c, 'type': 'bar', 'name': 'MEDIANA_nigeria_CONFIRMADOS'},
                {'y':  mediana_monaco_c, 'type': 'bar', 'name': 'MEDIANA_monaco_CONFIRMADOS'},
                {'y':  mediana_nigeria_m, 'type': 'bar', 'name': 'MEDIANA_nigeria_MUERTES'},
                {'y':  mediana_monaco_m, 'type': 'bar', 'name': 'MEDIANA_monaco_MUERTES'},
                {'y':  media_nigeria_c, 'type': 'bar', 'name': 'MEDIA_nigeria_CONFIRMADOS'},
                {'y':  media_monaco_c, 'type': 'bar', 'name': 'MEDIA_monaco_CONFIRMADOS'},
                {'y':  media_nigeria_m, 'type': 'bar', 'name': 'MEDIA_nigeria_MUERTES'},
                {'y':  media_monaco_m, 'type': 'bar', 'name': 'MEDIA_monaco_MUERTES'},
               
                
            ],
            'layout': {
                'title': 'Comparativo estadístico (Nigeria y Monaco)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
            
     dcc.Graph(
        id='pie_nigeria_monaco',
        figure={
            'data': [{
                'values': values_nigeria_monaco,
                'labels': labels_nigeria_monaco,
                'type': 'pie'
            }],
            'layout': {
                'title': 'Porcentaje casos confirmados y muertes (Nigeria y Monaco)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                     
                    
                }
                
            }
        }
    ),
    
    dcc.Graph(
        id="ukraine_oman",
        figure={
            'data': [
                {'x': fechas_india[:-1], 'y': confirmados_ukraine[:-1], 'type': 'line', 'name': 'Confirmados ukraine'},
                {'x': fechas_india[:-1], 'y': muertes_ukraine[:-1], 'type': 'line', 'name': 'Muertes ukraine'},
                {'x': fechas_andorra[:-1], 'y': confirmados_oman[:-1], 'type': 'line', 'name': 'Confirmados oman'},
                {'x': fechas_andorra[:-1], 'y': muertes_oman[:-1], 'type': 'line', 'name': 'Muertes oman'},
                
            ],
            'layout': {
                'title': 'Análisis de dos de los países con más mujeres (Ucrania) y con más hombres (Oman)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto'],
                    "size" : 15
                }
            }
        }
    ),
    
     dcc.Graph(
         
        id="comp4",
        figure={
            'data': [
                {'y': total_confirmados_ukraine, 'type': 'bar', 'name': 'Confirmados ukraine'},
                {'y': total_confirmados_oman, 'type': 'bar', 'name': 'Confirmados oman'},  
                {'y': total_muertes_ukraine, 'type': 'bar', 'name': 'Muertes ukraine'},
                {'y': total_muertes_oman, 'type': 'bar', 'name': 'Muertes oman'},  
            ],
            'layout': {
                'title': 'Comparativo casos confirmados y muertes Ucrania y Oman',
                'plot_bgcolor': colors['fondo'],
                "height" : "25%", 
                "width" : "100%",
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    
     dcc.Graph(
         
        id="Estadisticos4",
        figure={
            'data': [
                {'y':  desvest_ukraine_c, 'type': 'bar', 'name': 'DESVEST_ukraine_CONFIRMADOS'},
                {'y':  desvest_oman_c, 'type': 'bar', 'name': 'DESVEST_oman_CONFIRMADOS'},
                {'y':  desvest_ukraine_m, 'type': 'bar', 'name': 'DESVEST_ukraine_MUERTES'},  
                {'y':  desvest_oman_m, 'type': 'bar', 'name': 'DESVEST_oman_MUERTES'}, 
                {'y':  mediana_ukraine_c, 'type': 'bar', 'name': 'MEDIANA_ukraine_CONFIRMADOS'},
                {'y':  mediana_oman_c, 'type': 'bar', 'name': 'MEDIANA_oman_CONFIRMADOS'},
                {'y':  mediana_ukraine_m, 'type': 'bar', 'name': 'MEDIANA_ukraine_MUERTES'},
                {'y':  mediana_oman_m, 'type': 'bar', 'name': 'MEDIANA_oman_MUERTES'},
                {'y':  media_ukraine_c, 'type': 'bar', 'name': 'MEDIA_ukraine_CONFIRMADOS'},
                {'y':  media_oman_c, 'type': 'bar', 'name': 'MEDIA_oman_CONFIRMADOS'},
                {'y':  media_ukraine_m, 'type': 'bar', 'name': 'MEDIA_ukraine_MUERTES'},
                {'y':  media_oman_m, 'type': 'bar', 'name': 'MEDIA_oman_MUERTES'},
               
                
            ],
            'layout': {
                'title': 'Comparativo estadístico (Ucrania y Oman)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    
    dcc.Graph(
        
        id='pie_ucrania_oman',
        figure={
            'data': [{
                'values': values_ukraine_oman,
                'labels': labels_ukraine_oman,
                'type': 'pie'
            }],
            'layout': {
                'title': 'Porcentaje casos confirmados y muertes (Ucrania y Oman)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                     
                    
                }
                
            }
        }
    ),
    
    dcc.Graph(
        id="russia_angola",
        figure={
            'data': [
                {'x': fechas_india[:-1], 'y': confirmados_russia[:-1], 'type': 'line', 'name': 'Confirmados russia'},
                {'x': fechas_india[:-1], 'y': muertes_russia[:-1], 'type': 'line', 'name': 'Muertes russia'},
                {'x': fechas_andorra[:-1], 'y': confirmados_angola[:-1], 'type': 'line', 'name': 'Confirmados angola'},
                {'x': fechas_andorra[:-1], 'y': muertes_angola[:-1], 'type': 'line', 'name': 'Muertes angola'},
                
            ],
            'layout': {
                'title': 'Análisis de dos de los países catalogados con mayor número de personas con piel blanca (Rusia) y de color(Angola)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto'],
                    "size" : 15
                }
            }
        }
    ),
    
     dcc.Graph(
         
        id="comp5",
        figure={
            'data': [
                {'y': total_confirmados_russia, 'type': 'bar', 'name': 'Confirmados russia'},
                {'y': total_confirmados_angola, 'type': 'bar', 'name': 'Confirmados angola'},  
                {'y': total_muertes_russia, 'type': 'bar', 'name': 'Muertes russia'},
                {'y': total_muertes_angola, 'type': 'bar', 'name': 'Muertes angola'},  
            ],
            'layout': {
                'title': 'Comparativo casos confirmados y muertes Rusia y Angola',
                'plot_bgcolor': colors['fondo'],
                "height" : "25%", 
                "width" : "100%",
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
    ),
    
     dcc.Graph(
         
        id="Estadisticos5",
        figure={
            'data': [
                {'y':  desvest_russia_c, 'type': 'bar', 'name': 'DESVEST_russia_CONFIRMADOS'},
                {'y':  desvest_angola_c, 'type': 'bar', 'name': 'DESVEST_angola_CONFIRMADOS'},
                {'y':  desvest_russia_m, 'type': 'bar', 'name': 'DESVEST_russia_MUERTES'},  
                {'y':  desvest_angola_m, 'type': 'bar', 'name': 'DESVEST_angola_MUERTES'}, 
                {'y':  mediana_russia_c, 'type': 'bar', 'name': 'MEDIANA_russia_CONFIRMADOS'},
                {'y':  mediana_angola_c, 'type': 'bar', 'name': 'MEDIANA_angola_CONFIRMADOS'},
                {'y':  mediana_russia_m, 'type': 'bar', 'name': 'MEDIANA_russia_MUERTES'},
                {'y':  mediana_angola_m, 'type': 'bar', 'name': 'MEDIANA_angola_MUERTES'},
                {'y':  media_russia_c, 'type': 'bar', 'name': 'MEDIA_russia_CONFIRMADOS'},
                {'y':  media_angola_c, 'type': 'bar', 'name': 'MEDIA_angola_CONFIRMADOS'},
                {'y':  media_russia_m, 'type': 'bar', 'name': 'MEDIA_russia_MUERTES'},
                {'y':  media_angola_m, 'type': 'bar', 'name': 'MEDIA_angola_MUERTES'},
               
                
            ],
            'layout': {
                'title': 'Comparativo estadístico (Rusia y Angola)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                }
            }
        }
         
     ),
         
      dcc.Graph(
        id='pie_rusia_angola',
        figure={
            'data': [{
                'values': values_rusia_angola,
                'labels': labels_rusia_angola,
                'type': 'pie'
            }],
            'layout': {
                'title': 'Porcentaje casos confirmados y muertes (Rusia y Angola)',
                'plot_bgcolor': colors['fondo'],
                'paper_bgcolor': colors['fondo'],
                'font': {
                    'color': colors['texto']
                     
                    
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