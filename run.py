from flask import Flask, render_template, request, redirect,url_for
from forms import IndexForm
from data import DataList, Hecho, DataWeb
from red import Red
import numpy
import pandas as pd

app=Flask(__name__)

app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

RUTA_LISTA_ESPECIALIDADES="./resources/caracteristicas-RN.csv"
RUTA_KERAS="./resources/back_red.keras"

model= Red(RUTA_KERAS)

@app.before_request
def before_request():
    print("Antes de la petición ....")

@app.after_request
def after_request(response):
    print("Despues de la petición ....")
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    form = IndexForm()
    datal = DataList(RUTA_LISTA_ESPECIALIDADES)
    form.especialidad.choices= datal.GetList()
    
    if  form.validate_on_submit():
        dataweb=DataWeb(form.especialidad.data,
            form.edad.data,                 # Es el valor de la edad
            form.desempleado.data,           # Desempleado / ocupado
            form.desempleado.data,
            form.hombre.data,               # Hombre / mujer
            form.hombre.data, 
            form.especialidadrequerida.data,  #Especialidad requerida
            form.discapacidad.data,  #Discapacdad
            form.pld.data, #Pld
            form.titulacion.data,  #Titulacion
            form.orientacion.data,  #orientacion
            form.bajacualificacion.data,  #bajaCualificacion
            form.rsb.data,  #rsb
            form.cobraprestacion.data,  #cobraPrestacion
            form.hacursadoaf.data,  #haCursadoAf
            form.hasuperadoaf.data)  #haSuperadoAf)
        
        hecho = Hecho(dataweb.GetEspecialidad(), # Se prueba la formación propuesta
                     dataweb.GetEdad(),
                     dataweb.GetDesempleado(),
                     dataweb.GetOcupado(),
                     dataweb.GetHombre(),
                     dataweb.GetMujer(),
                     dataweb.GetEspecialidadRequerida(),
                     dataweb.GetDiscapacidad(),
                     dataweb.GetPld(),
                     dataweb.GetTitulacion(),
                     dataweb.GetOrientacion(),
                     dataweb.GetBajaCualificacion(),
                     dataweb.GetRsb(),
                     dataweb.GetCobraPrestacion(),
                     dataweb.GetHaCursadoAf(),
                     dataweb.GetHaSuperadoAf())  
        
        casos = model.GenerarCasos(dataweb.GetEdad(), # Se generan todos los casos posibles del perfil
                     dataweb.GetDesempleado(),
                     dataweb.GetOcupado(),
                     dataweb.GetHombre(),
                     dataweb.GetMujer(),
                     dataweb.GetEspecialidadRequerida(),
                     dataweb.GetDiscapacidad(),
                     dataweb.GetPld(),
                     dataweb.GetTitulacion(),
                     dataweb.GetOrientacion(),
                     dataweb.GetBajaCualificacion(),
                     dataweb.GetRsb(),
                     dataweb.GetCobraPrestacion(),
                     dataweb.GetHaCursadoAf(),
                     dataweb.GetHaSuperadoAf())
        
        prediccion=model.Predict(hecho.GetHecho()) # Se predice la formación propuesta
        scores=model.Predict(casos)                # Se predicen alternativas del perfil
        
        # Se preparan los datos a pasar al formulario

        des_especialidad= datal.GetItem(form.especialidad.data)
        datamodel= pd.DataFrame(scores)
        d=datal.ConcatPrediccion(datamodel)
        res = d.iloc[:,[0,1]]
        res.rename(columns={0: 'pr1'}, inplace=True)
        res['pr1'] = res['pr1'] *100 
        res=res.round({'pr1': 0})
        res=res.query("pr1 >= 90")
        predicciones=res.sort_values('pr1', ascending=False)
        longitud= len(predicciones)

        # Datos a pasar al formulario
        
        data = {'descripcion': des_especialidad,
                'prediccion': numpy.round(prediccion[0,0]*100,2),
                'predicciones': predicciones,
                'longitud': longitud}
        
        return render_template("index_handler.html",data=data, form=form) 
    return render_template("index.html", form=form)

def query_string():
    print (request)
    print(request.args)
    print(request.args.get('param1'))
    return "Ok"

def pagina_noencontrada (error):
    return redirect(url_for('index')) 

if __name__== '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404,pagina_noencontrada)
    app.run(debug=True, port=5000)
