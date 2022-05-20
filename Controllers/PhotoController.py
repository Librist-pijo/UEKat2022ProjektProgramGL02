from Services import GenderAgeDetectorService as gad, HelperService as hs
from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse


photo = APIRouter()

UPLOAD_PATH = 'UploadedFiles/'


@photo.get("/GetAllUploadedFiles")
def get_uploaded_files():
    try:
        files = hs.os.listdir(UPLOAD_PATH)
    except Exception:
        return {"error": "There was an error reading the files"}
    return files


@photo.get("/GetAllProcessedFiles")
def get_processed_files():
    try:
        files = hs.os.listdir(gad.SAVE_PATH)
    except Exception:
        return {"error": "There was an error reading the files"}
    return files


@photo.get("/DownloadProcessedFile")
def download_processed_file(filename: str):
    try:
        return FileResponse(path=gad.SAVE_PATH+filename, media_type='application/octet-stream', filename=filename)
    except Exception:
        return {"error": "There was an error reading the file"}


@photo.post("/UploadFile")
async def upload_file(file: UploadFile):
    try:
        file_extension = hs.os.path.splitext(file.filename)[1]
        if file_extension.lower() not in {'.jpg', '.jpeg', '.png'}:
            return {"error": "Wrong image file format, please use jpg, jpeg or png"}
        hs.delete_latest(UPLOAD_PATH)
        contents = await file.read()
        with open(UPLOAD_PATH+file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"error": "There was an error uploading the file"}
    finally:
        await file.close()
    return {"message": f"Successfuly uploaded {file.filename}"}


@photo.post("/ProcessFile")
def process_file(filename: str):
    try:
        hs.delete_latest(gad.SAVE_PATH)
        age, gender = gad.detect(UPLOAD_PATH, filename)
    except Exception:
        return {"error": "There was an error reading the file"}
    finally:
        hs.os.remove(UPLOAD_PATH+filename)
    return {"message": f"File processed successfully, detected Age: {age}, Gender: {gender}"}
