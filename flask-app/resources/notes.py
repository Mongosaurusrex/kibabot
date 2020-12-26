from flask import Response, request
from database.models import Note
from flask_restful import Resource


class NotesApi(Resource):
    def get(self):
        notes = Note.objects().to_json()
        return Response(notes, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        note = Note(**body).save()
        id = note.id
        return {'id': str(id)}, 200
    
class NoteApi(Resource):
    def get(self, id):
        note = Note.objects.get(id=id).to_json()
        return Response(note, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Note.objects.get(id=id).update(**body)
        return '', 200


    def delete(self, id):
        Note.objects.get(id=id).delete()
        return '', 200
        