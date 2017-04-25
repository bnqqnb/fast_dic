#! python3
#fast_dic.py - Search Dictionary from clipboard
#version 0.0.1
import requests,bs4,sys,webbrowser,tkinter,urllib
from tkinter import Tk, Label

word = ''
if len(sys.argv) > 1:
    word = ' '.join(sys.argv[1:])
else:
    #unable to use pyperclip,clipboard to copy utf-8 character from clipboard in mac so use Tk()
    temp = Tk()
    word = temp.clipboard_get()
    temp.destroy()    
url_word = urllib.parse.quote_plus(word) 
webbrowser.open('http://www.linguee.com/german-english/search?source=auto&query=' + url_word)


