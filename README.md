# Japronthost

Japronthost is a tiny module for [Japronto](https://github.com/squeaky-pl/japronto), that makes it really simple to setup a tiny FTP-Like service on a server.
Japronthost basically setup your Japronto Application's router to respond to HTTP GET requests, returning the file you want to access.

---------------

# Dependencies

Japronthost relies on 
* Japronto
* python-magic

Please make sure to install these dependencies before you start using Japronthost

# Setting it up

There's not much to do !

Before you run your application, let Japronthost setup its routes, like this :

	import Japronthost
	Japronthost.setup_routes('.',app.router)

See more code in the app.py file.

Then you just need to create .ignore files. 
* A .ignore files contains all the files/directories you dont want anybody to access. 
* Please make sure you only put one file per line. 
* A .ignore file **CAN** be empty.
* You can put as many .ignore files as you want, one per directory.

That's all there is !