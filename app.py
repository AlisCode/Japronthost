# coding: utf-8

from japronto import Application
import Japronthost 

app = Application();

# Let Pronthost setup the routes !
Japronthost.setup_routes(".",app.router);

# Runs the application
app.run(debug=True);
