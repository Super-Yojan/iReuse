import cv2
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile

CATEGORIES = ["bags", "bedsheets", "bottles", "cups", "jars",
	      "mugs", "paper"]

app = FastAPI()

def prepare(file):
    IMG_SIZE = 50
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    model = tf.keras.models.load_model("CNN.model")
    image = file.filename #your image path
    with open(file.filename, 'wb+')as f:
        f.write(file.file.read())
    prediction = model.predict(prepare(image))
    prediction = list(prediction[0])
    ret = CATEGORIES[prediction.index(max(prediction))]
    return {"prediction" : ret}




