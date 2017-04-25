#! python3
#fast_dic.py - Search Dictionary from clipboard
import requests,bs4,sys,pyperclip,webbrowser
if len(sys.argv) > 1:
    word = ' '.join(sys.argv[1:])
else:
    word = pyperclip.paste()
    
#type(res);
#res.raise_for_status()
#noStarchSoup = bs4.BeautifulSoup(res.text)
#type(noStarchSoup)

webbrowser.open('http://www.linguee.com/german-english/search?source=auto&query=' + word)

print(word);
