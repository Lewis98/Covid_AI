# = = = = = = = = = = #
#        CELL 1       #
# = = = = = = = = = = #


import numpy as np #Stored data as numpy arrays

import pickle #Pickle used to serialize dictionary of data and targets

from skimage.io import imread # Image pre-processing
from skimage.color import rgb2gray # Color to grayscale conversion
from skimage.transform import resize # Image resizing and standardisation

from sklearn import preprocessing # Used to scale data

import os # Directory navigation / manipulation




# = = = = = = = = = = #
#        CELL 2       #
# = = = = = = = = = = #

#Convert data

#Root directory containing Raw image files
root_dir = r'.\\Dataset' 


#Create arrays to store images and labels
Images = []
Targets = []

#Iteration counter
i = 0
tot = len(os.listdir(root_dir)) #Total files

#For each image
for f in os.listdir(root_dir):
    img = imread(root_dir + "\\" + f) #Read Image
    img = rgb2gray(img) #Convert to grayscale if colour
    img = resize(img, (512, 512),anti_aliasing=True) #Resize image
    img = img.flatten() #Flatten Matrix of image data into 1D array
    Images.append(img) #Append to array of images

    #If filename starts with Covid
    if f.startswith("COVID19"):
        Targets.append(1) #Append 1 to target array for positive
    else:
        Targets.append(0)#Append 0 to target array for negative
    
    
    #Update user with status of processing every 50 images
    i += 1
    if i % 50 == 0:
        print(str(i) + "/" + str(tot) + " Images processed")
        
        


# = = = = = = = = = = #
#        CELL 3       #
# = = = = = = = = = = #      
        
#Output directory for binary
save_dir = r'.\\' # REQUIRED - Filepath to output pickled dataset

#Scale Data
Images = preprocessing.scale(Images)

#Create dictionary containing Image data and Target data
Xrays = {
    "data" : Images,
    "targets" : Targets
}

#Create / open file and dump dictionary using pickle
with open( save_dir + "Xray_data.p", "wb" ) as of:
    pickle.dump( Xrays, of)
        