import os
import shutil
import random
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def split_dataset(source_dir, train_dir, val_dir, test_dir, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1):
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    for class_name in os.listdir(source_dir):
        class_dir = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_dir):
            continue

        images = os.listdir(class_dir)
        random.shuffle(images)

        train_count = int(train_ratio * len(images))
        val_count = int(val_ratio * len(images))

        train_images = images[:train_count]
        val_images = images[train_count:train_count + val_count]
        test_images = images[train_count + val_count:]

        class_train_dir = os.path.join(train_dir, class_name)
        class_val_dir = os.path.join(val_dir, class_name)
        class_test_dir = os.path.join(test_dir, class_name)

        if not os.path.exists(class_train_dir):
            os.makedirs(class_train_dir)
        if not os.path.exists(class_val_dir):
            os.makedirs(class_val_dir)
        if not os.path.exists(class_test_dir):
            os.makedirs(class_test_dir)

        for img in train_images:
            shutil.copy(os.path.join(class_dir, img), os.path.join(class_train_dir, img))
        for img in val_images:
            shutil.copy(os.path.join(class_dir, img), os.path.join(class_val_dir, img))
        for img in test_images:
            shutil.copy(os.path.join(class_dir, img), os.path.join(class_test_dir, img))

source_directory = '/content/ninjacart_data_clean'
train_directory = '/content/train'
val_directory = '/content/val'
test_directory = '/content/test'

split_dataset(source_directory, train_directory, val_directory, test_directory)