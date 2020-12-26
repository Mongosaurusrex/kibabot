from flask import Flask, jsonify, request, Response
from datetime import datetime
from database.db import initialize_db
from database.models import Note
from utils.settings import MONGODB_CONNECTION_STRING

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['MONGODB_SETTINGS'] = {
    'host': MONGODB_CONNECTION_STRING
}

initialize_db(app)
 
@app.route('/')
def health():
    return jsonify({'Health': 'healthy boi'})

@app.route('/notes')
def get_all_notes():
    notes = Note.objects().to_json()
    return Response(notes, mimetype="application/json", status=200)

@app.route('/notes', methods=['POST'])
def add_note():
    body = request.get_json()
    note = Note(**body).save()
    id = note.id
    return {'id': str(id)}, 200
    

@app.route('/notes/<id>', methods=["GET"])
def get_note(id):
    note = Note.objects.get(id=id).to_json()
    return Response(note, mimetype="application/json", status=200)

@app.route('/notes/<id>', methods=['PUT'])
def update_note(id):
    body = request.get_json()
    Note.objects.get(id=id).update(**body)
    return '', 200

@app.route('/notes/<id>', methods=['DELETE'])
def delete_note(id):
    Note.objects.get(id=id).delete()
    return '', 200

if __name__ == "__main__":
    app.run(port=3000)

