from tensorflow.keras import models
from matplotlib import image as mpimg
import numpy as np


def get_result(image):
    new_model = models.Sequential()

    new_model = models.load_model("C:\\Users\\anmol\\Downloads\\saved_model\\my_model")

    print("Done")

    mapping = {0: "Waste", 1: "Footpath Quality",
            2: "Obstruction", 3: "Encroachment", 4: "Unsafe Zone"}


    input_image = np.resize(np.array(image), (1, 1333, 1333, 3))

    result = new_model.predict(input_image)

    y_pred = np.argmax(result)
    y_pred = mapping[int(y_pred)]
    print(y_pred)
    return y_pred