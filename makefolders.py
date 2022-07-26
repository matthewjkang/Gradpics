import os

#Create the PHOTOS folder in your directory if it does not already exist
if not os.path.exists('PHOTOS'):
    os.mkdir('PHOTOS')

photos_path = os.path.abspath('PHOTOS') #Create a variable to your PHOTOS folder path
album_names = ['101','102','201','202','301','302','701','702']

# The code below creates a file hierarchy that should look like this :
# > PHOTOS 
#       >  101 
#       >  102 
#       >  201 
#       >  202 
#       >  301 
#       >  302 
#       >  701
#       >  702
all_album_paths = [] 
for i in album_names:
    album_path = os.path.join(photos_path,i)
    all_album_paths.append(album_path)

    if not os.path.exists(album_path):
        os.mkdir(album_path)
