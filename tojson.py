import os
import cv2
import json

filepath = 'inference/output/'

img_txts = os.listdir(filepath)
deletes = []

# list the img_names
for name in img_txts:
    if ".png" in name:
        deletes.append(name)

for delete in deletes:
    img_txts.remove(delete)

img_names = []
for img_txt in img_txts:
    img_names.append(img_txt.split(".")[0])
img_names.sort(key = lambda x: int(x))


result_to_json = []
# for each test data
for img_name in img_names:
    print(img_name)
    f = open(filepath + img_name + '.txt','r')
    box_infos = f.readlines()

    im = cv2.imread('dataset/test/'+img_name + '.png')
    h, w, c = im.shape
    
    for box_info in box_infos:
        box_dict = {}
        box_info = box_info.replace('\n','')
        box_info = box_info.split(' ')

        # An integer to identify the image
        box_dict["image_id"] = int(img_name)

        # A list ( [left_x, top_y, width, height] )
        w_center = w*float(box_info[1])
        h_center = h*float(box_info[2])
        width = w*float(box_info[3])
        height = h*float(box_info[4])
        left = int(w_center - width/2)
        top = int(h_center - height/2)
        box_dict["bbox"] = tuple((left, top, width, height))

        # A float number between 0 ~ 1 which means the confidence of the bbox
        box_dict["score"] = float(box_info[5])

        # An integer which means the label class
        box_dict["category_id"] = int(box_info[0])

        result_to_json.append(box_dict)
        
# Write the list to answer.json 
json_object = json.dumps(result_to_json, indent=4)

with open("answer.json", "w") as outfile:
    outfile.write(json_object)
