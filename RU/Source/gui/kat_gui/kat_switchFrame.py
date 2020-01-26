def create(root, buttonsText, buttonsActions, paramsActions=[], selected=0, bd=0, weight=1, bgColor="#D3D3D3", placeColor="DEFAULT", frameColor="#FFFFFF", onMouseColor="#87CEFA", outMouseColor="#FFDEAD", textColor="#000000", font=("Verdana", 8, "bold")):
    import tkinter as tk

    if placeColor == "DEFAULT":
        placeColor = bgColor

    def actRun(selected):
        buttonsActions[selected](root.place, paramsActions)

    def structRebuild(selected, isScript=False):
        if selected == root.selected and not isScript:
            return

        try:
            root.place.destroy()
        except:
            pass

        place               = tk.Frame(root.act_frame, bg=placeColor)
        place.grid          (row=0, column=0, sticky="nswe")
        root.place          = place

        old_select          = root.selected
        root.selected       = selected

        element             = root.buttons[old_select]
        element["bg"]       = outMouseColor
        element.bind("<Enter>", lambda event, x=element: setActiveButton(True, x))
        element.bind("<Leave>", lambda event, x=element: setActiveButton(False, x))

        element             = root.buttons[selected]
        element["bg"]       = frameColor
        element.unbind("<Enter>")
        element.unbind("<Leave>")

        actRun(selected)

    def setActiveButton(active, element):
        if active:
            element.config(bg=onMouseColor)
        else:
            element.config(bg=outMouseColor)

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
    root.grid_rowconfigure(0, weight=weight)
    root.grid_columnconfigure(0, weight=weight)

    root                    = tk.Frame(root, bg=bgColor)
    root.grid               (row=0, column=0, sticky="nswe")
    root.grid_columnconfigure(0, weight=weight)
    root.grid_rowconfigure(1, weight=weight)
    root.buttons            = []
    
    buttons_frame           = tk.Frame(root, bg=bgColor)
    buttons_frame.grid      (row=0, column=0, sticky="we")

    for idx, x in enumerate(buttonsText):
        element             = tk.Button(buttons_frame, text=buttonsText[idx], command= lambda x=idx: structRebuild(x), bg=outMouseColor, fg=textColor, font=font, bd=bd)
        element.grid        (row=0, column=0+idx, padx=3, sticky="w")

        if idx != selected:
            element.bind("<Enter>", lambda event, x=element: setActiveButton(True, x))
            element.bind("<Leave>", lambda event, x=element: setActiveButton(False, x))

        root.buttons.append(element)

    element                 = root.buttons[selected]
    element["bg"]           = frameColor


    act_frame               = tk.Frame(root, bg=bgColor, highlightcolor=frameColor, highlightbackground=frameColor, highlightthickness=3)
    act_frame.grid          (row=1, column=0, padx=3, sticky="nswe")
    act_frame.grid_rowconfigure (0, weight=weight)
    act_frame.grid_columnconfigure (0, weight=weight)
    root.act_frame          = act_frame

    root.selected           = selected
    structRebuild(selected, isScript=True)

    return root