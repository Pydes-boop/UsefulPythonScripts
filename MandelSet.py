# Python code for Mandelbrot Fractal

# Import necessary libraries
import sys
import glob
import os
import time
import colorsys
from PIL import Image
from numpy import complex, array, conj
from dearpygui.core import *
from dearpygui.simple import *

# Set Output Path (Generates Multiple Images there and then creates a .gif from them)
output = sys.path[0] + '/Mandel_Set_Images/'
output = output.replace('\\', '/')


# standart Values
generateOne = False
WIDTH = 512
iterations = 1
power = 2
stepsize = 0.5
mandelSetResolution = 10

commandLine = True
pyGui = False

# MandelSetCode
# if(True) just exists so i can "open/close" that part of the code in VScode (<-- is that stupid? Yes. But i dont care)
if(True):
    # a function to return a tuple of colors
    # as integer value of rgb
    def rgb_conv(i):
        color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
        return tuple(color.astype(int))

    # function defining a mandelbrot
    def mandelbrot(x, y):
        c0 = complex(x, y)
        c = 0
        for i in range(1, mandelSetResolution):
            if abs(c) > 2:
                return rgb_conv(i)
            c = pow(conj(c), power) + c0
        return (0, 0, 0)


    # change To single Image Generation
    if(generateOne):
        iterations = 1

    def mandelSet_calculation():
        # setting starting int
        for i in range(iterations):
            # creating the new image in RGB mode
            img = Image.new('RGB', (WIDTH, WIDTH))
            pixels = img.load()

            for x in range(img.size[0]):

                # displaying the progress as percentage
                print(str(i) + ' of ' + str(iterations) +
                    " iterations: %.2f %%" % (x / WIDTH * 100.0))
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
        if(generateOne == False):
            img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
            img.save(fp=fp_out, format='GIF', append_images=imgs,
                    save_all=True, duration=50, loop=0)

if(pyGui): 
    commandLine = False

    set_main_window_size(500, 500)

    def start_callback(sender, data):
        mandelSet_calculation()

    def save_callback(sender, data):
        print("Save Clicked")

    def kill_callback(sender, data):
        sys.exit("Killed Task")

    def retrieve_callback(sender, callback):
    
        show_logger()
        WIDTH = int(log_info(get_value("ImageResolution##inputtext")))
        iterations = int(log_info(get_value("ImageCount##inputtext")))
        power = float(log_info(get_value("Starting ^power for Calculation")))
        stepsize = float(log_info(get_value("Stepsize for ^power growth between Images")))
        mandelSetResolution = int(log_info(get_value("MandelSet Iterations per Calculation")))

    with window("Main Window"):
        add_text("Enter values used for Calculation")
        add_input_text("ImageResolution##inputtext", default_value="512", hint = "512", decimal=True, width=50)
        add_input_text("ImageCount##inputtext", default_value="1", hint = "1", decimal=True, width=50)
        add_input_text("Starting ^power for Calculation", default_value="2", hint = "2", decimal=True, width=50)
        add_input_text("Stepsize for ^power growth between Images", default_value="0.5", hint = "0.5", decimal=True, width=50)
        add_input_text("MandelSet Iterations per Calculation", default_value="10", hint = "10", decimal=True, width=50)
        add_button("Save", callback=save_callback)
        add_button("Start Generation", callback = start_callback)
        add_button("Kill", callback=kill_callback)

    start_dearpygui(primary_window="Main Window")

