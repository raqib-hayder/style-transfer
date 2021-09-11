import uuid

import cv2
import numpy as np
import uvicorn
from PIL import Image
from fastapi import FastAPI, File, UploadFile

import config
import inference

app = FastAPI()


@app.get("/")
def health():
    return {"health": "OK"}


@app.post("/{style}")
def get_image(style: str, file: UploadFile = File(...)):
    rgb_image = Image.open(file.file).convert("RGB")  # Convert image to RGB format
    image = np.array(rgb_image)  # Convert image to numpy array
    model = config.STYLES[style]  # Select model to use for style transfer
    output, resized = inference.inference(model, image)  # Style transfer the image
    name = f"/storage/{str(uuid.uuid4())}.jpg"  # Name the image
    cv2.imwrite(name, output)  # Save the image
    return {"name": name}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080,)