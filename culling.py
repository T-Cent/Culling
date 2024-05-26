import os
import time

print("Thank you for taking the time, starting review")
print("If the output matches the image, you can press enter, else, you can type anything")

import torch
from torchvision import transforms
from PIL import Image
import pygetwindow as gw

model_path = "modelv2"

class_names = ["blurry", "exposed", "good", "noisy"]
device = "cuda" if torch.cuda.is_available() else "cpu"

data_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


def get_predictions(model, img_path: str):
    try:
        img = Image.open(img_path)
    except:
        return "not an image"

    model.eval()
    file_loc = '"' + os.path.join(os.getcwd(), img_path) + '"'
    os.system(file_loc)
    window = gw.getWindowsWithTitle("Photos")[0]
    window.moveTo(600, 0)
    window.resizeTo(1000, 1000)
    img_path_no_ext = os.path.splitext(img_path)[0]
    img_ext = os.path.splitext(img_path)[1]
    is_jpg = (img_ext == ".jpg")
    if not is_jpg:
        img = img.convert("RGB")
        img.save(img_path_no_ext + "_temp", format="JPEG")
        img = Image.open(img_path_no_ext + "_temp")
    img = data_transforms(img)
    img = img.unsqueeze(0)
    img = img.to(device)

    with torch.no_grad():
        outputs = model(img)
        _, preds = torch.max(outputs, 1)
    os.remove(img_path_no_ext + "_temp") if not is_jpg else ...
    print(outputs)
    return class_names[preds[0]], window

culling_model = torch.load(model_path, map_location=torch.device(device))
terminal = gw.getWindowsWithTitle("Terminal")[0]
pos = terminal.topleft
size = terminal.size
terminal.moveTo(0, 0)
terminal.resizeTo(600, 1000)
correct = 0
total = 0
for x in os.listdir(os.getcwd()):
    out = get_predictions(culling_model, x)
    if out == "not an image":
        continue
    (attribute, window) = out
    terminal.activate()
    ans = input(f"is this image {attribute}? ") or "yes"
    window.close()
    total += 1
    correct += 1 if ans == "yes" else 0
    
terminal.moveTo(*pos)
terminal.resizeTo(*size)
print(f"Thanks once again, the review is done, our model was able to correctly identify {correct} images out of {total}")
