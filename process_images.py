from PIL import Image, ImageFilter
import pickle
import os
import numpy as np

data = []

def get_image(image_path, width, height, mode):
    """
    Read image from image_path
    :param image_path: Path of image
    :param width: Width of image
    :param height: Height of image
    :param mode: Mode of image
    :return: Image data
    """
    image = Image.open(image_path)

    return np.array(image.convert(mode))

def get_batch(image_files, width, height, mode):
    data_batch = np.array(
        [get_image(sample_file, width, height, mode) for sample_file in image_files]).astype(np.float32)

    # Make sure the images are in 4 dimensions
    if len(data_batch.shape) < 4:
        data_batch = data_batch.reshape(data_batch.shape + (1,))

    return data_batch

for file in os.listdir(r"c:\Work\new_images\128x128x3"):
    print(file)
    im = Image.open(os.path.join(r"c:\Work\new_images\128x128x3", file))
    im = im.resize((128,128))
    im = im.convert(mode="RGB")
    
    #a = np.reshape(np.array(list([((i/127.5) - 1) for i in im.tobytes()])), (-1, 128))
    #print(a)
    #data.append(a)
    im.save(os.path.join(r"c:\Work\new_images\128x128x3",file))
#with open(os.path.join(r"c:\Work\new_images\128x128x3","data.pkl"), "wb") as file:
#    pickle.dump(np.array(data),file)