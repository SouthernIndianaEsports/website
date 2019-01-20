from flask_nav import Nav
from flask_nav.elements import *

nav = Nav()

@nav.navigation()
def navigation_bar():
    return Navbar(
        "SIEA",
        View("Home", "index")
    )

def navigation_init(app):
    nav.init_app(app)
