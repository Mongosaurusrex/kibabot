from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Note
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, DoesNotExist, ValidationError, InvalidQueryError
from utils.errors import SchemaValidationError, FetchNoteError, InternalServerError, UpdatingNoteError, DeletingNoteError, NoteDoesNotExists

class NotesApi(Resource):
    @jwt_required
    def get(self):
        notes = Note.objects().to_json()
        return Response(notes, mimetype="application/json", status=200)
    
    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            note = Note(**body).save()
            id = note.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError
    
class NoteApi(Resource):
    @jwt_required
    def get(self, id):
        try:
            note = Note.objects.get(id=id).to_json()
            return Response(note, mimetype="application/json", status=200)
        except DoesNotExist:
            raise NoteDoesNotExists
        except Exception as e:
            raise FetchNoteError

    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            Note.objects.get(id=id).update(**body)
            return '', 200
        except DoesNotExist:
            raise NoteDoesNotExists
        except Exception as e:
            raise UpdatingNoteError 
    @jwt_required
    def delete(self, id):
        try:
            Note.objects.get(id=id).delete()
            return '', 200
        except DoesNotExist:
            raise NoteDoesNotExists
        except Exception as e:
            raise DeletingNoteError
