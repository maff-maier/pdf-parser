import io
import json
from parse import parse
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post('/')
async def upload_file(files: UploadFile = File(...)):
    with files.file as req_file:
        file = io.BytesIO(req_file.read())

    return json.load(parse(file=file))
