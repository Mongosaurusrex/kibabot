from werkzeug.exceptions import HTTPException

class InternalServerError(HTTPException):
    pass

class SchemaValidationError(HTTPException):
    pass

class FetchNoteError(HTTPException):
    pass

class CreatingNoteError(HTTPException):
    pass

class UpdatingNoteError(HTTPException):
    pass

class DeletingNoteError(HTTPException):
    pass

class NoteDoesNotExists(HTTPException):
    pass

class EmailAlreadyExistsError(HTTPException):
    pass

class UnauthorizedError(HTTPException):
    pass

errors = {
    "FetchNoteError": {
        "message": "Something went wrong when trying to fetch the note",
        "status": 500
    },
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500,
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "CreatingNoteError": {
        "message": "Something went wrong when trying to create the note",
        "status": 500
    },
    "UpdatingNoteError": {
        "message": "Something went wrong when trying to update the note",
        "status": 500
    },
    "DeletingNoteError": {
        "message": "Something went wrong when trying to delete the note",
        "status": 500
    },
    "NoteDoesNotExists": {
        "message": "The given note does not exist",
        "status": 404
    },
    "EmailAlreadyExistsError": {
        "message": "User with the given email address already exists",
        "status": 400,
    },
    "WrongCredentialsError": {
        "message": "Invalid username or password",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "You are not authorized to request this resource",
        "status": 401
    }
}