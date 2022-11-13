from pydantic import parse_obj_as
import json
import requests


def handle_res_throw(res: requests.Response, result_class):
    """
    Handle request response and convert to class and raise an Exception if response is not 2XX.
    @param res: Request response to handle / convert.
    @param result_class: Class that the response will be converted to.
    @return: An instance of "result_class".
    """
    if not 200 <= res.status_code < 300:
        msg = f'Response handling error : {res.url} with code {res.status_code}\n`{res.content}`'
        raise Exception(msg)

    json_data = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(result_class, json_data)
