import logging
import random
import string
import time
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Start function...')
    
    random.seed(time.time())

    n = req.params.get('n',"")
    try:
        n = int(n)
        if n<6:
            raise ValueError("length too short")
    except Exception as exc:
        logging.exception(str(exc), exc_info=True)
        return func.HttpResponse(str(exc), status_code=500)

    password = ""
    s = string.printable
    for x in range(n):
        index = random.randint(0, len(s)-1)
        password += s[index]
    result = { "password" : password }
    return func.HttpResponse( json.dumps(result), status_code=200, mimetype="application/json" )
