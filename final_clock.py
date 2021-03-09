import board
import neopixel
import time
from gpiozero import Button

#intialize the LEDs
pixels = neopixel.NeoPixel(board.D18,150,brightness=0.2,auto_write = False)
#The lists that standardize the LED numbers to make displaying numbers easier
digit0 = [0,13,14,27,28,1,12,15,26,29,2,11,16,25,30,3,10,17,24,31,4,9,18,23,32,5,8,19,22,33,6,7,20,21,34]
digit1 = [41,42,55,56,69,40,43,54,57,68,39,44,53,58,67,38,45,52,59,66,37,46,51,60,65,36,47,50,61,64,35,48,49,62,63]
digit2 = [83,84,97,98,111,82,85,96,99,110,81,86,95,100,109,80,87,94,101,108,79,88,93,102,107,78,89,92,103,106,77,90,91,104,105]
digit3 = [112,125,126,139,140,113,124,127,138,141,114,123,128,137,142,115,122,129,136,143,116,121,130,135,144,117,120,131,134,145,118,119,132,133,146]
#Military vs AM/PM Display
status = True

#Function to swap format options
def swap():
    global status
    #Military is True AM/PM is False
    if(status == True):
        status = False
    elif(status == False):
        status = True

#The number display functions, use a list to light up eqiuvalent LEDs to standard position to make a pixel number
def zero(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[1]] = (255,0,0)
    pixels[matrix[2]] = (255,0,0)
    pixels[matrix[3]] = (255,0,0)
    pixels[matrix[5]] = (255,0,0)
    pixels[matrix[9]] = (255,0,0)
    pixels[matrix[10]] = (255,0,0)
    pixels[matrix[13]] = (255,0,0)
    pixels[matrix[14]] = (255,0,0)
    pixels[matrix[15]] = (255,0,0)
    pixels[matrix[17]] = (255,0,0)
    pixels[matrix[19]] = (255,0,0)
    pixels[matrix[20]] = (255,0,0)
    pixels[matrix[21]] = (255,0,0)
    pixels[matrix[24]] = (255,0,0)
    pixels[matrix[25]] = (255,0,0)
    pixels[matrix[29]] = (255,0,0)
    pixels[matrix[31]] = (255,0,0)
    pixels[matrix[32]] = (255,0,0)
    pixels[matrix[33]] = (255,0,0)
    pixels.show()

def one(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[2]] = (255,0,0)
    pixels[matrix[6]] = (255,0,0)
    pixels[matrix[7]] = (255,0,0)
    pixels[matrix[12]] = (255,0,0)
    pixels[matrix[17]] = (255,0,0)
    pixels[matrix[22]] = (255,0,0)
    pixels[matrix[27]] = (255,0,0)
    pixels[matrix[31]] = (255,0,0)
    pixels[matrix[32]] = (255,0,0)
    pixels[matrix[33]] = (255,0,0)
    pixels.show()

def two(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[1]] = (255,0,0)
    pixels[matrix[2]] = (255,0,0)
    pixels[matrix[3]] = (255,0,0)
    pixels[matrix[5]] = (255,0,0)
    pixels[matrix[9]] = (255,0,0)
    pixels[matrix[14]] = (255,0,0)
    pixels[matrix[17]] = (255,0,0)
    pixels[matrix[18]] = (255,0,0)
    pixels[matrix[21]] = (255,0,0)
    pixels[matrix[25]] = (255,0,0)
    pixels[matrix[30]] = (255,0,0)
    pixels[matrix[31]] = (255,0,0)
    pixels[matrix[32]] = (255,0,0)
    pixels[matrix[33]] = (255,0,0)
    pixels[matrix[34]] = (255,0,0)
    pixels.show()

