from pylon import PylonApp, PylonAPI, Bridge, TrayEvent, is_production, get_production_path
import os

app = PylonApp(app_name="Pylon-App", single_instance=True)

if (is_production()):
    app.set_icon(os.path.join(get_production_path(), "icons/icon.png"))
else:
    app.set_icon("src-pylon/icons/icon.png")


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
app.run_tray()
####################################################################

############################## Bridge ##############################
class custom(PylonAPI):
    @Bridge(result=str)
    def create_window(self):
        window = app.create_window(
            title="Pylon Browser-2",
            js_apis=[custom()],
        )
        
        window.set_size(800, 600)
        window.set_position(0, 0)

        if (is_production()):
            window.set_dev_tools(False)
            window.load_file(os.path.join(get_production_path(), "build/index.html"))
        else:
            window.set_dev_tools(True)
            window.load_url("http://localhost:5173")
 
        print(window.get_all_shortcuts())

        
        
        window.show()
        window.focus()

        return window.id
####################################################################


if (is_production()):
    # production
    window = app.create_window(
        title="Pylon Browser-production",
        js_apis=[custom()],
    )
    window.load_file(os.path.join(get_production_path(), "build/index.html"))
else:
    window = app.create_window(
        title="Pylon Browser-dev",
        js_apis=[custom()],
        dev_tools=True,
    )
    window.load_url("http://localhost:5173")

window.show_and_focus()

app.run() # run
