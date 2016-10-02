# OpenCV-Workshop

OpenCV is an open source library of pre implemented computer vision algorithms. OpenCV was implemented in C++ and meant to be used in C++ but now we have bindings for OpenCV in Python, Java, Matlab and even in node.js.

## Task 0

### Installations
1. Install [python 2.7](https://www.python.org/downloads/).
2. Install numpy with ```pip install numpy```.

#### For Windows:
1. Install opencv python with ```pip install opencv-python```

#### For MacOSX:
1. Install [homebrew](http://brew.sh/).
2. Tap the science packages with ```brew tap homebrew/science```.
3. Install opencv with ```brew install opencv3 --with-contrib```.

#### For Linux:
1. Please refer to this [link](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/) for installation.


### Introduction
Images are seen by computers as a collection of pixels. A RGB image which appears to us as colored images would be seen by a computer as a collection of pixels whose values range from 0 to 255. A RGB image has 3 components for each pixel denoting Red, Green and Blue. A grayscaled image on the other hand would have 1 component denoting the intensity of the color black. 

![](http://1.bp.blogspot.com/-kt8PH5S_PZw/S4bZa6toSWI/AAAAAAAAADI/oAXaadbZaK8/s400/lenna_pixels.png "")
![](https://www.gimp.org/tutorials/Straight_Line/straight_line_example.png "")

Computer vision makes use of these pixels to derive different conclusion about an image. A simple example would be - a transition from a pixel value of 0 to 1 is not very significant whereas a transition from 0 to 255 could be considered an edge.

This workshop is intended to be more hands on than theory based. So I will be focusing a lot more on using the OpenCV library than explaining the concepts a lot.

## Task 1
Write a program to simply read and display an image with OpenCV. Use the ```cv2.imwrite()``` function to then, store this image in your directory.

## Task 2
Write a program to capture a video and display it with OpenCV. In addition, write the grayscaled frames to a file. Try to read this image in later.

## Task 3
Let us explore drawing functions. OpenCV allows you to draw on images with drawing functions. The options are lines, circles, rectangles, polygons and texts.

## Task 4
Let us now explore Image Operations. OpenCV-python stores images as numpy arrays. These arrays have several properties which turn out to be very useful factors of the images.

* Shape of the image returns the number of rows, columns and channels. The channels factor can determine whether the image is grayscaled or not.
* Size of the image returns the total number of pixels.
* Dtype of the image returns the datatype.

You can also pick a region of interest from this image.

Another operation is an Image Blend.

## Task 5
Color spaces are an important concept in image processing. A few commonly known color spaces are RGB, HSV and GRAY. 

Color maps let you map known color spaces to other pixel values. A few known color maps are RAINBOW, AUTUMN and so on.

## Task 6
Canny Edge Detection is a commonly used computer vision algorithm to detect edges in images. We take a look at the transition from black to white in a grayscaled and if continuous elements map the same transition it can be determined as an edge.

## Task 7
HoughTransform is another commonly used computer vision algorithm to detect lines or circles in an image. HoughLine Transform makes use of the parametric equation of a line to determine if an edge is a line or not.

## Task 8
HaarCascades is based on a paper by Viola and Jones on Rapid Object Detection. This algorithm can be used to train models to detect different types of objects.
