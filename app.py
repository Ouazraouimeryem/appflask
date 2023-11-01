
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Configuration de la base de données
app.config['DB_HOST'] = 'localhost'
app.config['DB_USER'] = 'root'
app.config['DB_PASSWORD'] = ''
app.config['DB_NAME'] = 'bd'

@app.route('/', methods=['GET', 'POST'])
def formulaire():
    nom = ""
    prenom = ""
    age = ""

    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        age = request.form['age']

        # Établir une connexion à la base de données
        db = pymysql.connect(
            host=app.config['DB_HOST'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASSWORD'],
            database=app.config['DB_NAME']
        )

        # Créer un curseur pour interagir avec la base de données
        cursor = db.cursor()

        # Insérer les données dans la base de données
        insert_query = "INSERT INTO ma_table(nom, prenom, age) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (nom, prenom, age))

        # Valider la transaction et fermer la connexion
        db.commit()
        db.close()
    return render_template('formulaire.html', nom=nom, prenom=prenom, age=age)

if __name__ == '__main__':
    app.run(debug=True)

