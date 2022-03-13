import numpy as np
import tensorflow as tf
from keras.preprocessing import image

CATEGORIES = ["dog","cat"]


test_image = image.load_img('kabir.jpg',  target_size = (224,224))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
model = tf.keras.models.load_model("test.model")
prediction = model.predict(test_image)
print(prediction)
# prediction = list(prediction[0])
# print(CATEGORIES[prediction.index(max(prediction))])
