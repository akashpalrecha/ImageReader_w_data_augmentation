import numpy as np
import cv2

class Horizontal_flip(object):
    """ 
    This class provides callable instances that randomly flip an image horizontally
    
    Parameters
    ----------
    randomize: default=True
            If set to 'True', the function will flip an image on a random basis
            If set to 'False', the function will always horizontally flip an image 
    
    Returns
    -------
    A callable instance of the class that acts as a function
    The functions takes as argument an image of type numpy.ndarray
    Returns: image of type numpy.ndarray
    
    Example Usage : 
    image = cv2.imread(PATH_TO_IMAGE)
    horiontal_flip_object = Horizontal_flip(randomize=True)
    flipped_image = horiontal_flip_object(image)
    """
    def __init__(self, randomize=True):
        self.randomize = randomize

    def __call__(self, img):
        do_op = np.random.randint(0,2,1) if self.randomize else 1
        if do_op:
            return cv2.flip(img, 1)
        else:
            return img

class Vertical_flip(object):
    """ 
    This class provides callable instances that randomly flip an image vertically
    
    Parameters
    ----------
    randomize: default=True
            If set to 'True', the function will flip an image on a random basis
            If set to 'False', the function will always vertically flip an image 
    
    Returns
    -------
    A callable instance of the class that acts as a function
    The functions takes as argument an image of type numpy.ndarray
    Returns: image of type numpy.ndarray
    
    Example Usage : 
    image = cv2.imread(PATH_TO_IMAGE)
    vertical_flip_object = Vertical_flip(randomize=True)
    flipped_image = vertical_flip_object(image)
    """
    
    def __init__(self, randomize=True):
        self.randomize = randomize

    def __call__(self, img):
        do_op = np.random.randint(0,2,1) if self.randomize else 1
        if do_op:
            return cv2.flip(img, 0)
        else:
            return img

class Color_jitter(object):
    """ 
    This class provides callable instances that take an image of type numpy.ndarray
    as an argument and apply random jittering to each pixel of the image.
    Here, jittering refers to randomly shifting pixel values in positive or negative amounts.
    
    Parameters
    ----------
    
    amount: default=0.1
            Maximum shift to apply to any pixel as as fraction of 255. Each pixel
            will be shifted by a random amount in the range (0, 255*amount)
    
    randomize: default=True
            If set to 'True', the function will apply color jitterring an image on a random basis
            If set to 'False', the function will always apply color jittering to an image 
    
    Returns
    -------
    A callable instance of the class that acts as a function.
    The functions takes as argument an image of type numpy.ndarray
    Returns: jittered image of type numpy.ndarray
    
    Example Usage : 
    image = cv2.imread(PATH_TO_IMAGE)
    color_jitter_object = Color_jitter(amount=0.05, randomize=True)
    modifier_image = color_jitter_object(image)
    """
    def __init__(self, amount=0.1, randomize=True):
        self.randomize = randomize
        self.amount = amount

    def __call__(self, img):
        do_op = np.random.randint(0,2,1) if self.randomize else 1
        if do_op:
            jitter = np.random.randint(-255*self.amount, 255*self.amount, img.shape).clip(0, 255).astype(np.uint8)
            return cv2.add(img, jitter)
        else:
            return img
            
class Gaussian_blur(object):
    """ 
    This class provides callable instances that take an image of type numpy.ndarray
    as an argument and randomly apply gaussian blurring to the image.
    
    Parameters
    ----------
    
    amount: default=1
            Maximum integer kernel size for gaussian blur.
            dtype: integer
            The kernel will of size (x,x) where x is a random odd number in the range (0, amount * 2 + 1)
    
    randomize: default=True
            If set to 'True', the function will blur an image on a random basis
            If set to 'False', the function will always blur an image 
    
    Returns
    -------
    A callable instance of the class that acts as a function.
    The functions takes as argument an image of type numpy.ndarray
    Returns: blurred image of type numpy.ndarray
    
    Example Usage : 
    image = cv2.imread(PATH_TO_IMAGE)
    blur_object = Gaussian_blur(amount=3, randomize=True)
    modifier_image = blur_object(image)
    """
    def __init__(self, amount=1, randomize=True):
        self.randomize = randomize
        self.amount = amount

    def __call__(self, img):
        do_op = np.random.randint(0,2,1) if self.randomize else 1
        if do_op:
            kernel = np.random.randint(0, self.amount, 1) * 2 + 1
            return cv2.GaussianBlur(img, (kernel, kernel), 0)
        else:
            return img
            
