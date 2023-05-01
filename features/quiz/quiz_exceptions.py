from werkzeug.exceptions import HTTPException, BadRequest
from ...app import app

# @app.errorhandler(BadRequest)
# def handle_bad_request(e):
#     return 'bad request!', 400


class InvalidQuizException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)


class MinimumLengthException(InvalidQuizException):
    pass

class NoLowerCaseException(InvalidQuizException):
    pass
