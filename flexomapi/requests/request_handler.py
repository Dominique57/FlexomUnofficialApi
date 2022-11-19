from enum import Enum
from typing import Callable, Any
import json
from pydantic import parse_obj_as, ValidationError
import requests


request_t = Callable[[], requests.Response]
authenticate_t = Callable[[], None]


class RequestHandler:

    class Error(Enum):
        NO_ERROR = 0
        HTTP_CODE = 1
        JSON_DECODE = 2
        DTO_CONVERSION_TYPE = 3

    request: request_t
    authenticate: authenticate_t
    result_class: Any

    def __init__(self, request: request_t, authenticate: authenticate_t, result_class: Any):
        """
        :param request: function that sends the request and returns a response
        :param authenticate: function to re-authenticate
        :param result_class: class in whom the request will be converted to
        """
        self.request = request
        self.authenticate = authenticate
        self.result_class = result_class

    def handle(self) -> (Error, Any):
        """
        Handles a requests.Response object with re-authentication and dto conversion
        :return: Error or Value
        """
        # Step 1, try and auth + retry on 401
        response = self.request()
        if response.status_code == 401:
            self.authenticate()
            response = self.request()

        # Step 2, error on other invalid http verbs
        if not response.ok:
            return self.Error.HTTP_CODE, None

        # Step 3, try to convert response to class
        try:
            json_data = json.JSONDecoder().decode(response.content.decode('utf-8'))
            result = parse_obj_as(self.result_class, json_data)
        except ValidationError:
            return self.Error.DTO_CONVERSION_TYPE, None
        except ValueError:
            return self.Error.JSON_DECODE, None

        # Finished
        return self.Error.NO_ERROR, result

    def handle_or_throw(self) -> Any:
        """
        Handles a requests.Response object with re-authentication and dto conversion
        @return: DTO and throw exception on any error
        """
        err, val = self.handle()
        if err != RequestHandler.Error.NO_ERROR:
            raise Exception(f"Failed to fetch dto, err code `{err}`")
        return val
