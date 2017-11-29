#! python3
# webmap.py - Launches a map in the browser using an address from the
# command line or clipboard.

import sys,webbrowser,pyperclip
if(len(sys.argv) > 1):
    address = " ".join(sys.argv[1:]) #because it gives us list so we
                                        #convert into single string value excluding program name
else:
    address = pyperclip.paste()
webbrowser.open("www.google.com/maps/place/" + address)
    
