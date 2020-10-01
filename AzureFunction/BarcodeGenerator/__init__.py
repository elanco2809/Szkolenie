import logging
from barcode import EAN13
from barcode.writer import ImageWriter
from io import BytesIO

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    code = req.params.get('code',"").strip()
    if len(code)!=12 or not code.isdigit():
        return func.HttpResponse("Za mało cyfr lub niepoprawne dane", status_code=500)
    
    fd = BytesIO()
    EAN13( code, writer=ImageWriter()).write(fd)
    fd.seek(0)
    return func.HttpResponse(fd.read(-1) , status_code=200, mimetype="image/jpg" )
