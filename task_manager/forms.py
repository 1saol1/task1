from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    title = StringField('Введите название вашей задачи', 
                        validators=[DataRequired('Обязательное поле')])

    
    
    submit = SubmitField('Добавить')
