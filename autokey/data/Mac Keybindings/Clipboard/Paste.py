winClass = window.get_active_class()

if winClass == "gnome-terminal-server.Gnome-terminal" or winClass == "terminator.Terminator":
    keyboard.send_keys("<ctrl>+<shift>+v")
else:
    keyboard.send_keys("<ctrl>+v")
