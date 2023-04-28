from fastapi import FastAPI, BackgroundTasks, UploadFile, File, HTTPException
from pydantic import BaseModel, validator 
import tensorflow as tf 
import shutil
import os
from image_model import make_predictions

app = FastAPI() 



class ImageModel(BaseModel):
    image: str
    prediction: str
    
    
    
@app.get("/")
def health_check():
    return {"status": "OK"}


# @app.post("/upload")
# async def image_prediction(image: UploadFile = File(...)):
#     "File should be an image file"
#     img = await image.read()
    
#     with open(f"saved_files/{image.filename}", "wb") as f:
#         f.write(img)
        
#     return {"Filename" : image.filename}
        


@app.post("/upload_new")
async def image_upload(im: UploadFile = File(...)):
    if im.content_type not in ["image/png", "image/jpeg", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Uploaded file should be an image file")
        
    else:
        with open(f"images_files/{im.filename}", "wb") as f:
            shutil.copyfileobj(im.file, f)
    
            
    return {"Filename": im.filename}


    
@app.get("/result")
def get_prediction():
    y_hat = make_predictions()
    return {"Prediction": y_hat}
    