# Brain Tumor Detection Using MRI Scans

Dataset Br35H 👉🏻 https://www.kaggle.com/ahmedhamada0/brain-tumor-detection

Dataset MRI Images 👉🏻 https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection

---

[![Code Climate](https://codeclimate.com/github/boennemann/badges.svg)]()

<!-- PROJECT LOGO -->

<br />
<p align="center">
<a href="">
  <img src="images/logo.png" alt="Logo" width="400" height="300">
</a>

<!-- INTRODUCTION -->

## Objective
  
Brain tumors are the consequence of abnormal growths and uncontrolled cells division in the brain. They can lead to death if they are not detected early and accurately. Some types of brain tumor such as Meningioma, Glioma, and Pituitary tumors are more common than the others.

In this project, I designed & built an automatic brain tumor segmentation technique based on Convolutional Neural Network. MRI scan is used because it is less harmful and more accurate than CT brain scan.
  
<!-- ABOUT THE PROJECT -->

## About The Project

<a href="">
    <img src="images/mini-brain.png" width="80" height="80">
</a>

Brain tumors are the consequence of abnormal growths and uncontrolled cells division in the brain. They can lead to death if they are not detected early and accurately. Some types of brain tumor such as Meningioma, Glioma, and Pituitary tumors are more common than the others.

In this project, I designed & built an automatic brain tumor segmentation technique based on Convolutional Neural Network. We have used three MRI views of human brain. MRI scan is used because it is less harmful and more accurate than CT brain scan.

## Libraries Used 

    ```
    * Flask
    * keras
    * matplotlib
    * numpy
    * opencv-python
    * Pillow
    * scikit-learn
    * tensorFlow
    * Werkzeug
    ```

## Algorithms Used

* Data Loading And Pre-Processing
* Train-Test Split
* Data Normalization And One-Hot Encoding
* Model Architecture
* Loss Function And Oprimizer
* Model Training
* Model Saving
* Explanation Of Activation Function
* Explanation Of Softmax Activation

## Directory Structure

```sh
├── datasets
│   └── no
│       └── no0.jpg - no1499.jpg
│   └── yes
│       └── y0.jpg - y1499.jpg
├── images
│   └── invalid.png
│   └── logo.png
│   └── mini-brain.png
│   └── no.png
│   └── yes.png
├── pred
│   └── pred0.jpg - pred59.jpg
├── static
│   └── css
│   └── js
├── templates
│   └── import
│   └── index
├── uploads
├── app.py
├── BrainTumor10Epochs.h5
├── BrainTumor10EpochsCategorical.h5
├── mainTest.py
├── mainTrain.py
├── README.md
├── render.yaml
├── requirements.txt
```

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Prerequisites

Create a virtualenv. (optional)
  ```sh
    python3 -m venv braintumour
    surce braintumour/bin/activate
  ```

## Installation

1. Clone the repo
    ```sh
    git clone 
    ```

2. Install required libraries
   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->

## Usage

Now run the app.py file by typing following command 
```sh
   python app.py
   ```
_For more examples, please refer to the [Documentation](#)_

## About Contribution

* Raise the `issue` .
* Work on raised issues .
* Come up with interesting Medical related problems and solutions .
* You can improve the UI/UX .
* Can contribute on readme files as well .

---
                          "What we know is a drop, what we don't know is an ocean."
                                                                — Isaac Newton
---

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)]()

<p align="center">
<a href="">
  <img src="images/yes.png" alt="yes" width="900">
</a>

<p align="center">
<a href="">
  <img src="images/no.png" alt="no" width="900">
</a>

<p align="center">
<a href="">
  <img src="images/invalid.png" alt="invalid" width="900">
</a>