from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-secret"  # necesario para flash

USUARIOS = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/procesar", methods=["POST"])
def procesar():
    nombre = request.form.get("nombre", "").strip()
    edad = request.form.get("edad", "").strip()

    if not nombre or not edad.isdigit():
        flash(("error", "Completá nombre y edad válidos."))
        return redirect(url_for("formulario"))

    USUARIOS.append({"nombre": nombre, "edad": int(edad)})
    flash(("success", f"Se registró a {nombre} correctamente."))
    return redirect(url_for("lista"))

@app.route("/lista")
def lista():
    return render_template("lista.html", usuarios=USUARIOS)

if __name__ == "__main__":
    app.run(debug=True)
