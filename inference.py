import os
import argparse
import tensorflow as tf

def load_model():
    model_path = "model.h5"
    model = tf.keras.models.load_model(model_path)
    return model

def infer(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(32, 32))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    
    # Нормалізація зображення, так само, як було зроблено під час навчання моделі
    img_array = img_array / 255.0

    predictions = model.predict(img_array)
    ascii_index = tf.argmax(predictions[0]).numpy()

    return ascii_index

def main(directory):
    model = load_model()

    label_mapping = {index: char for index, char in enumerate("0123456789ABCDEFGHIJKLMNPQRSTUVWXY")}
    ascii_index = {char: ord(char) for char in "0123456789ABCDEFGHIJKLMNPQRSTUVWXY"}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                image_path = os.path.join(root, file)

                try:
                    class_index = infer(image_path, model)
                    label = label_mapping[class_index]
                    asc = ascii_index[label]
                    print(f"label {label}, ascii_index {asc}, path {image_path}")

                except Exception as e:
                    print(f"Помилка при обробці зображення {image_path}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test inference script.')
    parser.add_argument('--input', type=str, help='Directory with image samples.')
    args = parser.parse_args()

    main(args.input)
