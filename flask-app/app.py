from flask import Flask, jsonify, request, Response
from datetime import datetime

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

notes = [
    {
        "id": 1,
        "created": datetime.now().isoformat(),
        "whom": "Nathan",
        "poop": 3,
        "barked": True,
        "reasonForBark": "Because the person was black",
        "desc": "Barked at a random person, otherwise good"
    },
    {
        "id": 2,
        "created": datetime.now().isoformat(),
        "whom": "Lovisa",
        "poop": 5,
        "barked": False,
        "reasonForBark": None,
        "desc": "Barked at a random person, otherwise good"
    }
]

@app.route('/')
def health():
    return jsonify({'Health': 'healthy boi'})

@app.route('/notes')
def get_all_notes():
    return jsonify(result=notes), 200

@app.route('/notes', methods=['POST'])
def add_note(id):
    note = request.get_json()
    notes.append(note)
    return jsonify(result={ id: len(notes) }), 201

@app.route('/notes/<int:id>', methods=["GET"])
def get_note(id):
    return Response(status=501)

@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    return Response(status=501)

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    return Response(status=501)

if __name__ == "__main__":
    app.run(port=3000)