if(commandLine):
    # MultipleImages/Gif or Single Image?
    print("Started MandelSet Generator\nWould you like to generate multiple Images? >>> Yes/No/Kill")
    while(True):
        userInput = input()
        if(userInput == 'Yes' or userInput == 'yes'):
            generateOne = False
            break
        else:
            if(userInput == 'No' or userInput == 'no'):
                generateOne = True
                break
            else:
                if(userInput == 'Kill' or userInput == 'kill'):
                    sys.exit("Killed Task")
                    input("Press enter to exit...")
                else:
                    print("Invalid Input: " + userInput +
                        "\nWould you like to generate multiple Images? >>> Yes/No/Kill")

    # ImageResolution
    print("What should be the image resolution? Please enter a number...")
    while(True):
        userInput = input()
        if(userInput.isdigit):
            WIDTH = int(userInput)
            break
        else:
            if(userInput == 'Kill' or userInput == 'kill'):
                sys.exit("Killed Task")
                input("Press enter to exit...")
            else:
                print("Invalid Input: " + userInput +
                    "\nWhat should be the image resolution? Please enter a number...")

    # How Many Images to create?
    if(generateOne == False):
        print("How many Images should be created? Please enter a number...")
        while(True):
            userInput = input()
            if(userInput.isdigit):
                iterations = int(userInput)
                break
            else:
                if(userInput == 'Kill' or userInput == 'kill'):
                    sys.exit("Killed Task")
                    input("Press enter to exit...")
                else:
                    print("Invalid Input: " + userInput +
                        "\nHow many Images should be created? Please enter a number...")

        print("Please enter a number for the growth between images...")
        while(True):
            userInput = input()
            if(userInput.replace(".", "", 1).isdigit()):
                stepsize = float(userInput)
                break
            else:
                if(userInput == 'Kill' or userInput == 'kill'):
                    sys.exit("Killed Task")
                    input("Press enter to exit...")
                else:
                    print("Invalid Input: " + userInput +
                        "\nPlease enter a number for the growth between images...")

    # Potency / Power
    if(generateOne):
        print("How many fractals do you want / What should be the Power of the Mandelset Calculation?")
    else:
        print("At which Power do you want to start generating the Mandelset Images? Please enter a number...")
    while(True):
        userInput = input()
        try:
            power = int(userInput)
            is_Dig = True
        except ValueError:
            is_Dig = False
        if(is_Dig):
            break
        else:
            if(userInput == 'Kill' or userInput == 'kill'):
                sys.exit("Killed Task")
                input("Press enter to exit...")
            else:
                print("Invalid Input: " + userInput)
                if(generateOne):
                    print(
                        "How many fractals do you want / What should be the potency of the Mandelset Calculation?")
                else:
                    print("Invalid Input: " + userInput +
                        "\nAt which potency do you want to start generating the Mandelset Images? Please enter a number...")

    # MandelSet Range
    print("Enter a max number of iterations per Mandelset Pixel Calculation")
    while(True):
        userInput = input()
        if(userInput.isdigit):
            mandelSetResolution = int(userInput)
            break
        else:
            if(userInput == 'Kill' or userInput == 'kill'):
                sys.exit("Killed Task")
                input("Press enter to exit...")
            else:
                print("Invalid Input: " + userInput +
                    "\nWhat should be the image resolution? Please enter a number...")


    # create new folder for runtime so pictures dont overwrite each other
    timestr = time.strftime("%d%m%Y-%H%M%S")
    output = output + timestr + "/"
    try:
        os.mkdir(output)
    except OSError:
        sys.exit("Creation of the directory %s failed" % output)
        input("Press enter to exit...")
    else:
        print("Successfully created the directory %s " % output)

    #Generator Message
    if(generateOne == False):
        print("Generating " + str(iterations) + " images starting at ^" + str(power) + " with a growth of " +
            str(stepsize) + " in a resolution of " + str(WIDTH) + " with an iteration size per Pixel of " + str(iterations))
    else:
        print("Generating " + str(iterations) + " image with a power of ^" + str(power) +
            " in a resolution of " + str(WIDTH) + " with an iteration size per Pixel of " + str(iterations))

if(commandLine == False):
    print("Program succesfully executed\ncreated " + "%s" % iterations + "Mandelset images, starting at Power " + "%s" % power +
        " up to " + "%s" % (power+(iterations*stepsize)) + " with a resolution of " + "%s" % WIDTH + "\nsaved images to " + output)

    input("Press enter to exit...")
