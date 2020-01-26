def setActiveButton(element, active, mode):
    if mode == 0:
        if active:
            element.config(bg="#87CEFA")
        else:
            element.config(bg="SystemButtonFace")
    else:
        return

def setActiveButton_bind(element, mode):
    element.bind("<Enter>", lambda event: setActiveButton(element, True, mode))
    element.bind("<Leave>", lambda event: setActiveButton(element, False, mode))
def setActiveButton_unbind(element):
    element.unbind("<Enter>")
    element.unbind("<Leave>")