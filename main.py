from flask import Flask

app = Flask(__name__)

@app.route("/")
def ana_adres():
    return '<h1>ana adreste bulunuyorsun!</h1>'
@app.route("/secondpage")
def ikinci_adres():
    return '<h1>ikinci sayfada bulunuyorsun!</h1>'
@app.route("/ADRES")
def ucuncu_adres():

    app.run(debug=True)