def three(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[0]] = (255,0,0)
    pixels[matrix[1]] = (255,0,0)
    pixels[matrix[2]] = (255,0,0)
    pixels[matrix[3]] = (255,0,0)
    pixels[matrix[4]] = (255,0,0)
    pixels[matrix[9]] = (255,0,0)
    pixels[matrix[13]] = (255,0,0)
    pixels[matrix[17]] = (255,0,0)
    pixels[matrix[18]] = (255,0,0)
    pixels[matrix[24]] = (255,0,0)
    pixels[matrix[25]] = (255,0,0)
    pixels[matrix[29]] = (255,0,0)
    pixels[matrix[31]] = (255,0,0)
    pixels[matrix[32]] = (255,0,0)
    pixels[matrix[33]] = (255,0,0)
    pixels.show()

def four(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[3]] = (255,0,0)
    pixels[matrix[7]] = (255,0,0)
    pixels[matrix[8]] = (255,0,0)
    pixels[matrix[11]] = (255,0,0)
    pixels[matrix[13]] = (255,0,0)
    pixels[matrix[15]] = (255,0,0)
    pixels[matrix[18]] = (255,0,0)
    pixels[matrix[20]] = (255,0,0)
    pixels[matrix[21]] = (255,0,0)
    pixels[matrix[22]] = (255,0,0)
    pixels[matrix[23]] = (255,0,0)
    pixels[matrix[24]] = (255,0,0)
    pixels[matrix[28]] = (255,0,0)
    pixels[matrix[33]] = (255,0,0)
    pixels.show()

def five(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[0]] = (255,0,0)
    pixels[matrix[1]] = (255,0,0)
    pixels[matrix[2]] = (255,0,0)
    pixels[matrix[3]] = (255,0,0)
    pixels[matrix[4]] = (255,0,0)
    pixels[matrix[5]] = (255,0,0)
    pixels[matrix[10]] = (255,0,0)
    pixels[matrix[11]] = (255,0,0)
    pixels[matrix[12]] = (255,0,0)
    pixels[matrix[13]] = (255,0,0)
    pixels[matrix[19]] = (255,0,0)
    pixels[matrix[24]] = (255,0,0)
    pixels[matrix[25]] = (255,0,0)
    pixels[matrix[29]] = (255,0,0)
    pixels[matrix[31]] = (255,0,0)
    pixels[matrix[32]] = (255,0,0)
    pixels[matrix[33]] = (255,0,0)
    pixels.show()

def six(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[2]] = (255,0,0)
    pixels[matrix[3]] = (255,0,0)
    pixels[matrix[4]] = (255,0,0)
    pixels[matrix[6]] = (255,0,0)
    pixels[matrix[10]] = (255,0,0)
    pixels[matrix[15]] = (255,0,0)
    pixels[matrix[16]] = (255,0,0)
    pixels[matrix[17]] = (255,0,0)
    pixels[matrix[18]] = (255,0,0)
    pixels[matrix[20]] = (255,0,0)
    pixels[matrix[24]] = (255,0,0)
    pixels[matrix[25]] = (255,0,0)
    pixels[matrix[29]] = (255,0,0)
    pixels[matrix[31]] = (255,0,0)
    pixels[matrix[32]] = (255,0,0)
    pixels[matrix[33]] = (255,0,0)
    pixels.show()

def seven(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[0]] = (255,0,0)
    pixels[matrix[1]] = (255,0,0)
    pixels[matrix[2]] = (255,0,0)
    pixels[matrix[3]] = (255,0,0)
    pixels[matrix[4]] = (255,0,0)
    pixels[matrix[9]] = (255,0,0)
    pixels[matrix[13]] = (255,0,0)
    pixels[matrix[17]] = (255,0,0)
    pixels[matrix[21]] = (255,0,0)
    pixels[matrix[26]] = (255,0,0)
    pixels[matrix[31]] = (255,0,0)
    pixels.show()

def eight(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[1]] = (255,0,0)
    pixels[matrix[2]] = (255,0,0)
    pixels[matrix[3]] = (255,0,0)
    pixels[matrix[5]] = (255,0,0)
    pixels[matrix[9]] = (255,0,0)
    pixels[matrix[10]] = (255,0,0)
    pixels[matrix[14]] = (255,0,0)
    pixels[matrix[16]] = (255,0,0)
    pixels[matrix[17]] = (255,0,0)
    pixels[matrix[18]] = (255,0,0)
    pixels[matrix[20]] = (255,0,0)
    pixels[matrix[24]] = (255,0,0)
    pixels[matrix[25]] = (255,0,0)
    pixels[matrix[29]] = (255,0,0)
    pixels[matrix[31]] = (255,0,0)
    pixels[matrix[32]] = (255,0,0)
    pixels[matrix[33]] = (255,0,0)
    pixels.show()

