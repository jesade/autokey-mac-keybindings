winClass = window.get_active_class()

if winClass.find(".Google-chrome") > -1:
    keyboard.send_keys("<ctrl>+<shift>+w")
else:
    keyboard.send_keys("<ctrl>+q")
    

