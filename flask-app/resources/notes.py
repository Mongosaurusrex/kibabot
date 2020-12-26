from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Note
from flask_restful import Resource


class NotesApi(Resource):
    @jwt_required
    def get(self):
        notes = Note.objects().to_json()
        return Response(notes, mimetype="application/json", status=200)
    
    @jwt_required
    def post(self):
        body = request.get_json()
        note = Note(**body).save()
        id = note.id
        return {'id': str(id)}, 200
    
class NoteApi(Resource):
    @jwt_required
    def get(self, id):
        note = Note.objects.get(id=id).to_json()
        return Response(note, mimetype="application/json", status=200)

    @jwt_required
    def put(self, id):
        body = request.get_json()
        Note.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        Note.objects.get(id=id).delete()
        return '', 200
