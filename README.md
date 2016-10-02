# OpenCV-Workshop

OpenCV is an open source library of pre implemented computer vision algorithms. OpenCV was implemented in C++ and meant to be used in C++ but now we have bindings for OpenCV in Python, Java, Matlab and even in node.js.

# Task 0

## Installations
1. Install [python 2.7](https://www.python.org/downloads/).
2. Install the dependencies with ```pip install -r requirements.txt```

## Introduction
Images are seen by computers as a collection of pixels. A RGB image which appears to us as colored images would be seen by a computer as a collection of pixels whose values range from 0 to 255. A RGB image has 3 components for each pixel denoting Red, Green and Blue. A grayscaled image on the other hand would have 1 component denoting the intensity of the color black. 

Computer vision makes use of these pixels to derive different conclusion about an image. A simple example would be - a transition from a pixel value of 0 to 1 is not very significant whereas a transition from 0 to 255 could be considered an edge.