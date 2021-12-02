# 2021-VRDL-HW2

This repository contains the code for homework 2 of 2021 Fall Selected Topics in Visual Recognition using Deep Learning.

## Installation
```
pip install -r requirements.txt
```

## Dataset Preparation
1. Download the training set `train.zip`, test set `test.zip`, `digitStruct.mat` and `see_bboxes.m` from [CodaLab](https://competitions.codalab.org/competitions/35888) and put them in `dataset` folder
2. Unzip `train.zip` and `test.zip`
3. Run `python read_mat.py` to create a txt file containing label information for each training image separately. The file structure will be as following:
```
- train/
├── 1.png
├── 1.txt
├── 2.png
├── 2.txt
│     .
│     .
│     .
├── 33402.png
└── 33402.txt
```

## Quick Start for generating the submitted results
1. Download the [model weight](https://drive.google.com/file/d/1oCXwLIHOnQRQttscQqBc0ilwaCDk37M5/view?usp=sharing) and run
```
python detect.py --source dataset/test/ --weights best.pt --conf 0.25 --img-size 512 --device 0 --save-txt --save-conf
```
2. Run `python tojson.py` to collect the predicted results and generate a `.json` file
3. Using [inference.ipynb](https://drive.google.com/file/d/1tI_WbfAVm2f27MvjUxuH-9Cl-ch8poVd/view?usp=sharing) to test the inference time

## Train Model
1. Download the pre-trained weight of `YOLOR-CSP-X` from the official site of [YOLOR](https://github.com/WongKinYiu/yolor) or [google drive](https://drive.google.com/file/d/10ZSMuCnu2-7ysjOuS-tOj_uN8jzAeT-j/view?usp=sharing)
2. Run the comment
```
python train.py --img 512 --batch 8 --epochs 30 --device 0 --name yolor_csp_x
```

## Acknowledgement
This implementation is heavily based on [YOLOR](https://github.com/WongKinYiu/yolor).
