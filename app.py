# coding: utf-8

from japronto import Application
import Pronthost

app = Application();

# Let Pronthost setup the routes !
Pronthost.setup_routes(".",app.router);

# Runs the application
app.run(debug=True);
