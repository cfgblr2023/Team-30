# from tensorflow.keras import models
from matplotlib import image as mpimg
import numpy as np


def get_result(img_path):
    new_model = models.Sequential()

    new_model = models.load_model("C:\\Users\\Amishraj\\Downloads\\my_model\\my_model")

    print("Done")

    mapping = {0: "Waste", 1: "Footpath Quality",
            2: "Obstruction", 3: "Encroachment", 4: "Unsafe Zone"}

    image = mpimg.imread(img_path)

    input_image = np.resize(np.array(image), (1, 1333, 1333, 3))

    result = new_model.predict(input_image)

    y_pred = mapping[np.argmax(result)[0]]

    return y_pred