from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()

@nav.navigation()
def navigation_bar():
    return Navbar(
        "SIEA",
        View("Home", "index"),
        View("Events", "events"),
        View("About", "about"),
        View("Social Media", "social")
    )

def navigation_init(app):
    nav.init_app(app)
