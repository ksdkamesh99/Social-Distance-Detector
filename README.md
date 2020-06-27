# ⛹️‍♂️Social-Distance-Detector

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Directory Tree](#directory-tree)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [License](#license)


## Demo
![](demo.gif)

## Overview
It is a social distance detector based on OPENCV  used to find track persons who are following social distance and who are not following.  

## Motivation
Limiting face-to-face contact with others is the best way to reduce the spread of coronavirus disease 2019 (COVID-19).

Social distancing, also called “physical distancing,” means keeping space between yourself and other people outside of your home.

This Project/Idea is very much helpful for government and police to track people in public places through the help of artificial intelligence.

## Technical Aspect

Here in this project I used MobilenetSSD and YOLOV3 to detect the persons in the video and used a basic algorithm created by me to detect whether the distance between any 2 persons is greater than 1.5 feet is marked as safe and other are marked as unsafe. Persons who are unsafe are marked with red border and people who are safe are marked as green border .  

## Installation
1. If you like my project do 🌟🌟 my repository.

2. Clone my repository by using following command in terminal/Command Prompt.

```sh
git clone https://github.com/ksdkamesh99/Social-Distance-Detector.git
```

3. Now we need to install required libraries like opencv,spacy etc.  

4. You need to download YOLOV3 weights for 608x608 dimensions from darknet. [Check Here](https://pjreddie.com/media/files/yolov3.weights)

5. Based on the input type commands are here:
    1. If your input type is a image and want to detect then type your relative image path as argument in terminal..
    ```sh
    python app_image.py "test_image.jpg"
    ```
    2. If your input type is a video and want to detect using mobilenet_ssd then type your relative video path as argument in terminal.
    ```sh
    python app_video.py "test_video."
    ```
    3. If your input type is a image and want to detect usiing YOLOV3 608x608 then type your relative video path as argument in terminal..
    ```sh
    python app_yolo.py "test_video."
    ```    
## To Do in future:-

1. Need to ad bird view to the project

2. Improve accuracy

## Bug / Feature Request
If you find a bug (gave undesired results), kindly open an issue [here](https://github.com/ksdkamesh99/Social-Distance-Detector/issues/new/) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/ksdkamesh99/Social-Distance-Detector/issues/new/choose). Please include sample queries and their corresponding results.

## Technologies Used

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)[![forthebadge](https://forthebadge.com/images/badges/its-not-a-lie-if-you-believe-it.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)

[<img target="_blank" src="https://pjreddie.com/media/image/yologo_2.png" width=200>](https://pjreddie.com/darknet/yolo/) [<img target="_blank" src="https://opencv-python-tutroals.readthedocs.io/en/latest/_static/opencv-logo-white.png" width=170>](https://opencv-python-tutroals.readthedocs.io/en/latest/)



## License

MIT License

Copyright (c) 2020 Kota Sai Durga Kamesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## 📧Contact:-
For any kind of suggesstions/ help in code Please mail me at ksdkamesh99@gmail.com.

