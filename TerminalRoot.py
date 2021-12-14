from tqdm import tqdm, trange
from phonenumbers import carrier
import phonenumbers
from phonenumbers import geocoder
from words import word_list
from playsound import playsound
from turtle import *
import geocoder
import folium
import cv2
import os
import re
import platform
from pynput import keyboard
import socket
import subprocess
import time
import datetime
import random
import file_converter
import youtube_downloader
import pytube
import pygame
import sys
import requests
import time
import json
import nmap
import urllib3
import numpy as np
import pyautogui

monitor = pyautogui.size()
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)


def main():
    while True:
        path = os.getcwd()
        code = input("┌──(root@Terminal)" +
                     "~" + "[" + path + "]" + "\n" + "└─$ ")
        if code == 'ping':
            host = input("Enter Website To Ping: ")
            number = input("Enter How Many Times To Ping: ")

            def ping(host):
                param = '-n' if platform.system().lower() == 'windows' else '-c'
                command = ['ping', param, number, host]
                return subprocess.call(command)
            print(ping(host))
        if code == 'cd':
            WTCD = input("Enter Directory: ")

            try:
                os.chdir(WTCD)
            except:
                print("\nDirectory does not exist!")
        if code == 'sys info':
            print("\n")
            print("Processor: " + (platform.processor()))
            print("Operating System: " + platform.system() +
                  " " + platform.version())
            print("Machine: " + platform.machine())
            print("Hostname: " + host_name)
            print("IP Address: " + host_ip)
            print(monitor)
        if code == 'whoami':
            print("root")
        if code == 'ipconf':
            print("IPv4 Address. . . . : " + host_ip)
        if code == 'date':
            print("The Local Date Is: " + time.strftime("%m/%d/%Y"))
        if code == 'time':
            print("The Local Time Is: " + time.strftime("%H-%M-%S"))
        if code == 'list':
            dir_list = os.listdir(path)
            print("Files and Directories in '", path, "' :")
            print(dir_list)
        if code == 'list -a':
            file = input("Enter The Direct File Path To Read: ")
            dir_list2 = os.listdir(file)
            print("Files and directories in '", file, "':")
            print(dir_list2)
        if code == 'echo me':
            echo = input("What Do You Want Me To Echo: ")
            print(echo)
        if code == '^z':
            exit()
        if code == 'exit':
            exit()
        if code == 'op list':
            print("Open Program List:")
            print("open notepad")
        if code == 'notepad':
            programname = ("NotePad.exe")
            subprocess.Popen(programname)
        if code == 'help':
            print(
                "Type help() for interactive help, or help(object) for help about object.")
        if code == 'help()':
            print("Welcome to Terminal [BETA] help utility!")
            print("Use 'quit' to exit.")
        if code == 'help(commands)':
            print("Commands:")
        if code == 'Run app':
            app = input("Enter The App To Run: ")
            programname = (app)
            subprocess.Popen(programname)
        if code == 'terminal -version':
            print("Terminal [BETA]")
        if code == 'clear':
            pyautogui.printInfo
        if code == 'terminal -find -number -location':
            numbr = input("Enter Phone Number: ")

            ch_nmber = phonenumbers.parse(numbr, "CH")
            print(geocoder.description_for_number(ch_nmber, "en"))

            service_nmber = phonenumbers.parse(numbr, "RO")
            print(carrier.name_for_number(service_nmber, "en"))
        if code == 'timer':
            seconds = int(input("Time: "))
            sound = ('C:\\alarm.mp3')

            print(seconds)

            for i in range(seconds):
                print(str(seconds - i) + " seconds remain")
                time.sleep(1)

            playsound(sound)
            print("Finished")
        if code == 'play':
            game = input("number guessing or hangman: ")

            if game == 'number guessing':
                with tqdm(total=100) as pbar:
                    for i in range(100):
                        time.sleep(0.1)
                        pbar.update(1)

                number = random.randrange(1, 50)
                guess = int(input("Guess a number between 1 and 10: "))

                while guess != number:
                    if guess < number:
                        print("You need to guess higher. Try again.")
                        quess = int(
                            input("\nGuess a number between 1 and 10: "))
                    else:
                        print("You need to guess higher. Try again.")
                        quess = int(
                            input("\nGuess a number between 1 and 10: "))

                print("You guessed the number!")
            if game == 'hangman':
                def get_word():
                    word = random.choice(word_list)
                    return word.upper()

                def play(word):
                    word_completion = "_" * len(word)
                    guessed = False
                    guessed_letters = []
                    guessed_words = []
                    tries = 6
                    print("Let's play Hangman!")
                    print(display_hangman(tries))
                    print(word_completion)
                    print("\n")
                    while not guessed and tries > 0:
                        guess = input(
                            "Please guess a letter or word: ").upper()
                        if len(guess) == 1 and guess.isalpha():
                            if guess in guessed_letters:
                                print("You already guessed the letter", guess)
                            elif guess not in word:
                                print(guess, "is not in the word.")
                                tries -= 1
                                guessed_letters.append(guess)
                            else:
                                print("Good job,", guess, "is in the word!")
                                guessed_letters.append(guess)
                                word_as_list = list(word_completion)
                                indices = [i for i, letter in enumerate(
                                    word) if letter == guess]
                                for index in indices:
                                    word_as_list[index] = guess
                                word_completion = "".join(word_as_list)
                                if "_" not in word_completion:
                                    guessed = True
                        elif len(guess) == len(word) and guess.isalpha():
                            if guess in guessed_words:
                                print("You already guessed the word", guess)
                            elif guess != word:
                                print(guess, "is not the word.")
                                tries -= 1
                                guessed_words.append(guess)
                            else:
                                guessed = True
                                word_completion = word
                        else:
                            print("Not a valid guess.")
                        print(display_hangman(tries))
                        print(word_completion)
                        print("\n")
                    if guessed:
                        print("Congrats, you guessed the word! You win!")
                    else:
                        print("Sorry, you ran out of tries. The word was " +
                              word + ". Maybe next time!")

                def display_hangman(tries):
                    stages = [  # final state: head, torso, both arms, and both legs
                                """
                                --------
                                |      |
                                |      O
                                |     \\|/
                                |      |
                                |     / \\
                                -
                                """,
                                # head, torso, both arms, and one leg
                                """
                                --------
                                |      |
                                |      O
                                |     \\|/
                                |      |
                                |     / 
                                -
                                """,
                                # head, torso, and both arms
                                """
                                --------
                                |      |
                                |      O
                                |     \\|/
                                |      |
                                |      
                                -
                                """,
                                # head, torso, and one arm
                                """
                                --------
                                |      |
                                |      O
                                |     \\|
                                |      |
                                |     
                                -
                                """,
                                # head and torso
                                """
                                --------
                                |      |
                                |      O
                                |      |
                                |      |
                                |     
                                -
                                """,
                                # head
                                """
                                --------
                                |      |
                                |      O
                                |    
                                |      
                                |     
                                -
                                """,
                                # initial empty state
                                """
                                --------
                                |      |
                                |      
                                |    
                                |      
                                |     
                                -
                                """
                    ]
                    return stages[tries]

                def main():
                    word = get_word()
                    play(word)
                    while input("Play Again? (Y/N) ").upper() == "Y":
                        word = get_word()
                        play(word)

                if __name__ == "__main__":
                    main()
            else:
                print("Game Not Found")
        if code == 'terminal -ytmp3':
            links = youtube_downloader.input_links()
            for link in links:
                print("Downloading...")
                filename = youtube_downloader.download_video(link, 'low')
                print("Converting...")
                file_converter.convert_to_mp3(filename)
        if code == 'whereami':
            print("You are in the earth")
        if code == 'terminal -cal':
            print("Select an operation to perform: ")
            print("1. addition")
            print("2. subtraction")
            print("3. multiplication")
            print("4. division")

            operation = input("Operation to perform (Number Only): ")

            if operation == '1':
                num1 = input("Enter the first number: ")
                num2 = input("Enter the second number: ")
                print("The sum is " + str(float(num1) + float(num2)))
            if operation == '2':
                num1 = input("Enter the first number: ")
                num2 = input("Enter the second number: ")
                print("The sum is " + str(float(num1) - float(num2)))
            if operation == '3':
                num1 = input("Enter the first number: ")
                num2 = input("Enter the second number: ")
                print("The sum is " + str(float(num1) * float(num2)))
            if operation == '4':
                num1 = input("Enter the first number: ")
                num2 = input("Enter the second number: ")
                print("The sum is " + str(float(num1) / float(num2)))
            else:
                print("Unknown operation")
        if code == 'terminal -wspkc':
            command_output = subprocess.run(
                ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

            profile_names = (re.findall(
                "All User Profile     : (.*)\r", command_output))

            wifi_list = []

            if len(profile_names) != 0:
                for name in profile_names:

                    wifi_profile = {}

                    profile_info = subprocess.run(
                        ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

                    if re.search("Security key           : Absent", profile_info):
                        continue
                    else:

                        wifi_profile["ssid"] = name

                        profile_info_pass = subprocess.run(
                            ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()

                        password = re.search(
                            "Key Content            : (.*)\r", profile_info_pass)

                        if password == None:
                            wifi_profile["password"] = None
                        else:
                            wifi_profile["password"] = password[1]

                        wifi_list.append(wifi_profile)

            for x in range(len(wifi_list)):
                print(wifi_list[x])
        if code == 'amdmin -capture':
            passww = input("Enter password: ")

            if passww == 'adminonly':
                print("!This Cannot Break Need To Close The Terminal!")
                seconds = 5

                print(seconds)

                for i in range(seconds):
                    print(str(seconds - i) + " seconds remain")
                    time.sleep(1)

                video = cv2.VideoCapture(0)

                while True:
                    check, frame = video.read()

                    print(check)
                    print(frame)
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    cv2.imshow("Capturing", gray)

                    key = cv2.waitKey(1)

                    if key == ord('q'):
                        break

                video.release()
            else:
                print("Wrong Password")
        if code == 'terminal -dc':
            domain = input("Enter domain: ")
            req = requests.get("https://"+domain)
            print(req.headers, "\n")

            ip_addr = socket.gethostbyname(domain)
            print(f"IP address of {domain} is {ip_addr}", "\n")

            req2 = requests.get("https://ipinfo.io/"+ip_addr+"/json")
            data = json.loads(req2.text)
            print("Location of "+domain+" is "+data["loc"])
            print(data)
        if code == 'terminal --help':
            print("List of commands available:")
            print(
                "terminal -dc == This will scan the subdomains of the website that you entered")
            print("terminal -wspkc == This will scan the saved wifi")
            print("terminal -cal == calculator")
            print("terminal -ytmp3 == this will save the link you entered")
            print("terminal -ps == port scanner")
        if code == 'terminal -ps':
            print("!This only works on port 443!")
            hostt = input("Enter the ip: ")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            host = hostt
            port = 443

            def portscanner(port):
                if sock.connect_ex((host, port)):
                    print("Port %d is closed" % (port))
                else:
                    print("Port %d is opened" % (port))

            portscanner(port)
        if code == 'clear':
            if platform.system() == 'Windows':
                os.system("cls")
            if platform.system() == 'Linux':
                os.system("clear")
        if code == 'nano':
            if platform.system() == 'Windows':
                os.system("cls")
                print("BUILT IN TEXT EDITOR!")
                print(
                    "If you press enter the file will be saved. The default file name was 'Terminal-nano.txt' just rename it")
                WTS = input("> ")

                myfile = open("Terminal-nano.txt", "w+")
                myfile.write(WTS)
                myfile.close()
            if platform.system() == 'Linux':
                os.system("nano")


if __name__ == "__main__":
    main()
