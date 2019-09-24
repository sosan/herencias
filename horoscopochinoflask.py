"""
HOROSCOPO CHINO FLASK

"""

from flask import Flask, request, make_response, redirect, render_template, session, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp, InputRequired  # se puede modificar a nuestro gusto
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
import logging

app = Flask(__name__)

app.config["SECRET_KEY"] = "clave"  # encriptacion con clave


class FormularioChino(FlaskForm):
    # variables globales
    ano = StringField("Introduce tu Año Nacimiento:", validators=[DataRequired(), Length(4, 5)])
    botonEnviar = SubmitField("Enviar")


@app.route("/", methods=["GET", "POST"])
def inicio():
    form = FormularioChino()

    context = {
        "formulario": form

    }
    return render_template("inicio.html", datos=context)


@app.route("/resultado", methods=["POST"])
def resultado():
    if (request.method == "POST"):
        pass
    else:
        return render_template("inicio.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 80, debug=True)
