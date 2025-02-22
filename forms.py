from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,RadioField, IntegerField, EmailField
from wtforms import validators

class UserForm(Form):
    matricula = StringField("Matricula",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="El campo debe tener entre 3 y 10 caracteres")
    ])
    nombre = StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
    ])
    
    Apellido = StringField("Apellido")
    email= EmailField("Correo", [
        validators.Email(message="Ingrese un correo valido")
    ])
    
class ZodiacoForm(Form):
    nombre = StringField("nombre",[
        validators.DataRequired(message="El campo es requerido")
    ])
    apaterno = StringField("apaterno",[
        validators.DataRequired(message="El campo es requerido")
    ])
    
    amaterno = StringField("amaterno",[
        validators.DataRequired(message="El campo es requerido")
    ])
    
    dia = IntegerField("dia",[
        validators.DataRequired(message="El campo es requerido"),
        validators.number_range(min=1, max=31)
    ])
    
    mes = IntegerField("mes",[
        validators.DataRequired(message="El campo es requerido"),
        validators.number_range(min=1, max=12)
    ])
    
    anio = IntegerField("anio",[
        validators.DataRequired(message="El campo es requerido")
    ])
    
    sexo = RadioField("Sexo", choices=[
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ], validators=[validators.DataRequired(message="El campo es requerido")])
    