# coding: utf-8

from japronto import Application
import Pronthost as pronthost

app = Application();

pronthost.setup_routes(".",app.router);

# Runs the application
app.run(debug=True);
