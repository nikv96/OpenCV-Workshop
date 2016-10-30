#### For Windows:
1. Install OpenCV python by typing ```pip install opencv-python``` in the command prompt/terminal.
2. Test if the installation worked:
  1. Open Command Prompt/Terminal.
  2. Type in ```python```.
  3. In the python shell type in ```import cv2``` and in the next line ```cv2.__version__``` and it should print ```3.1.0```.

#### For macOS:
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