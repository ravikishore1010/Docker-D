from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:RaVv%51996@db-instance-rk.cfoogwy0q7ui.ap-south-1.rds.amazonaws.com:5432/mydb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.String(100), nullable=False)

@app.route("/store", methods=["POST"])
def store_data():
    data = request.json
    new_data = Data(key=data["key"], value=data["value"])
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message": "Data stored successfully"})

@app.route("/recall", methods=["GET"])
def recall_data():
    key = request.args.get("key")
    data = Data.query.filter_by(key=key).first()
    if data:
        return jsonify({"value": data.value})
    return jsonify({"message": "Data not found"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)