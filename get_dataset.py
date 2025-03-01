import os
import numpy as np
from PIL import Image
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split


def get_img(data_path):
    img1 = Image.open(data_path)
    img = np.asarray(img1)
    return img


def save_img(img, path):
    img.save(path)
    return


def get_dataset(dataset_path='Data/Train_Data'):
    try:
        X = np.load('Data/npy_train_data/X.npy')
        Y = np.load('Data/npy_train_data/Y.npy')
    except:
        labels = os.listdir(dataset_path)
        X = []
        Y = []
        count_category = [-1, '']
        for label in labels:
            datas_path = f"{dataset_path}/{label}"
            for data in os.listdir(datas_path):
                img = get_img(f"{datas_path}/{data}")
                X.append(img)
                if data != count_category[1]:
                    count_category[0] += 1
                    count_category[1] = data.split(',')
                Y.append(count_category[0])
        X = np.array(X).astype('float32') / 255.
        Y = np.array(Y).astype('float32')
        Y = to_categorical(Y, count_category[0] + 1)
        if not os.path.exists('Data/npy_train_data/'):
            os.makedirs('Data/npy_train_data/')
        np.save('Data/npy_train_data/X.npy', X)
        np.save('Data/npy_train_data/Y.npy', Y)
    X, X_test, Y, Y_test = train_test_split(X, Y, test_size=0.1, random_state=1)
    return X, X_test, Y, Y_test
