def setActiveButton(element, active, mode):
    if mode == 1:
        if active:
            element.config(bg="#87CEFA")
        else:
            element.config(bg="SystemButtonFace")
    else:
        return