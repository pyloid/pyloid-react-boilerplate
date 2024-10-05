import json
import random
from pylon import PylonApp, PylonAPI, Bridge, TrayEvent, is_production, get_resource_path


app = PylonApp(single_instance=True, icon_path="src-pylon/icons/icon.ico")


############################## Tray ################################
def on_double_click():
    print("Tray icon was double-clicked.")

app.set_tray_actions(
    {
        TrayEvent.DoubleClick: on_double_click,
    }
)
app.set_tray_menu_items(
    [
        {"label": "Show Window", "callback": app.show_main_window},
        {"label": "Exit", "callback": app.quit},
    ]
)
app.setup_tray()
####################################################################

############################## Bridge ##############################
class custom(PylonAPI):
    @Bridge(str, result=str)
    def echo(self, message):
        print(message)
        return f"Message received from Python: {message}"

    @Bridge(result=str)
    def getAppVersion(self):
        return "1.0.0"
    
    @Bridge(result=str)
    def create_window(self):
        if (is_production()):
            # production
            window = app.create_window(
                "index.html",
                title="Pylon Browser-production",
                js_apis=[custom()],
            )
        else:
            window = app.create_window(
                "http://localhost:5173",
                title="Pylon Browser-dev",
                js_apis=[custom()],
                enable_dev_tools=True,
            )
        return window.id
####################################################################


if (is_production()):
    # production
    window = app.create_window(
        "index.html",
        title="Pylon Browser-production",
        js_apis=[custom()],
    )
else:
    window = app.create_window(
        "http://localhost:5173",
        title="Pylon Browser-dev",
        js_apis=[custom()],
        enable_dev_tools=True,
    )


app.run() # run
