
#import appropriate items

import numpy as np

from scipy import ndimage

import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')

import math

from astropy.io import fits

from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

from astropy.utils.data import get_pkg_data_filename

from astropy.io import fits

import imageio
import matplotlib
import matplotlib.pyplot as plt

from PIL import Image

yvals=[]  
reader = imageio.get_reader('TrimmedBetel.mp4')
firstframe = ndimage.measurements.center_of_mass(reader.get_next_data())
for i, im in enumerate(reader):
    brightest = ndimage.measurements.center_of_mass(im)
    ypoint = [math.sqrt((float(brightest[0]-firstframe[0])**2)+(float(brightest[1]-firstframe[1])**2))]
    yvals.append(ypoint)
    
#Plot the sqrt(x^2+y^2) on the y axis and the image number on the x axis.
#This will help us see how well the telescope is pointing based on how straight- 
#this line is (ie how much the center of the star is moving.)
def create_graph(yvals):
    xaxis = np.arange(np.size(yvals))
    plt.xticks(np.arange(min(xaxis), max(xaxis)+1, 25.0))
    #plt.yticks(np.arange(min(yvals), max(yvals[i])+1, 1))
    plt.xlabel('Frame Number')
    plt.ylabel('Star Displacement')
    
    
  
    
    fig, (ax0, ax1) = plt.subplots(2, 1)
    ax0.plot((xaxis), (yvals))
    ax1.psd(np.array(yvals).flatten())

    plt.savefig("twographs.png")
#call functions here
create_graph(yvals)

