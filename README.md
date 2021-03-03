# Make up application
## Group member:
* **Nguyen Hoang An** - *18520430@gm.uit.edu.vn*
* **Nguyen Huynh Anh** - *18520456@gm.uit.edu.vn*
* **Nguyen Ngoc Binh** - *18520506@gm.uit.edu.vn*
* **Duong Trong Van** - *18521630@gm.uit.edu.vn*

# Table of contents
=================

<!--ts-->
   * [Introduction](introduction)
   * [Install requirements](#install-requirements)
   * [Demo](#Demo)
   * [Run streamlit](#run-streamlit)
   * [Checklist](#Checklist)
<!--te-->

## Introduction
This project is on the field of Computer Vision, an sub-domain of Computer Science. On this project, we combine two methods:
* Facial landmark with HoG features 
* [Face parsing](https://github.com/zllrunning/face-parsing.PyTorch)

Futhermore, we use [Streamlit](https://streamlit.io/) - an open source framework to build our GUI 

## Install requirements
```Shell
pip install -r requirements.txt
```

## Demo

### Main screen
![alt text](https://github.com/NguyenHoangAn0511/Make-up-application-DeepLearning-Flask/blob/main/Makeup/example/main.jpeg)

### Image Enhance + Filter + Dye hair example
![alt text](https://github.com/NguyenHoangAn0511/Make-up-application-DeepLearning-Flask/blob/main/Makeup/example/POSTERIZE%20%2B%20OBLUE.jpeg)
![alt text](https://github.com/NguyenHoangAn0511/Make-up-application-DeepLearning-Flask/blob/main/Makeup/example/PURRPLE-hair.jpeg)
![alt text](https://github.com/NguyenHoangAn0511/Make-up-application-DeepLearning-Flask/blob/main/Makeup/example/MAKEUP-adjust.jpeg)

## Run streamlit
```
streamlit run main.py
```
###### Output:
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.5:8501
```
## Checklist
- [x] Upload Image
- [x] Process uploaded image
- [x] Save Image to Database
- [x] Interactive Web app
- [x] Face detection (Facial Landmark, Face parsing)
- [x] Image filter (Vintage, ...)
- [x] Dye hair & better eyebrow color
