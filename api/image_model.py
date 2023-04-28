import tensorflow as tf 
import os 
import shutil
import glob



model = tf.keras.models.load_model("./model/cifar10_model.hdf5")



def load_and_prep_image(filename, img_shape=32, scale=True):
  """
  Reads in an image from filename, turns it into a tensor and reshapes into
  (32, 32, 3).
  """
  # Read in the image
  img = tf.io.read_file(filename)
  # Decode it into a tensor
  img = tf.image.decode_jpeg(img)
  # Resize the image
  img = tf.image.resize(img, [img_shape, img_shape])
  if scale:
    # Rescale the image (get all values between 0 and 1)
    return img/255.
  else:
    return img


def make_predictions():
    cifarcls = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    model = tf.keras.models.load_model("model/cifar10_model.hdf5")
    list_of_files = glob.glob("images_files/*")
    latest_file = max(list_of_files, key=os.path.getmtime)
    image_file = load_and_prep_image(latest_file)
    image = tf.expand_dims(image_file, axis=0)
    prediction = model.predict(image)
    pred_class = cifarcls[prediction.argmax()]
    return pred_class
    