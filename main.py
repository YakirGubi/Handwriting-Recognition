import numpy as np
from WriteNumber import returnImage
import matplotlib.pyplot as plt
from AI import model

while True:
    image = returnImage()
    input_data = np.array(image)
    plt.imshow(input_data, cmap='gray')
    plt.title('MNIST Digit')
    plt.show()
    reshaped_input = np.reshape(input_data, (1, 28, 28, 1)).astype("float32") / 255
    prediction = model.predict(reshaped_input)
    print(prediction.argmax())
