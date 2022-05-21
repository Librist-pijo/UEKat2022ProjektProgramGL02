import uvicorn
from fastapi import FastAPI
from Controllers import PhotoController


app = FastAPI()
app.include_router(PhotoController.photo)

# if __name__ == '__main__':
#     uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
