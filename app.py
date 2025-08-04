from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    opcion = None
    if request.method == 'POST':
        opcion = request.form.get('opcion')
    return render_template('index.html', opcion=opcion)

if __name__ == '__main__':
    app.run(debug=True)
