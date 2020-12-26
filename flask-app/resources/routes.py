from .notes import NoteApi, NotesApi
from .health import HealthApi
from .auth import SignupApi

def initialize_routes(api):
    api.add_resource(SignupApi, '/auth/signup')

    api.add_resource(HealthApi, '/')

    api.add_resource(NotesApi, '/notes')
    api.add_resource(NoteApi, '/notes/<id>')