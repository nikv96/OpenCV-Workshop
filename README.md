# OpenCV-Workshop

*Disclaimer - This workshop was made for the $PATH to iNTUition workshop series leading to [iNTUition v3.0](http://intuition.ieeentu.com).*

OpenCV is an open source library of pre implemented computer vision algorithms. OpenCV was implemented in C++ and meant to be used in C++ but now we have bindings for OpenCV in Python, Java, Matlab and even in node.js.

## Task 0

Clone this repository or [download](https://github.com/nikv96/OpenCV-Workshop/archive/master.zip) the zip file from GitHub.

### Installations
1. Install [python 2.7](https://www.python.org/downloads/) (For OSX and Linux users, python 2.7 should be installed by default).
2. Add python to your system path. (For Windows users, navigate to This PC -> System Properties or Settings -> Advanced System Settings -> Environment Variables -> Path -> Edit and then add ```C:\Python27``` and ```C:\Python27\Scripts``` to the Path).
4. Restart your terminal or command prompt.
5. On your terminal/command prompt enter ```pip install numpy``` to install numpy.
6. (Additional) Install a text editor such as [sublime text](https://sublimetext.com/2) to edit your code.
7. (Additional) For Windows users, I would advice downloading a bash shell such as [git bash](https://git-scm.com/downloads).

#### For Windows:
1. Install OpenCV python by typing ```pip install opencv-python``` in the command prompt/terminal.
2. Test if the installation worked:
  1. Open Command Prompt/Terminal.
  2. Type in ```python```.
  3. In the python shell type in ```import cv2``` and in the next line ```cv2.__version__``` and it should print ```3.1.0```.

#### For MacOSX:
1. First step,install [Xcode](https://developer.apple.com/xcode/) which is combination of IDE and software developement tools for developing applications on OSX AND iOS platform.
2. Install [homebrew](http://brew.sh/).
3. To update brew simply execute: 

	```
	$ brew update
	```

4. Install user specific version of python: 

	```
	$ brew install python
	```

5. However, before we proceed, we need to update our PATH  in our ~/.bash_profile  file to indicate that we want to use Homebrew packages before any system libraries or packages. Open up your ~/.bash_profile  file in your favorite editor (if it does not exist, create it), and append the following lines to the file:
	```
	# Homebrew
	export PATH=/usr/local/bin:$PATH
	```
	* From there, reload your ~./bash_profile  file to ensure the changes have been made: 
	```
	$ source ~/.bash_profile
	```
	* As a sanity check, let’s confirm that we are using the Homebrew version of Python rather than the system one:
		$ which python

	* If your output of which python  is /usr/local/bin/python , then you are indeed using the Homebrew version of Python. And if your  output is /usr/bin/python , then you are still using the system version of Python — and you need to go back and ensure that your ~/.bash_profile  file is updated and reloaded correctly.
6. [Optional] Installing virtualenv and virtualenvwrapper: ```$ pip install virtualenv virtualenvwrapper```
	* Again, we need to update our ~/.bash_profile  file by appending the following two lines:
		```
		# Virtualenv/VirtualenvWrapper
		source /usr/local/bin/virtualenvwrapper.sh
		```
	* After updating the ~/.bash_profile  file, we need to reload it:
		```
		$ source ~/.bash_profile
		```
	* At this point, both virtualenv  and virtualenvwrapper  are installed correctly, so we can create our cv  virtual environment:
		```
		$ mkvirtualenv cv
		```
7. We need to install NumPy since the OpenCV Python bindings represent images as multi-dimensional NumPy arrays:

	```
	$ pip install numpy
	```
	
	* Now that our developement environment is set up and configured,its time for us to get into real work.
	
		```
		$ brew install cmake pkg-config
		```
		
	* Install necessary image I/O packages
	
		```
		$ brew install jpeg libpng libtiff openexr
		$ brew install eigen tbb
		```
		
8. Alright, our system is all setup — time to compile and install OpenCV 3.0 with Python 2.7+ support.

	```
	$ cd ~
	$ git clone https://github.com/Itseez/opencv.git
	$ cd opencv
	$ git checkout 3.0.0
	```

    [Optional]	
    
	```
	$ cd ~
	$ git clone https://github.com/Itseez/opencv_contrib
	$ cd opencv_contrib
	$ git checkout 3.0.0
	```
	
9. Let’s setup our OpenCV build by creating the build  directory:

	```
	$ cd ~/opencv
	$ mkdir build
	$ cd build
	```
	
	* Where we’ll use CMake to configure our build
	
		```
		$ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
			-D PYTHON2_PACKAGES_PATH=~/.virtualenvs/cv/lib/python2.7/site-packages \
			-D PYTHON2_LIBRARY=/usr/local/Cellar/python/2.7.10/Frameworks/Python.framework/Versions/2.7/bin \
			-D PYTHON2_INCLUDE_DIR=/usr/local/Frameworks/Python.framework/Headers \
			-D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON \
			-D BUILD_EXAMPLES=ON \
			-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules ..
		$ make -j4
		$ make install
		$ sudo make install
		```
		
10. After all this work, lets check if OpenCV 3 is correctly installed.

	```
	$ python
	$ import cv2
	$ cv2.__version
	```
	
	The output has to be 3.1.0 or 3.0.0.
				
	
#### For Linux:
1. Please refer to this [link](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/) for installation.

### Running the scripts
1. Navigate to the directory with the script in your command prompt or terminal. eg: ```cd <Path to Repository>/Task\ 1```.
2. Run on command prompt or terminal with ```python <script>.py```.

### Introduction
Images are seen by computers as a collection of pixels. A RGB image which appears to us as colored images would be seen by a computer as a collection of pixels whose values range from 0 to 255. A RGB image has 3 components for each pixel denoting Red, Green and Blue. A grayscaled image on the other hand would have 1 component denoting the intensity of the color black. 

![](http://1.bp.blogspot.com/-kt8PH5S_PZw/S4bZa6toSWI/AAAAAAAAADI/oAXaadbZaK8/s400/lenna_pixels.png "")
![](https://www.gimp.org/tutorials/Straight_Line/straight_line_example.png "")

Computer vision makes use of these pixels to derive different conclusion about an image. A simple example would be - a transition from a pixel value of 0 to 1 is not very significant whereas a transition from 0 to 255 could be considered an edge.

## Task 1
Write a program to simply read and display an image with OpenCV. Use the ```cv2.imwrite()``` function to then, store this image in your directory.

## Task 2
Write a program to capture a video and display it with OpenCV. In addition, write the grayscaled frames to a file. Try to read this image in later.

## Task 3
Let us explore drawing functions. OpenCV allows you to draw on images with drawing functions. The options are lines, circles, rectangles, polygons and texts.

**Exercise** - Recreate the Olympics symbol as close as possible!

## Task 4
Let us now explore Image Operations. OpenCV-python stores images as numpy arrays. These arrays have several properties which turn out to be very useful factors of the images.

* Shape of the image returns the number of rows, columns and channels. The channels factor can determine whether the image is grayscaled or not.
* Size of the image returns the total number of pixels.
* Dtype of the image returns the datatype.

You can also pick a region of interest from this image.

Another operation is an Image Blend.

**Exercise** - Try to overwrite a region of the image with a black image.

## Task 5
Color spaces are an important concept in image processing. A few commonly known color spaces are RGB, HSV and GRAY. 

Color maps let you map known color spaces to other pixel values. A few known color maps are RAINBOW, AUTUMN and so on.

**Exercise** - Try to get the image looking close to a thermal camera output.

## Task 6
Canny Edge Detection is a commonly used computer vision algorithm to detect edges in images. We take a look at the transition from black to white in a grayscaled and if continuous elements map the same transition it can be determined as an edge.

## Task 7
HoughTransform is another commonly used computer vision algorithm to detect lines or circles in an image. HoughLine Transform makes use of the parametric equation of a line to determine if an edge is a line or not.

**Exercise** - Find an image online with two circles. Detect the two circles with OpenCV and connect the centers with a line.

## Task 8
HaarCascades is based on a paper by Viola and Jones on Rapid Object Detection. This algorithm can be used to train models to detect different types of objects.

**Exercise** - Extend the detector to detect eyes. Then, extend the code to detect faces and eyes in a video.

## Help & Feedback
If you have any questions or feedback on the workshop, write to me at [nikv96@gmail.com](mailto:nikv96@gmail.com). I'd love to hear what you think about this workshop. :)

## Errors
If you find any mistakes/typos/bugs, please post an issue or create a pull request and I'll take a look at it! Thanks!

## References
1. [http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)
2. [www.pyimagesearch.com/](www.pyimagesearch.com/)

## Further Studies
1. [http://opencv.org/documentation.html](http://opencv.org/documentation.html)
2. [https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
3. [http://www.pyimagesearch.com/](http://www.pyimagesearch.com/)
