import os 
import zipfile 
import tensorflow as tf 
from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras import layers 
from tensorflow.keras import Model 
from tensorflow.keras.applications.vgg16 import VGG16
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

base_dir = 'datasets'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# Directory with our training bags pictures
train_bags_dir = os.path.join(train_dir, 'bags')

# Directory with our training dog pictures
train_cups_dir= os.path.join(train_dir, 'cups')

train_mugs_dir = os.path.join(train_dir, 'mugs')

train_jars_dir = os.path.join(train_dir, 'jars')

train_beedsheets_dir = os.path.join(train_dir, 'bedsheets')

# Directory with our validationing bags pictures
validation_bags_dir = os.path.join(validation_dir, 'bags')

# Directory with our validationing dog pictures
validation_cups_dir= os.path.join(validation_dir, 'cups')

validation_mugs_dir = os.path.join(validation_dir, 'mugs')

validation_jars_dir = os.path.join(validation_dir, 'jars')

validation_beedsheets_dir = os.path.join(validation_dir, 'bedsheets')


# Add our data-augmentation parameters to ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255.,rotation_range = 40, width_shift_range = 0.2, height_shift_range = 0.2, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)

# Note that the validation data should not be augmented!
test_datagen = ImageDataGenerator( rescale = 1.0/255. )


# Flow training images in batches of 20 using train_datagen generator
train_generator = train_datagen.flow_from_directory(train_dir, batch_size = 20, class_mode = 'categorical_crossentropy', target_size = (224, 224))

# Flow validation images in batches of 20 using test_datagen generator
validation_generator = test_datagen.flow_from_directory( validation_dir,  batch_size = 20, class_mode = 'categorical_crossentropy', target_size = (224, 224))




base_model = VGG16(input_shape = (224, 224, 3), # Shape of our images
include_top = False, # Leave out the last fully connected layer
weights = 'imagenet')

for layer in base_model.layers:
    layer.trainable = False

# Flatten the output layer to 1 dimension
x = layers.Flatten()(base_model.output)

# Add a fully connected layer with 512 hidden units and ReLU activation
x = layers.Dense(512, activation='relu')(x)

# Add a dropout rate of 0.5
x = layers.Dropout(0.5)(x)

# Add a final sigmoid layer with 1 node for classification output
x = layers.Dense(1, activation='sigmoid')(x)

model = tf.keras.models.Model(base_model.input, x)

model.compile(optimizer = tf.keras.optimizers.RMSprop(lr=0.0001), loss = 'binary_crossentropy',metrics = ['acc'])


vgghist = model.fit(train_generator, validation_data = validation_generator, steps_per_epoch = 100, epochs = 10)

# Saving the model
model_json = model.to_json()
with open("model.json", "w") as json_file:
	json_file.write(model_json)


model.save_weights('model.h5')
model.save('test.model')


print(vgghist.history.keys())

