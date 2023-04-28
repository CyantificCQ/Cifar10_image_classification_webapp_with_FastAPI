# Cifar10_image_classification_webapp_with_FastAPI

I used the dataset called [Cifar10](https://www.cs.toronto.edu/~kriz/cifar.html) that contains 60000 32x32 pixel images.

The dataset has 10 classes: **airplane, automobile,bird,cat, deer, dog, frog, horse, ship, truck**.
There are 50000 training and 10000 testing images. 

I used Tensorflow Sequential API to create a basic model that has a relatively high accuracy.
After I trained a model, I created a prediction on the test set and also used some other downloaded pictures to make predictions.

![fastapi3](https://user-images.githubusercontent.com/97511979/234261188-a0370641-dea4-44d0-bc0f-6a6002fad7e2.png)

After I got that right I created my machine learning API using FastAPI.
Created a post request for uploading an image and a get request for the prediction. 

![fastapi1](https://user-images.githubusercontent.com/97511979/234262077-32a8aeb1-30cf-4973-a06d-73d319fbc429.png)
![fastapi2](https://user-images.githubusercontent.com/97511979/234262102-526f1064-240c-4b4a-ae3a-52241fae1b75.png)

It was working well so I created a Docker container for it. 
