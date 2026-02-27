from flask import Flask, render_template,jsonify
import mysql.connector
app = Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
    return "<h1> hello </h1>"

@app.route("/test/json", methods=["GET"])
def testjson():
    user={"name":"John Doe","age":30,"email":"johndoe@example.com"}
    return jsonify(user)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/get-data", methods = ["GET"])
def get_data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="flask_app"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM user_auth")
    data = cursor.fetchall()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)