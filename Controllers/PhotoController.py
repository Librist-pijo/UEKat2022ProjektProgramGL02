import time
from Services import GenderAgeDetector as gad
from fastapi import APIRouter, UploadFile
import os


photo = APIRouter()

UPLOAD_PATH = 'UploadedFiles/'


@photo.get("/getallfiles")
def get_files():
    try:
        files = os.listdir(UPLOAD_PATH)
        for root, dirs, files in os.walk(UPLOAD_PATH):
            for list in files:
                list=os.path.join(root,list) # joining root and the file name for full path
                file_size = os.path.getsize(list)
                createDate = time.ctime(os.path.getctime(list))
                listOfFiles = list, "Size: %.1f bytes"%file_size, "Created date: " + createDate
    except Exception:
        return {"error": "There was an error reading the files"}
    return files,listOfFiles


@photo.get("/getagegenderfromfile")
def get_gender_age(filename):
    try:
        age, gender = gad.detect(UPLOAD_PATH+filename)
    except Exception:
        return {"error": "There was an error reading the file"}
    return {"message": f"Age: {age},Gender: {gender}"}


@photo.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    try:
        contents = await file.read()
        with open(UPLOAD_PATH+file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"error": "There was an error uploading the file"}
    finally:
        await file.close()
    return {"message": f"Successfuly uploaded {file.filename}"}
