from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {
        'id':1,
        'name':"idk",
        'number':"57238752"
    }
]

@app.route("/")
def home():
    return "Contacts"

@app.route("/add-contact", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide a data!"
        },400)

    contact={
        "id":data[-1]['id']+1,
        'name': request.json['name'],
        'number': request.json['number']
    }
    data.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added succesfully!"
    })

@app.route("/contacts")
def show():
    return jsonify({
        "contacts":data
    })
if(__name__=="__main__"):
    app.run(debug=True)