def nine(matrix):
    for x in range(35):
        pixels[matrix[x]] = (0,0,0) 
    pixels.show()
    pixels[matrix[1]] = (255,0,0)
    pixels[matrix[2]] = (255,0,0)
    pixels[matrix[3]] = (255,0,0)
    pixels[matrix[5]] = (255,0,0)
    pixels[matrix[9]] = (255,0,0)
    pixels[matrix[10]] = (255,0,0)
    pixels[matrix[14]] = (255,0,0)
    pixels[matrix[16]] = (255,0,0)
    pixels[matrix[17]] = (255,0,0)
    pixels[matrix[18]] = (255,0,0)
    pixels[matrix[19]] = (255,0,0)
    pixels[matrix[24]] = (255,0,0)
    pixels[matrix[28]] = (255,0,0)
    pixels[matrix[30]] = (255,0,0)
    pixels[matrix[31]] = (255,0,0)
    pixels[matrix[32]] = (255,0,0)
    pixels.show()

#Tell PI that GPIO 16 is connected to a button
button = Button(16)

#Infinite while loop that constantly updates clock display while running
while(True):
    #If the button is pressed format of display is swapped
    button.when_pressed = swap
    #Light up pixels to be the colon between hour side and minute side of display
    pixels[72] = (0,100,150)
    pixels[74] = (0,100,150)
    #Get the time and format it
    t = time.localtime()
    current_time = time.strftime("%H:%M",t)
    #Display time in military form
    if(status == True):
        #Light up Military indicator and turn off AM/PM indicators
        pixels[149] = (100,100,100)
        pixels[148] = (0,0,0)
        pixels[147] = (0,0,0)
        #Check the number stored in each digit of the time and display that number in that LED matrix when found
        if(int(current_time[0]) == 0):
            zero(digit0)
        elif(int(current_time[0]) == 1):
            one(digit0)
        elif(int(current_time[0]) == 2):
            two(digit0)
        if(int(current_time[1]) == 0):
            zero(digit1)
        elif(int(current_time[1]) == 1):
            one(digit1)
        elif(int(current_time[1]) == 2):
            two(digit1)
        elif(int(current_time[1]) == 3):
            three(digit1)
        elif(int(current_time[1]) == 4):
            four(digit1)
        elif(int(current_time[1]) == 5):
            five(digit1)
        elif(int(current_time[1]) == 6):
            six(digit1)
        elif(int(current_time[1]) == 7):
            seven(digit1)
        elif(int(current_time[1]) == 8):
            eight(digit1)
        elif(int(current_time[1]) == 9):
            nine(digit1)
        if(int(current_time[3]) == 0):
            zero(digit2)
        elif(int(current_time[3]) == 1):
            one(digit2)
        elif(int(current_time[3]) == 2):
            two(digit2)
        elif(int(current_time[3]) == 3):
            three(digit2)
        elif(int(current_time[3]) == 4):
            four(digit2)
        elif(int(current_time[3]) == 5):
            five(digit2)
        elif(int(current_time[3]) == 6):
            six(digit2)
        elif(int(current_time[3]) == 7):
            seven(digit2)
        elif(int(current_time[3]) == 8):
            eight(digit2)
        elif(int(current_time[3]) == 9):
            nine(digit2)
        if(int(current_time[4]) == 0):
            zero(digit3)
        elif(int(current_time[4]) == 1):
            one(digit3)
        elif(int(current_time[4]) == 2):
            two(digit3)
        elif(int(current_time[4]) == 3):
            three(digit3)
        elif(int(current_time[4]) == 4):
            four(digit3)
        elif(int(current_time[4]) == 5):
            five(digit3)
        elif(int(current_time[4]) == 6):
            six(digit3)
        elif(int(current_time[4]) == 7):
            seven(digit3)
        elif(int(current_time[4]) == 8):
            eight(digit3)
        elif(int(current_time[4]) == 9):
            nine(digit3)
    #Display time in AM/PM form
    elif(status == False):
        #Turn off all indicators so AM vs PM can be decided later
        pixels[149] = (0,0,0)
        pixels[148] = (0,0,0)
        pixels[147] = (0,0,0)
        #Convert hour from current_time into an int to be used in if statements
        tens = int(current_time[0]) * 10
        ones = int(current_time[1])
        hour = tens + ones
        #Figure out military time hour and then display that hour time in its AM/PM form as well as determine if time is in AM or PM
        if(hour == 0):
            pixels[148] = (0,0,0)
            pixels[147] = (100,100,100)
            one(digit0)
            two(digit1)
        elif(hour <= 11 and hour > 0):
            pixels[148] = (0,0,0)
            pixels[147] = (100,100,100)
            if(int(current_time[0]) == 0):
                zero(digit0)
            elif(int(current_time[0]) == 1):
                one(digit0)
            if(int(current_time[1]) == 0):
                zero(digit1)
            elif(int(current_time[1]) == 1):
                one(digit1)
            elif(int(current_time[1]) == 2):
                two(digit1)
            elif(int(current_time[1]) == 3):
                three(digit1)
            elif(int(current_time[1]) == 4):
                four(digit1)
            elif(int(current_time[1]) == 5):
                five(digit1)
            elif(int(current_time[1]) == 6):
                six(digit1)
            elif(int(current_time[1]) == 7):
                seven(digit1)
            elif(int(current_time[1]) == 8):
                eight(digit1)
            elif(int(current_time[1]) == 9):
                nine(digit1)
        elif(hour > 11):
            pixels[148] = (100,100,100)
            pixels[147] = (0,0,0)
            if(hour == 12):
                one(digit0)
                two(digit1)
            elif(hour == 13):
                zero(digit0)
                one(digit1)
            elif(hour == 14):
                zero(digit0)
                two(digit1)
            elif(hour == 15):
                zero(digit0)
                three(digit1)
            elif(hour == 16):
                zero(digit0)
                four(digit1)
            elif(hour == 17):
                zero(digit0)
                five(digit1)
            elif(hour == 18):
                zero(digit0)
                six(digit1)
            elif(hour == 19):
                zero(digit0)
                seven(digit1)
            elif(hour == 20):
                zero(digit0)
                eight(digit1)
            elif(hour == 21):
                zero(digit0)
                nine(digit1)
            elif(hour == 22):
                one(digit0)
                zero(digit1)
            elif(hour == 23):
                one(digit0)
                one(digit1)
        if(int(current_time[3]) == 0):
            zero(digit2)
        elif(int(current_time[3]) == 1):
            one(digit2)
        elif(int(current_time[3]) == 2):
            two(digit2)
        elif(int(current_time[3]) == 3):
            three(digit2)
        elif(int(current_time[3]) == 4):
            four(digit2)
        elif(int(current_time[3]) == 5):
            five(digit2)
        elif(int(current_time[3]) == 6):
            six(digit2)
        elif(int(current_time[3]) == 7):
            seven(digit2)
        elif(int(current_time[3]) == 8):
            eight(digit2)
        elif(int(current_time[3]) == 9):
            nine(digit2)
        if(int(current_time[4]) == 0):
            zero(digit3)
        elif(int(current_time[4]) == 1):
            one(digit3)
        elif(int(current_time[4]) == 2):
            two(digit3)
        elif(int(current_time[4]) == 3):
            three(digit3)
        elif(int(current_time[4]) == 4):
            four(digit3)
        elif(int(current_time[4]) == 5):
            five(digit3)
        elif(int(current_time[4]) == 6):
            six(digit3)
        elif(int(current_time[4]) == 7):
            seven(digit3)
        elif(int(current_time[4]) == 8):
            eight(digit3)
        elif(int(current_time[4]) == 9):
            nine(digit3)
