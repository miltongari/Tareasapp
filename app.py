from flask import Flask, request, render_template, redirect

tareas = []


app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods = ["GET", "POST"])
def agregar():
    if request.method == "GET":
        return render_template('agregar.html')
    else:
        tarea = request.form.get("tarea")
        tareas.append(tarea)
        return redirect("/agregar")




if __name__ == "__main__":
    app.run(debug=True)
