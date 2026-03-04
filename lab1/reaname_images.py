import os

raw_dir = "data/raw"

for class_name in os.listdir(raw_dir):
    class_path = os.path.join(raw_dir, class_name)

    if not os.path.isdir(class_path):
        continue

    print(f"\nОбработка класса: {class_name}")

    images = [f for f in os.listdir(class_path)
              if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    images.sort()

    for idx, filename in enumerate(images):
        old_path = os.path.join(class_path, filename)
        temp_path = os.path.join(class_path, f"temp_{idx}.jpg")
        os.rename(old_path, temp_path)

    temp_images = [f for f in os.listdir(class_path)
                   if f.startswith("temp_")]

    temp_images.sort()

    for idx, filename in enumerate(temp_images, start=1):
        old_path = os.path.join(class_path, filename)
        new_path = os.path.join(class_path, f"{idx}.jpg")
        os.rename(old_path, new_path)

    print(f"Готово: {len(images)} файлов переименовано")

print("\nВсе классы обработаны")
