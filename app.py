import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model("mnist_model.h5")
img = Image.open("number.png").convert("L")
img = img.resize((28, 28))
img_array = np.array(img).reshape(-1, 784) / 255.0
prediction = model.predict(img_array)
print(np.squeeze(prediction))
print(f"予測した数字：{np.argmax(prediction)}")
