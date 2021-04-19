
import requests
import datetime

r = requests.get("https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=casos-asociados-a-covid-19&q=&rows=237&facet=fecha_actualizacion&facet=id_registro&facet=origen&facet=sector&facet=entidad_um&facet=sexo&facet=entidad_nac&facet=entidad_res&facet=municipio_res&facet=tipo_paciente&facet=fecha_ingreso&facet=fecha_def&facet=edad&facet=nacionalidad&facet=embarazo&facet=habla_lengua_indi&facet=diabetes&facet=epoc&facet=asma&facet=inmusupr&facet=hipertension&facet=cardiovascular&facet=obesidad&facet=renal_cronica&facet=tabaquismo&facet=negativo&facet=migrante&facet=pais_nacionalidad&facet=rango_edad&facet=positivo&facet=pendiente")

datos = r.json()

fecha_ingreso = []
edad = []
positivo = []
negativo = []
fecha_def = []
inmusupr = []
entidad_res = []
tipo_paciente = []
cardiovascular = []
neumonia = []
hipertension = []
otra_com = []
epoc = []
asma = []
fecha_sintomas = []
nacionalidad = []
pais_origen = []
rango_edad = []
embarazo = []
municipio_res = []
sexo = []
obesidad = []
habla_lengua_indi = []
intubado = []
tabaquismo = []
diabetes = []
edad = []
num_hospitalizados = []
pais_nacionalidad = []
migrante = []
entidad_nac = []
otro_caso = []
renal_cronica = []



       
for dato in datos:
    
    fecha_ingreso.append("fecha_ingreso")
    edad.append("edad")
    positivo.append("positivo")
    negativo.append("negativo")
    fecha_def.append("fecha_def")
    inmusupr.append("inmusupr")
    entidad_res.append("entidad_res")
    tipo_paciente.append("tipo_paciente")
    neumonia.append("neumonia")
    hipertension.append("hipertension")
    otra_com.append("otra_com")
    epoc.append("epoc")
    asma.append("asma")
    fecha_sintomas.append("fecha_sintomas")
    nacionalidad.append("nacionalidad")
    pais_origen.append("pais_origen")
    rango_edad.append("rango_edad")
    embarazo.append("embarazo")
    municipio_res.append("municipio_res")
    sexo.append("sexo")
    habla_lengua_indi.append("habla_lengua_indi")
    intubado.append("intubado")
    diabetes.append("diabetes")
    edad.append("edad")
    num_hospitalizados.append("num_hospitalizados")
    pais_nacionalidad.append("pais_nacionalidad")
    migrante.append("migrante")
    entidad_nac.append("entidad_nac")
    otro_caso.append("tabaquismo")
    renal_cronica.append("renal_cronica")

   

  
    



       
       