import numpy as np
class Transformer(object):
    """
    This class provides callable instances that apply specified transformations to images.
    The instances take as argument an image and return the transformed image.
    By default, all the transformations in the list 'transforms' will be applied to an image.
    If 'randomize_transforms' is set to 'True', then on each call a random subset of the provided
    transformations in 'transfoms' will be applied to the passed image of type numpy.ndarray
    
    Parameters
    ----------
    
    transforms: An iterable with each element representing a callable function / object that takes as argument
                an image of type numpy.ndarray and returns an image of type numpy.ndarray
                Example behaviour:
                image = cv2.imread(PATH_TO_IMAGE)
                transformed_image = transforms[i](image)
    
    randomize_transforms: default = False
                If left to default, all the transformations are applied to an image.
                If set to 'True', then a subset of the transformations in 'transforms' is applied to the image
                A boolean array can be passed of length len(transforms) specifying the randomy behaviour for each
                transform separately
                
    
    Returns
    -------
    A callable instance that acts as an image transformation function.
    The functions takes in as argument an image of type numpy.ndarray and returns an image of the same type
    
    Example Usage:
    transforms = [Horizontal_flip(), Gaussian_blur(amount=3), 
                  Crop_and_resize(do_crop=False, resize_dims=(512, 512))]
    transformer_object = Transformer(transforms=transforms)
    
    image = cv2.imread(PATH_TO_IMAGE)
    transformed_image = transformer_object(image)
    """
    def __init__(self, transforms, randomize_transforms=False):
        self.transforms = list(transforms)
        self.randomize = randomize_transforms
        try:
            self.len = len(self.transforms)
        except:
            self.len = 1
        self.do_ops = self.get_do_ops()

    def get_do_ops(self):
        if self.randomize == True:
            return np.zeros(self.len, dtype=np.uint8)
        elif self.randomize == False:
            return np.ones(self.len, dtype=np.uint8)
        elif len(self.randomize) == self.len:
            return self.randomize
        
    def __call__(self, img):
        operations = np.random.randint(0, 2, self.len) + self.do_ops
        for i in range(self.len):
            if operations[i]:
                img = self.transforms[i](img)
        return img