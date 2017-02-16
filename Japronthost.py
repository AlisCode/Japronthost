# coding: utf-8

import os, magic

files = {};

def fileRequest(req):
	encodeMagic = magic.Magic(mime_encoding=True);
	fileMagic = magic.Magic(mime=True);
	fileEncoding = encodeMagic.from_file("." + req.path);
	mime = fileMagic.from_file("." + req.path);
	
	# Handle special cases: css,HTML,XML ...
	if req.path.endswith(".css"):
		mime = "text/css";
	elif req.path.endswith(".html"):
		mime = "text/html";
	elif req.path.endswith(".xml"):
		mime = "text/xml";

	content = "";
	if fileEncoding != 'binary':
		with open('.' + req.path, 'r', encoding=fileEncoding) as fileToRead:
			content = fileToRead.read();
		rep = req.Response(code=200,mime_type=mime,text=content, encoding=fileEncoding);
	else:
		with open('.' + req.path, 'rb') as fileToRead:
			content = fileToRead.read();
		rep = req.Response(code=200,mime_type=mime,body=content, encoding=fileEncoding);

	fileToRead.close();
	return rep;

def addFileRoute(router, fileToAdd):
	print("adding a route ", fileToAdd[1:]);
	router.add_route(fileToAdd[1:], fileRequest);

def setup_routes(currentPath, router):
	# Loads all the ignored files from the .ignore of the current dir
	ignored = [".ignore"];
	if os.path.isfile(currentPath + '/.ignore'):
		fileIgnore = open(currentPath + "/.ignore");
		for line in fileIgnore:
			ignored.append(line.strip());
		fileIgnore.close();

	# Adds a route for all the files that we dont want to ignore
	for fileScanned in os.listdir(currentPath):
		if fileScanned not in ignored:
			if os.path.isdir(currentPath + '/' + fileScanned):
				# Found a directory, scanning its files ...
				setup_routes(currentPath + '/' + fileScanned, router);
			else:
				# Found a file, adding a route ...
				addFileRoute(router, currentPath + '/' + fileScanned);
