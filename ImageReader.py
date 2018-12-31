import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from Transformer import *
from aug_transforms import *

class ImageReader(object):
    """
    This class provides instance to easily read and transform images from a directory.
    It has been designed to make it easy to apply data augmentation to images in deep learning tasks.
    The class can be initialized with a root folder and a list of transformations to be applied to
    each image. The class also provides to minimal functions to plot images.
    
    Parameters
    ----------
    root: A Path to the root directory containing all the images.
          Currently, the directory should contain images only. Each image should have the same extension.
    
    file_ids: default = A list of all file names in the provided directory with extensions removed
          Optionally, a list containing IDs of files can be passed. In this case, the functions read_image_random
          and read_image_from_idx will read files provided in file_ids.
          
    suffix: default = Extension is inferred from image names in the directory
    
    transforms: A list of transformations to be applied to each image.
          See 'Transformer' for more details.
          
    randomize_transforms: default = False
          Parameter to randomize transformations. See 'Transforms' for more details
    """
    def __init__(self, root, file_ids=None, suffix=None,
                 transforms=None, randomize_transforms=False):
        self.PATH = root
        self.file_ids = file_ids
        self.suffix = suffix
        self.get_image_ids()
        self.len = len(self.file_ids)
        self.transforms = transforms
        assert randomize_transforms == True or randomize_transforms == False or len(randomize_transforms) == len(transforms)
        if transforms:
            self.transform_image = Transformer(transforms, randomize_transforms)
        
    def get_image_ids(self):
        """ Function to infer image IDs"""
        if self.file_ids:
            pass #file_ids provided by user
        else:
            self.file_ids = os.listdir(self.PATH)
        if self.suffix:
            pass #suffix provided by user
        else:
            self.suffix = self.file_ids[0][self.file_ids[0].find('.'):]
        self.file_ids = np.array(list(map(lambda x: x[0 : x.find('.')], self.file_ids)))

    def read_image_from_id(self, ID):
        """
        Function to read an image specified by ID.
        
        Parameters
        ----------
        ID: The file ID.
            The function returns an image with name (ID + suffix)
            
        Returns
        -------
        An image of type numpy.ndarray with appropriate transformations
        """
        
        #Read image and shift channels to convert to RGB
        img_path = os.path.join(self.PATH, ID + self.suffix)
        
        if self.transform_image:
            return self.transform_image(cv2.imread(img_path)[:, :, ::-1])
        else:
            return cv2.imread(img_path)[:, :, ::-1]
    
    def read_image_from_idx(self, idx):
        """
        Function to read an image specified by index.
        
        Parameters
        ----------
        idx: The file index.
            The function returns an image with name (file_ids[idx] + suffix)
            
        Returns
        -------
        An image of type numpy.ndarray with appropriate transformations
        """
        return self.read_image_from_id(self.file_ids[idx])
    
    def read_image_random(self):
        """
        Function to read a random image from root folder.
        
        Parameters
        ----------
        None
            
        Returns
        -------
        An image of type numpy.ndarray with appropriate transformations
        """
        idx = np.random.randint(0, self.len, 1)[0]
        return self.read_image_from_id(self.file_ids[idx])
    
    def show_by_id(self, ID):
        """
        Plot image specified by ID
        """
        plt.imshow(self.read_image_from_id(ID))
    
    def show_random(self):
        """
        Plot a random image from file_ids
        """
        self.show_by_id(self.file_ids[np.random.randint(0, self.len, 1)][0])