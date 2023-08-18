import os
from PIL import Image

dir = os.getcwd()

#creates folder for newly converted images
converteddir=os.path.join(dir,"Output")
if not os.path.isdir(converteddir):
    os.mkdir(converteddir)

#loops through the current directory
for file in os.listdir(dir):
    currentimage =os.path.join(dir, file)

    #checks if the current file actually exists
    if os.path.isfile(currentimage):
            #checks if the file is an image or not
            try:
                 image=Image.open(currentimage)
            except Exception:
                 continue
            print(os.path.split(currentimage)[1])
            image = Image.open(currentimage)
            output=os.path.join(converteddir,os.path.splitext(os.path.split(currentimage)[1])[0]+".png")
            image.save(output)