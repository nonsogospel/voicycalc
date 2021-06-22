# Code written by nonsogospel
from django.shortcuts import render, redirect
import speech_recognition as sr
import pyttsx3
import datetime
from calculator.factorial import fact
import re
from calculator.basic_calculation import (
    add, sub, multiply, divide
)
from calculator.functions_for_power_calculation import (find_sqrt, 
    cube_root,
    power,
    square,
    cube,
)
from calculator.trigonometry import (
    sin_value, sinh_value,
    cos_value, cosh_value,
    tan_value, tanh_value,
    log,
)


# Create your views here.
def index(request):
    return render(request, 'index.html')

# if request.method == 'POST' and 'run_script' in request.POST:
#     from path_to_script import function_to_run
#     function_to_run()
#     return HttpResponde

# View for the Voice Calculator
def voice_calculator(request):
    return render(request, 'voice_calculator.html')

# View for the button below the Voice Calculator
def run_script(request):
    import pythoncom
    pythoncom.CoInitialize()
    print("Your Speech Recognition version is: " + sr.__version__)
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[len(voice) - 1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-62)
    
    def response(audio):
        print(f"Calc: {audio}")
        engine.say(audio)
        engine.runAndWait()
        
    def my_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening....")
            audio = r.listen(source)
            
        try:
            command = r.recognize_google(audio, language="en-in")
            print(f"User: {command}" + '\n')
        except sr.UnknownValueError:
            response("Opps, Sorry! Didn't Get That. Kindly go back to the Homepage to start all over again. Thanks")
            command = str(input('command: '))
        return command
        
    def greeting():
        curr_time = int(datetime.datetime.now().hour)
        if curr_time >= 0 and curr_time < 12:
            response("Hello there, Morning!, Say something")
        if curr_time >= 12 and curr_time < 17:
            response("Hello there, Afternoon! Say something")
        if curr_time >= 17 and curr_time != 0:
            response("Hello there, Evening! Say something")
    # greeting()


    greeting()
    command = my_command()
    command = command.lower()

    if "+" in command or "sum" in command or "add" in command:
        res = add(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Total is: {res}")

    if "-" in command or "minus" in command or "substract" in command:
        res = sub(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Result is: {res}")

    if 'multiply' in command or "product" in command:
        res = multiply(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Product is: {res}")

    if "divide by" in command or "division" in command:
        nums = list(map(str, re.findall(r"[-+]?\d*\.?\d+", command)))
        # if 0 in nums[1:]:
        #     response("Divisin by 0 is not valid expression.")
        # else:
        res = divide(nums)
        response(f"Result is: {res}")

    if "square" in command:
        res = square(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Square is: {res}")

    if "cube of" in command:
        res = cube(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Cube is {res}")

    if "r" in command:
        res = find_sqrt(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Square root is: {res}")

    if "is to the power" in command or "power" in command:
        res = power(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Result is {res}")

    if "cube root" in command:
        res = cube_root(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Cube root is: {res}")

    if "factorial" in command:
        res = fact(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Factorial is: {res}")

    if re.search("sine of", command):
        res = sin_value(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Sine value is: {res}")

    if re.search("cos of", command):
        res = cos_value(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Cos value is: {res}")

    if re.search("tan of", command):
        res = tan_value(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Tan value is: {res}")

    if re.search("hyperbolic sine", command):
        res = sinh_value(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Hyperbolic sine is: {res}")

    if re.search("hyperbolic cos", command):
        res = cosh_value(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Hyperbolic cos is: {res}")

    if re.search("hyperbolic tan", command):
        res = tanh_value(list(map(str, re.findall(r"[-+]?\d*\.?\d+", command))))
        response(f"Hyperboic tan is: {res}")

    if re.search("log of", command):
        num = list(map(str, re.findall(r"[-+]?\d*\.?\d+", command)))
        res = log(num)
        response(f"Log of {num[0]} base {num[1]} is: {res}")
    
    return render(request, 'success.html')

def help_script(request):
    import pythoncom
    pythoncom.CoInitialize()
    test = "Here are the command for how to use the different operator: plus, minus, multipy, divide by, square, is to the power, cube root, factorial, sine of, tan of, log of, r for square root. for example 3 plus 4, 4 minus 3, 3 multiply 5 and so on. You Grab Right?  "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    print("i have a dream")
    engine.say(test)
    engine.runAndWait()
    return render(request, 'voice_calculator.html')
# def success(request):
#     return render(request, )
    