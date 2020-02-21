winClass = window.get_active_class()

if winClass == "gnome-terminal-server.Gnome-terminal" or winClass == "terminator.Terminator":
    keyboard.send_keys("<ctrl>+<shift>+c")
else:
    keyboard.send_keys("<ctrl>+c")
    