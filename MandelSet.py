# Python code for Mandelbrot Fractal 
  
# Import necessary libraries 
import glob
from PIL import Image 
from numpy import complex, array, conj
import colorsys 
  
# setting the width of the output image
WIDTH = 512
#Output Path (Generates Multiple Images there and then creates a .gif from them)
output = 'C:/Users/Dani/Documents/UsefulPythonScripts/Mandel_Set_Images/'
#setting iterations (how many mandelbrot images it should create)
iterations = 200
#stepsize between mandelbrot images
stepsize = 0.05
  
# a function to return a tuple of colors 
# as integer value of rgb 
def rgb_conv(i): 
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5)) 
    return tuple(color.astype(int)) 

power = 0.1

# function defining a mandelbrot 
def mandelbrot(x, y): 
    c0 = complex(x, y) 
    c = 0
    for i in range(1, 20): 
        if abs(c) > 2: 
            return rgb_conv(i) 
        c = pow(conj(c), power) + c0
    return (0, 0, 0) 

# setting starting int  
for i in range(iterations):
    # creating the new image in RGB mode 
    img = Image.new('RGB', (WIDTH, WIDTH)) 
    pixels = img.load() 

    for x in range(img.size[0]): 
    
        # displaying the progress as percentage 
        print(str(i) + ' of ' + str(iterations) + " iterations: %.2f %%" % (x / WIDTH * 100.0))  
        for y in range(img.size[1]): 
            pixels[x, y] = mandelbrot((x - (WIDTH * 0.5)) / (WIDTH / 4), 
                                        (y - (WIDTH * 0.5)) / (WIDTH / 4))
    
    # to display the created fractal after  
    # completing the given number of iterations 
    # img.show() 
    number = '%03d' % i
    img.save(output + "image_" + number + '.png', )
    power = power + stepsize

fp_in = output + "image_*.png"
fp_out = output + "image.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=50, loop=0)