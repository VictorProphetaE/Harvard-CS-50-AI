import cv2
import numpy as np
import os
import sys
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf
import os.path

from os.path import join , exists
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images = []
    labels = []
    #check if the folder exist
    if exists(data_dir):
        #generates the file names in a directory tree by walking the tree
        for root, _, files in os.walk(data_dir):
            for file in files:
                #abs_path = os.path.join(root, file)
                img_path = join(root, file)
                #read de image and resize to the specification size
                img = cv2.imread(img_path)
                img = cv2.resize(img, (IMG_WIDTH,IMG_HEIGHT) )
                
                images.append(img)
                #get the base name of pathname path
                labels.append(int(os.path.basename(root)))
    return (images, labels)

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = Sequential()
    """
    With "SAME" padding, if you use a stride of 1, the layer's outputs will have the same spatial dimensions as its inputs.
    With "VALID" padding, there's no "made-up" padding inputs. The layer only uses valid input data.

    """
    #add 2 layers one with 32 filters, other with 64, with padding same
    model.add(Conv2D(filters=32, kernel_size=(3,3), padding='same', activation='relu', 
                            input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Conv2D(filters=64, kernel_size=(3,3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    #add Dense Hidden layer of 256 and a dropout of 0.5
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CATEGORIES, activation='softmax'))
    
    #model.summary()
    
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    return model


if __name__ == "__main__":
    main()