class Rotate_rand(object):
    """ 
    This class provides callable instances that take an image of type numpy.ndarray
    as an argument and randomly rotate the image by degrees in range (0, amount).
    
    Parameters
    ----------
    
    amount: default=30
            Maximum degrees by which to rotate the image.
            dtype: integer
            The image will be rotated by x degrees where x is a random integer in range (0, amount)
    
    randomize: default=True
            If set to 'True', the function will rotate an image on a random basis
            If set to 'False', the function will always rotate an image 
    
    Returns
    -------
    A callable instance of the class that acts as a function.
    The functions takes as argument an image of type numpy.ndarray
    Returns: rotated image of type numpy.ndarray. The ia
    
    Example Usage : 
    image = cv2.imread(PATH_TO_IMAGE)
    rotate_object = Rotate_rand(amount=30, randomize=True)
    modifier_image = rotate_object(image)
    """
    def __init__(self, amount=30, randomize=True):
        import skimage.transform as tfms
        self.rotate = tfms.rotate
        self.randomize = randomize
        self.amount = amount

    def __call__(self, img):
        do_op = np.random.randint(0,2,1) if self.randomize else 1
        if do_op:
            degrees = np.random.randint(-self.amount, self.amount, 1)
            return self.rotate(img, degrees)
        else:
            return img
            
class Crop_and_resize(object):
    """ 
    This class provides callable instances that take an image of type numpy.ndarray.
    The instance performs the following operations when called on an image:
    1. Crops out a section of the image which has both width and height greater that (1 - amount)
       percentage of the corresponding dimension. The exact height and width is random.
    2. If 'box' is provided, then the image is always cropped according to boundaries given in 'box'
    3. If do_crop is set to 'True', then cropping is always performed and vice versa.
    3. Resizes the image to the provided dimensions in sz (width, height) or to the
       original size if sz is not provided.
    
    Parameters
    ----------
    
    amount: default=0.1
            Maximum amount by which to reduce height and width of the cropped image as percentage of
            the original height and width. The cropping coordinates are randomly chosen.
            dtype: integer
    
    sz: default=-1
            if set to default value, each image wil be resized to its original dimensions after cropping.
            Optionally, an iterable of form (width, height) can be passed to resize each image to corresponding
            dimensions.
            
    do_crop: default=None
            If set to 'True', images will always be cropped
            If set to 'False', images will never be cropped
    
    crop_box: default=-1
            If left to default, cropping dimensions will be determined randomly using 'amount'
            An iterable of form (top, bottom, left, right) can be passed in crop_box to specify cropping dimensions
            Here, for example, 'top', refers to the upper boundary of the cropped image between (0, height).
            If 'top' = 0, then the upped boundary would be the upper side of the image and 'height' will
            be the bottom of the image
    
    randomize: default=True
            If set to 'True', the function will crop an image on a random basis
            If set to 'False', the function will always crop an image 
    
    Returns
    -------
    A callable instance of the class that acts as a function.
    The functions takes as argument an image of type numpy.ndarray
    Returns: cropped and resized image of type numpy.ndarray
    
    Example Usage : 
    image = cv2.imread(PATH_TO_IMAGE)
    crop_object = Crop_and_resize(amount=0.1, randomize=True, do_crop=True)
    modifier_image = crop_object(image)
    """
    def __init__(self, amount=0.1, randomize=True, sz=-1, do_crop=None, crop_box=-1):
        self.randomize = randomize
        self.amount = amount
        assert self.amount < 1 and self.amount >=0
        self.resize_dims = sz
        self.do_crop = do_crop
        self.box = crop_box
        
    def get_crop_box(self, img):
        if self.box == -1:
            h, b, _ = img.shape
            randx = np.random.randint(0, b*self.amount, 1)[0]
            rand_breadth = np.random.randint(randx + b*(1-self.amount), b, 1)[0]
            randy = np.random.randint(0, h*self.amount, 1)[0]
            rand_height = np.random.randint(randy + h*(1-self.amount), h, 1)[0]
            return (randy, rand_height, randx, rand_breadth)
        elif self.box != -1:
            return self.box
        
    def crop(self, img):
        do_op = np.random.randint(0,2,1) if self.randomize else 1
        if self.do_crop != False:
            if self.do_crop or do_op:    #if cropping is compulsory
                box = self.get_crop_box(img)
                return img[box[0]:box[1], box[2]:box[3], :]
            else:
                return img
        else:
            return img
    
    def resize(self, img, img_dims):
        ## self.resize = (width, height)
        if self.resize_dims == -1:
            return cv2.resize(img, (img_dims[1], img_dims[0]), interpolation=cv2.INTER_LINEAR)
        else:
            resz_product = self.resize_dims[0] * self.resize_dims[1]
            sz_product = img.shape[0] * img.shape[1]
            interp_method = cv2.INTER_LINEAR if resz_product > sz_product else cv2.INTER_AREA
            return cv2.resize(img, (self.resize_dims[0], self.resize_dims[1]), interpolation=interp_method)
    
    def __call__(self, img):
        return self.resize(self.crop(img), img.shape)
  
