import io
from parse import parse, get_filename
from fastapi import FastAPI, File, UploadFile
import json

# def main() -> None:
#     file_name = get_filename()

#     parse(file_name=file_name)

app = FastAPI()

@app.post('/')
async def upload_file(files: UploadFile = File(...)):
    with files.file as req_file:
        file = io.BytesIO(req_file.read())
        filename = files.filename
        
    return json.loads(parse(file=file, filename=filename))


# if __name__ == '__main__':
#     main()
