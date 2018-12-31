# A simplified approach to Data Augmentation for Computer Vision applications using python.
(Please bear with me, I’m still a beginner in deep learning and this is my first upload to GitHub, I don’t know the way of the hub) <br>
After doing a lot of mini projects, I realized the need to have a generalized input pipeline for machine learning models involving images. Further, I wanted to streamline data augmentation by creating certain common and easy to use image transformations.
<br>This library is my solution to the problems posed above. I acknowledge that there will many bugs in the code provided. Also, the code may not have followed the best design philosophies. I welcome all changes to my repo.
The class `ImageReader` serves to provide all of image reading and data augmentation functionalities in minimal lines of code. 
 <br>
Here is an example to show just how easy it is: <br>
 <br>
`tfms = [Horizontal_flip(), Vertical_flip(), Gaussian_blur(3),` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Crop_and_resize(do_crop=False, sz=(300, 300))]` <br>
`imr = ImageReader(PATH_TO_IMAGES, transforms=tfms)` <br>
`image = imr.read_image_random()` <br>
<br>
This will read an image from the given path with random transformations applied each time an image is read.
<br><br>
The `ImageReader` class provides certain convenience functions: <br>
`read_image_from_id(self, ID)`: reads an image specified by ID. <br>
`read_image_from_idx(self, idx)`: reads an image from specified index from a list of all files in `PATH_TO_IMAGES` <br>
`read_image_random(self)`: reads and returns a random image from `PATH_TO_IMAGES` <br>
`show_by_id(self, ID)`: Displays image specified by ID <br>
`show_random(self)`: Displays a random image from `PATH_TO_IMAGES` <br>

Here, OpenCV is primarily used to read images and perform most transformation operations. <br>

The file `aug_transforms.py` includes certain common transformations used in computer vision and their appropriate documentation is included in the functions. <br>
The file `Transformer.py` provides a `Transformer` class that is used by the `ImageReader` class. It can be used to create objects that transform images read as numpy arrays. You can pass any number of your own transformations that behave as specified in the Transformer class’ documentation. <br>


A typical way to use this library would be as follows:  <br>

`from ImageReader import *` <br> <br>

`tfms = [Horizontal_flip(), Vertical_flip(), Gaussian_blur(3),` <br>
`		Crop_and_resize(do_crop=False, sz=(300, 300))]` <br>
`imr = ImageReader(PATH_TO_IMAGES, transforms=tfms)` <br>
`image = imr.read_image_random()` <br>

 <br> <br>
Dependencies:  <br>
OpenCV, skimage, Numpy, Matplotlib, os.
 <br> <br>
Use as you please :-)
