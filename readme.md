# HW_face

This project is based on mtcnn and facenet.

set PYTHONPATH environment to this root directory like this on linux:
```bash
export PYTHONPATH=path/to/this/root/directory
```

## Prepare data

Move HW_1_Face data to `dataset/HW_1_Face/raw`

Change the data structure by running

```bash
python dataset/HW_1_Face/raw/sort.py
```

## face detection

Using mtcnn to align face bounding box. Run

```bash
python align/align_dataset_mtcnn.py \
dataset/HW_1_Face/raw/train/ \
dataset/HW_1_Face/mtcnn_160/train \
--image_size=160 \
--margin=32 \
--gpu_memory_fraction=0.85
```

and 

```bash
python align/align_dataset_mtcnn.py \
dataset/HW_1_Face/raw/test/ \
dataset/HW_1_Face/mtcnn_160/test \
--image_size=160 \
--margin=32 \
--gpu_memory_fraction=0.85
```

to get face detection of the data

## face recognition

This will use pretrained checkpoint in `saved_models/vgg_face2` trained on vgg_face2

> in progress

* using svm

train on our data using

```bash
python classifier_svm.py \
TRAIN \
dataset/HW_1_Face/mtcnn_160/train/ \
saved_models/vgg_face2/ \
saved_models/HW_1_classifier_svm.pkl \
--batch_size=256 \
--image_size=160
```

and test on our data using

```bash
python classifier_svm.py \
CLASSIFY \
dataset/HW_1_Face/mtcnn_160/test/ \
saved_models/vgg_face2/ \
saved_models/HW_1_classifier_svm.pkl \
--batch_size=256 \
--image_size=160
```
