import os
import shutil
import random

# Пути
raw_dir = "data/raw"
train_dir = "data/train"
val_dir = "data/val"
test_dir = "data/test"

# Пропорции
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

random.seed(42)

for class_name in os.listdir(raw_dir):
    class_path = os.path.join(raw_dir, class_name)

    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    random.shuffle(images)

    total = len(images)
    train_split = int(total * train_ratio)
    val_split = int(total * (train_ratio + val_ratio))

    train_images = images[:train_split]
    val_images = images[train_split:val_split]
    test_images = images[val_split:]

    for folder in [train_dir, val_dir, test_dir]:
        os.makedirs(os.path.join(folder, class_name), exist_ok=True)

    for img in train_images:
        shutil.copy(
            os.path.join(class_path, img),
            os.path.join(train_dir, class_name, img)
        )

    for img in val_images:
        shutil.copy(
            os.path.join(class_path, img),
            os.path.join(val_dir, class_name, img)
        )

    for img in test_images:
        shutil.copy(
            os.path.join(class_path, img),
            os.path.join(test_dir, class_name, img)
        )

print("Разделение завершено")
