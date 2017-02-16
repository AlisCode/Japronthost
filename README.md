# Japronthost

Japronthost is a tiny module for [Japronto](https://github.com/squeaky-pl/japronto), that makes it really simple to setup a tiny FTP-Like service on a server.

---------------

# Dependencies

Japronthost relies on 
* Japronto
* python-magic

Please make sure to install these dependencies before you start using Japronthost

# Setting it up

There's not much to do !

Before you run your application, let Japronthost setup its routes, like this :
	import Pronthost
	Pronthost.setup_routes('.',app.router)

Then you just need to create .ignore files. A .ignore files contains all the files/directories you dont want anybody to access. Please make sure you only put one file per line.

That's all there is !