class Brightness(object):
    """ 
    This class provides callable instances that take an image of type numpy.ndarray
    as an argument and randomly apply random brightness variataions to the image.
    
    Parameters
    ----------
    
    amount: default = 0.05
            Maximum amount by which to alter brightness as percentage of 255
            dtype: integer
            The function will increase or decrease the brighness of an image by an amount 
            in the range (0, amount*255)
    
    randomize: default=True
            If set to 'True', the function will modify brightness of an image on a random basis
            If set to 'False', the function will always modify the brightness of an image 
    
    Returns
    -------
    A callable instance of the class that acts as a function.
    The functions takes as argument an image of type numpy.ndarray
    Returns: image of type numpy.ndarray with modified brightness
    
    Example Usage : 
    image = cv2.imread(PATH_TO_IMAGE)
    brightness_object = Brightness(amount=0.3, randomize=True)
    modifier_image = brightness_object(image)
    """
    def __init__(self, amount=0.05, randomize=True):
        self.randomize = randomize
        self.amount = amount

    def __call__(self, img):
        do_op = np.random.randint(0,2,1) if self.randomize else 1
        if do_op:
            return (img + np.random.randint(-255*self.amount, 255*self.amount, 1)[0]).clip(0, 255)
        else:
            return img
        
class Contrast(object):
    """ 
    This class provides callable instances that take an image of type numpy.ndarray
    as an argument and randomly apply random contrast variataions to the image.
    
    Parameters
    ----------
    
    amount: default = 0.05
            Maximum amount by which to alter contrast
            dtype: integer
            The function will increase or decrease the contrast of an image by an amount
            in the range (0, amount*255)
    
    randomize: default=True
            If set to 'True', the function will modify brightness of an image on a random basis
            If set to 'False', the function will always modify the brightness of an image 
    
    Returns
    -------
    A callable instance of the class that acts as a function.
    The functions takes as argument an image of type numpy.ndarray
    Returns: image of type numpy.ndarray with modified contrast
    
    Example Usage : 
    image = cv2.imread(PATH_TO_IMAGE)
    contrast_object = Contrast(amount=0.3, randomize=True)
    modifier_image = contrast_object(image)
    """
    def __init__(self, amount=0.05, randomize=True):
        self.randomize = randomize
        self.amount = amount

    def __call__(self, img):
        do_op = np.random.randint(0,2,1) if self.randomize else 1
        if do_op:
            return (img * (1 + np.random.uniform(-self.amount, self.amount, 1)[0])).astype(int).clip(0, 255)
        else:
            return img  