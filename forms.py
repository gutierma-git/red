from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,SelectField,BooleanField,IntegerField,validators
from wtforms.validators import DataRequired, Email, Length

# Clase de formulario de entrada de datos

class IndexForm(FlaskForm):
    especialidad = SelectField('Especialidad formativa de interés',coerce=int)
    edad = IntegerField("Edad",
       [ validators.DataRequired(message = "El campo Edad es es obligatorio"),
        validators.NumberRange(min=16, max =70, message= "La edad debe estar comprendida entre 16 y 70 años")
       ])
    desempleado = BooleanField("Desempleado",  false_values=('False', 'false', ''))
    hombre = BooleanField("Hombre",  false_values=('False', 'false', ''))
    especialidadrequerida = BooleanField("Especialidad en su demanda",  false_values=('False', 'false', ''))
    discapacidad = BooleanField("Discapacidad",  false_values=('False', 'false', ''))
    pld = BooleanField("Parado de larga duración",  false_values=('False', 'false', ''))
    titulacion = BooleanField("Dispone de alguna titulación",  false_values=('False', 'false', ''))
    orientacion = BooleanField("Utiliza servicios de orientación",  false_values=('False', 'false', ''))
    bajacualificacion = BooleanField("Tiene baja cualificacion",  false_values=('False', 'false', ''))
    rsb = BooleanField("Percibe renta social básica",  false_values=('False', 'false', ''))
    cobraprestacion = BooleanField("Percibe prestación por desempleo",  false_values=('False', 'false', ''))
    hacursadoaf = BooleanField("Ha cursado acciones formativas anteriormente",  false_values=('False', 'false', ''))
    hasuperadoaf = BooleanField("Ha superado alguna acción formativa anteriormente",  false_values=('False', 'false', ''))
    submit = SubmitField('Buscar')
    
