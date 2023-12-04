from roboflow import Roboflow

# finds plate and returns x and y coordinates of plate

def find_plate(model, img_path):

    dic = model.predict(img_path, confidence=40, overlap=30).json()
    if len(dic["predictions"]) == 0:
        return None
    data = dic["predictions"][0]
    box = []
    box.append(data['x'])
    box.append(data['y'])
    box.append(data['width'])
    box.append(data['height'])
    return box
