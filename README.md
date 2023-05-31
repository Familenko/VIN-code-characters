Project Documentation

Introduction

This project focuses on digitalisation of handwritten VIN-code characters

Data

The data used in this project is from https://www.kaggle.com/datasets/vaibhao/handwritten-characters?datasetId=53376&sortBy=voteCount

Application manual from https://keras.io/api/applications/

Tips for building a model from:
Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems, 2nd Edition O'Reilly

Methods and Models

Model Architecture
The model used in this project is based on VGG16. The architecture consists of GlobalMaxPooling2D and two Dense layer. Optimal parameters was found by
GridSearch with testing of different applications ('DenseNet201','EfficientNetB0','VGG16'), neyrons and activators

Training
The model was trained using Adam optimaizer, and relu activation. The training data was prepared using ImageDataGenerator(rescale=1./255), wich was sufficient.     Training size was (32, 32) specialy to inkrease batch_size up to 320. Also was using EarlyStopping wich stop training after 6 epoch with accuracy 90

Evaluation
The trained model was evaluated on a separate validation dataset. The achieved accuracy on the validation set was 90

Usage Instructions

Clone the project repository: https://github.com/Familenko/VIN-code-characters.git or gh repo clone Familenko/VIN-code-characters

Build conteiner: docker build -t my_app .

Check the files in Docker conteiner: docker run -it --rm -v /Users/aleksejkitajskij/Desktop/app:/app my_app ls /app (change directory according to you)

Run the conteiner: docker run -it --rm -v /Users/aleksejkitajskij/Desktop/app:/app my_app python3 /app/inference.py --input /app/test/9 (change directory according to you)

This project was developed by Kitaiskyi Oleksii. For any inquiries, please contact leshafamilenko@gmail.com or Telegram @Familenko
