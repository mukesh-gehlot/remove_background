# Install following module

#pip intsall rembg
#pip install easygui
#pip install pillow

from rembg import remove
import easygui
from PIL import Image

inPath = easygui.fileopenbox(title = 'Select Image file') # select image
outPath = easygui.filesavebox(title = 'Save Fil to...') #select location to save image

input = Image.open(inPath) #open the image and store into input variable
output = remove(input) # store without background image in output
output.save(outPath) #save the image in selected outpath variable