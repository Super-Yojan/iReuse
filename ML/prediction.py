import cv2
import tensorflow as tf
from flask import Flask , request
from flask_cors import cross_origin, CORS
import sqlite3

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}



CATEGORIES = ["bags", "bedsheets", "bottles", "cups", "jars",
	      "mugs", "paper"]


def prepare(file):
    IMG_SIZE = 50
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


def get_options(item):
    db = sqlite3.connect('../webCrawl/site_crawl.db')
    cursor = db.cursor()
    query = "select * from indexes where Item = '%s'"%item

    cursor.execute(query) 
    data = cursor.fetchall()
    for i in data:
        print(i)

@app.route("/uploadfile", methods=["POST"])
@cross_origin()
def create_upload_file():
    file = request.files['file']
    file.save(file.filename)
    model = tf.keras.models.load_model("CNN.model")
    image = file.filename #your image path
    prediction = model.predict(prepare(image))
    prediction = list(prediction[0])
    ret = CATEGORIES[prediction.index(max(prediction))]
    get_options(ret)
    print(ret)
    return {"prediction" : ret}



if __name__ == '__main__':
   app.run(debug=True)
