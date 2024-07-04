from PIL import Image
import numpy as np
import onnxruntime
import os
import sys

categories = ["blurred", "exposed", "good", "noisy"]
session = onnxruntime.InferenceSession(os.path.join(os.getcwd(), "model_v11_onnx.onnx"))

def preprocess_image(image_path) -> np.array:
    image = Image.open(image_path)
    image = image.resize((512, 512))
    image_data = np.asarray(image).astype(np.float32)
    image_data = image_data.transpose((2, 0, 1))
    mean, std = np.array([0.485, 0.456, 0.406]), np.array([0.229, 0.224, 0.225])
    for channel in range(image_data.shape[0]):
        image_data[channel, :, :] = (image_data[channel, :, :] / 255 - mean[channel]) / std[channel]
    image_data = np.expand_dims(image_data, axis=0)
    return image_data

def run_sample(session, image_path):
    output = session.run([], {"image": preprocess_image(image_path)})[0]
    output = output.flatten()
    return categories[np.argmax(output)]

print(run_sample(session, sys.argv[1]))
