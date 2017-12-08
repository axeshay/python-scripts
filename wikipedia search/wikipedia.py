import webbrowser,sys
if(len(sys.argv)>1):
	address = " ".join(sys.argv[1:])
	
	
webbrowser.open("https://en.wikipedia.org/wiki/" + address)
