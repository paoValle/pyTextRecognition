from PIL import Image, ImageFilter
#Read image
im = Image.open( 'AB.png' )
#Display image
im.show()

#Applying a filter to the image
im_sharp = im.filter( ImageFilter.EMBOSS )
#Saving the filtered image to a new file
im_sharp.save( 'AB_sharpened.png', 'PNG' )
im_sharp.show()

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()

#Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data