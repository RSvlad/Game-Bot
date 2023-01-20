import os
import dxcam
import predict
import game_control
from PIL import Image
from keras.models import model_from_json


def main():
    model_file1 = open('Data/Model/model.json', 'r')
    model1 = model_file1.read()
    model_file1.close()
    model1 = model_from_json(model1)
    model1.load_weights("Data/Model/weights.h5")


camera = dxcam.create()
model_file = open('Data/Model/model.json', 'r')
model = model_file.read()
model_file.close()
model = model_from_json(model)
model.load_weights("Data/Model/weights.h5")

print('AI start now!')
while True:
    screen = camera.grab()
    Y = model.predict(screen)
    if Y != [0, 0, 0, 0]:
        # Keyboard
        if Y[0] == 0:
            key = get_key(Y[2])
            if Y[1] == 1:
                press(key)
            else:
                release(key)
        # Mouse
        elif Y[0] == 1:
            if Y[3] == 1:
                click(Y[1], Y[2])
            elif Y[3] == 0:
                position(Y[1], Y[2])
    else:
        continue
