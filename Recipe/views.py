from django.shortcuts import render
import base64
import json
from io import BytesIO
import numpy as np
from keras.preprocessing import image
import requests
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def vision_api(request):
    img = image.img_to_array(image.load_img(BytesIO(base64.b64decode(request.POST.get('b64'))),
                                            target_size=(224, 224))) / 255.

    # this line is added because of a bug in tf_serving(1.10.0-dev)
    img = img.astype('float16')

    # Creating payload for TensorFlow serving request
    payload = {
        "instances": [{'input_image': img.tolist()}]
    }

    # Making POST request
    r = requests.post('http://localhost:8501/v1/models/HomeCook:predict', json=payload)

    # Decoding results from TensorFlow Serving server
    pred = json.loads(r.content.decode('utf-8'))
    output = np.array(pred['predictions'])
    output = [1 if i >= 0.1 else 0 for i in np.around(output, 2).tolist()[0]]

    res_data = []
    for i, d in output:
        if d:
            if i == 0:
                res_data.append({14: "Butter"})
            elif i == 1:
                res_data.append({3: "Chicken"})
            elif i == 2:
                res_data.append({1: "Eggs"})
            elif i == 3:
                res_data.append({32: "Tomato"})

    return json.dumps(res_data)
