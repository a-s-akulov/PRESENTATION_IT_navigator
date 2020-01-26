def create(
        root,
        columns = [["Колонка 1", True], ["Колонка 2", True], ["Колонка 3", True]],
        DATA = [],

        onSingleClick = None,
        onSingleClickParams = [],
        onSingleClickText = "Действие 1",
        onDoubleClick = None,
        onDoubleClickParams = [],
        onDoubleClickText = "Действие 1",
        onPKMClick = None,
        onPKMClickParams = [],
        onPKMClickText = "Действие 1",

        sortColumn = 0,
        sortColumnReverse = False,

        bg = "#808080",
        weight = 1,

        headColor = "#FFFFFF",
        headTextColor = "#000000",
        headOnMouseColor = "#87CEFA",
        headOnMouseTextColor = "#FFFFFF",
        headFont = ("Verdana", 8, "bold"),

        headStrColor = "#FFFFFF",
        headStrTextColor = "#000000",
        headStrOnMouseColor = "#87CEFA",
        headStrOnMouseTextColor = "#FFFFFF",
        headStrFont = ("Verdana", 8, "bold"),

        str1Color = "#FFDAB9",
        str1TextColor = "#000000",
        str1Font = ("Verdana", 8),

        str2Color = "#FFFFFF",
        str2TextColor = "#000000",
        str2Font = ("Verdana", 8),

        cellSelectColor = "#0000FF",
        cellSelectTextColor = "#FFFFFF",
        cellSelectFont = ("Verdana", 8, "bold"),

        xSelectColor = "DISABLED",
        xSelectTextColor = "DISABLED",
        xSelectFont = "DISABLED",

        ySelectColor = "#1E90FF",
        ySelectTextColor = "#FFFFFF",
        ySelectFont = ("Verdana", 8, "bold"),
        
        tailColor = "#98FB98",
        tailTextColor = "#FF6347",
        tailTextFont = ("Verdana", 8, "bold"),
        tailButtonsColor = "#D3D3D3",
        tailButtonsTextColor = "#000000",
        tailButtonsTextFont = ("Verdana", 9, "bold"),
        tailButtons_text = [],
        tailButtons_commands = [],
        tailButtons_cmdParams = []
        ):
    
    import tkinter as tk

    if bg == "DEFAULT":
        bg = root["bg"]

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root                = tk.Frame(root, bg=bg)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid(row=0, column=0, sticky="nswe")
    root_frame          = tk.Frame(root, bg=bg)
    root_frame.grid(row=0, column=0, sticky="nswe")
    root.root_frame     = root_frame

    # SET VARIABLES TO ROOT
    root.columns = columns
    root.DATA = DATA
    root.onSingleClick = onSingleClick
    root.onSingleClickParams = onSingleClickParams
    root.onSingleClickText = onSingleClickText
    root.onDoubleClick = onDoubleClick
    root.onDoubleClickParams = onDoubleClickParams
    root.onDoubleClickText = onDoubleClickText
    root.onPKMClick = onPKMClick
    root.onPKMClickParams = onPKMClickParams
    root.onPKMClickText = onPKMClickText
    root.sortColumn = sortColumn
    root.sortColumnReverse = sortColumnReverse
    root.bg = bg
    root.weight = weight
    root.headColor = headColor
    root.headTextColor = headTextColor
    root.headOnMouseColor = headOnMouseColor
    root.headOnMouseTextColor = headOnMouseTextColor
    root.headFont = headFont
    root.headStrColor = headStrColor
    root.headStrTextColor = headStrTextColor
    root.headStrOnMouseColor = headStrOnMouseColor
    root.headStrOnMouseTextColor = headStrOnMouseTextColor
    root.headStrFont = headStrFont
    root.str1Color = str1Color
    root.str1TextColor = str1TextColor
    root.str1Font = str1Font
    root.str2Color = str2Color
    root.str2TextColor = str2TextColor
    root.str2Font = str2Font
    root.cellSelectColor = cellSelectColor
    root.cellSelectTextColor = cellSelectTextColor
    root.cellSelectFont = cellSelectFont
    root.xSelectColor = xSelectColor
    root.xSelectTextColor = xSelectTextColor
    root.xSelectFont = xSelectFont
    root.ySelectColor = ySelectColor
    root.ySelectTextColor = ySelectTextColor
    root.ySelectFont = ySelectFont
    root.tailColor = tailColor
    root.tailTextColor = tailTextColor
    root.tailTextFont = tailTextFont
    root.tailButtonsColor = tailButtonsColor
    root.tailButtonsTextColor = tailButtonsTextColor
    root.tailButtonsTextFont = tailButtonsTextFont
    root.tailButtons_text = tailButtons_text
    root.tailButtons_commands = tailButtons_commands
    root.tailButtons_cmdParams = tailButtons_cmdParams
    del(DATA)

    # FUNCTIONS
    def sort(column):
        sorted_column = -1
        sort_reverse = False

        cellsUnselect()
        try:
            sort_reverse = root.sorted_columnReverse
            sorted_column = root.sorted_column
        except:
            sorted_column = -1
            sort_reverse = False

        if sorted_column != -1:
            element = root.columnsHead[sorted_column]
            text = root.columns[sorted_column][0]
            if sorted_column == column:
                if sort_reverse:
                    element["text"] = "{}  \\/".format(text)
                else:
                    element["text"] = "{}  /\\".format(text)
                sort_reverse = not sort_reverse
            else:
                element["text"] = text
                sort_reverse = False
        else:
            sort_reverse = sortColumnReverse
        
        element = root.columnsHead[column]
        text = root.columns[column][0]
        if sort_reverse:
            element["text"] = "{}  /\\".format(text)
        else:
            element["text"] = "{}  \\/".format(text)

        root.sorted_column = column
        root.sorted_columnReverse = sort_reverse

        root.DATA.sort(key= lambda x, idx=column: x[idx], reverse= not sort_reverse)
        root.data_rebuild()



    def onMouse(element, action):
        color_set = "DISABLED"
        colorText_set = "DISABLED"
        font_set = "DISABLED"
        str_type = -1

        if action == "ENTER":
            if element.xCoordinate == -1:
                color_set = root.headStrOnMouseColor
                colorText_set = root.headStrOnMouseTextColor
            elif element.yCoordinate == -1:
                color_set = root.headOnMouseColor
                colorText_set = root.headOnMouseTextColor
            else:
                str_type = element.str_type
                color_set = root.cellSelectColor
                colorText_set = root.cellSelectTextColor
                font_set = root.cellSelectFont
        
            if color_set != "DISABLED":
                element["bg"]=color_set
            if colorText_set != "DISABLED":
                element["fg"]=colorText_set
            if font_set != "DISABLED":
                element["font"]=font_set
                
        elif action == "LEAVE":
            if element.xCoordinate == -1 or element.yCoordinate == -1:
                element.configure(bg=element.bgDefault, fg=element.fgDefault)
                return
            
            try:
                color_set = element.bgSelected
                colorText_set = element.fgSelected
                font_set = element.fontSelected

                if color_set != "DISABLED":
                    element["bg"]=color_set
                else:
                    element["bg"]=element.bgDefault

                if colorText_set != "DISABLED":
                    element["fg"]=colorText_set
                else:
                    element["fg"]=element.fgDefault

                if font_set != "DISABLED":
                    element["font"]=font_set
                else:
                    element["font"]=element.fontDefault
            except:
                element.configure(bg=element.bgDefault, fg=element.fgDefault, font=element.fontDefault)


    def data_rebuild():
        try:
            try:
                for x in root.rowsHead:
                    x.destroy()
            except:
                pass
            try:
                for x in root.data_frames:
                    x.destroy()
            except:
                pass
            for x in root.data_cells:
                x.destroy()
        except:
            pass
        
        root.data_frames = []
        root.rowsHead = []
        data_cells = []
        str_type = 1
        for stringId, string in enumerate(root.DATA):
            label = tk.Label (root_frame, text=stringId + 1, bg=root.headStrColor, fg=root.headStrTextColor, font=root.headStrFont)
            if headStrOnMouseColor != "DISABLED" or headStrOnMouseTextColor != "DISABLED":
                label.bind("<Enter>", lambda event, lbl=label: root.onMouse(lbl, "ENTER"))
                label.bind("<Leave>", lambda event, lbl=label: root.onMouse(lbl, "LEAVE"))
            
            label.bgDefault = root.headStrColor
            label.fgDefault = root.headStrTextColor
            label.xCoordinate = -1
            label.yCoordinate = stringId
            root.rowsHead.append(label)
            label.grid(row=stringId + 1, column=0, sticky="we")

            # CREATE DATA CELLS
            string_arr = []
            if str_type == 1:
                bg = root.str1Color
                fg = root.str1TextColor
                font = root.str1Font
            elif str_type == 2:
                bg = root.str2Color
                fg = root.str2TextColor
                font = root.str2Font
            for columnId, cell in enumerate(string):
                fr = tk.Frame(root_frame, highlightcolor="#000000", highlightbackground="#000000", highlightthickness=1)
                fr.grid_columnconfigure(0, weight=1)
                label = tk.Label (fr, text=cell, bg=bg, fg=fg, font=font, anchor="w")
                if root.cellSelectColor != "DISABLED" or root.cellSelectTextColor != "DISABLED":
                    label.bind("<Enter>", lambda event, lbl=label: root.onMouse(lbl, "ENTER"))
                    label.bind("<Leave>", lambda event, lbl=label: root.onMouse(lbl, "LEAVE"))
                label.bind("<Control-KeyPress>", root.cellPressCtrl)
                label.bind("<ButtonPress-1>", root.cellClick)
                if root.onDoubleClick != None:
                    label.bind("<Double-ButtonPress-1>", lambda event: root.onDoubleClick(event, root, root.onDoubleClickParams))
                if root.onPKMClick != None:
                    label.bind("<ButtonPress-3>", lambda event: root.onPKMClick(event, root, root.onPKMClickParams))

                # END OF WORK, VARIABLES INIT
                label.bgDefault = bg
                label.fgDefault = fg
                label.fontDefault = font
                label.xCoordinate = columnId
                label.yCoordinate = stringId
                label.str_type = str_type
                root.data_frames.append(fr)
                string_arr.append(label)

                fr.grid(row=stringId + 1, column=columnId + 1, sticky="we")
                label.grid(row=0, column=0, sticky="we")

            data_cells.append(string_arr)
            if str_type == 1:
                str_type = 2
            elif str_type == 2:
                str_type = 1
        
        root.data_cells = data_cells
        root.update()
        for idx, x in enumerate(root.columnsHead):
            root.root_frame.grid_columnconfigure(idx + 1, minsize=x.winfo_width())

        # scroll inicialization and set if sorted
        try:
            root.scroll_init(root.scrolled)
        except:
            root.scroll_init()




    def scroll_init(setPos=0):
        count_rows                  = len(root.data_cells)

        if count_rows < 2:
            return

        root.root_frame.bind("<MouseWheel>", root.scroll)
        for x in root.data_cells:
            for x2 in x:
                x2.bind("<MouseWheel>", root.scroll)

        if setPos > 0:
            if root.scrolled < len(root.data_cells):
                for i in range (0, root.scrolled):
                    root.rowsHead[i].grid_forget()
                    for idx, x in enumerate(root.data_cells[i]):
                        root.data_frames[i*len(root.columns) + idx].grid_forget()
                return
        root.scrolled = 0



    def scroll(event):
        count_rows                  = len(root.data_cells)
        scrolled                    = root.scrolled
        delta                       = int(event.delta/120)

        if delta == 0 or (delta > 0 and scrolled == 0) or (delta < 0 and scrolled > count_rows - 2):
            return

        if delta < 0:
            delta = max([delta, -(count_rows - scrolled - 1)])
            for i in range(scrolled, scrolled + abs(delta)):
                root.rowsHead[i].grid_forget()
                for idx, x in enumerate(root.data_cells[i]):
                    root.data_frames[i*len(root.columns) + idx].grid_forget()
        else:
            delta = min([delta, scrolled])
            for i in range(scrolled - delta, scrolled):
                root.rowsHead[i].grid(row=i + 1, column=0, sticky="we")
                for idx, x in enumerate(root.data_cells[i]):
                    root.data_frames[i*len(root.columns) + idx].grid(row=i + 1, column=idx + 1, sticky="we")

        root.scrolled = root.scrolled - delta

        if root.scrolled != 0:
            root.scrollLabel["text"]="/\\ /\\ /\\"
        else:
            root.scrollLabel["text"]="\\/ \\/ \\/"
    


    def cellPressCtrl(event):
        element = event.widget
        if event.keycode == 67: # C english or russian
            root.copyCellText()



    def copyCellText():
        try:
            element = root.selected
            root.clipboard_clear()
            root.clipboard_append(element["text"])
        except:
            pass

    def cellsUnselect(event=None):
        try:
            selected = root.selected
            x =     selected.xCoordinate
            y =     selected.yCoordinate
            for idx, x1 in enumerate(root.data_cells):
                if idx == y:
                    for x2 in x1:
                        x2.configure(bg=x2.bgDefault, fg=x2.fgDefault, font=x2.fontDefault)
                        del(x2.bgSelected)
                        del(x2.fgSelected)
                        del(x2.fontSelected)
                else:
                    x1[x].configure(bg=x1[x].bgDefault, fg=x1[x].fgDefault, font=x1[x].fontDefault)
                    del(x1[x].bgSelected)
                    del(x1[x].fgSelected)
                    del(x1[x].fontSelected)
            del(selected.bgSelected)
            del(selected.fgSelected)
            del(selected.fontSelected)
            del(root.selected)
        except:
            pass



    def cellClick(event):
        element = event.widget
        element.focus_set()
        if root.onSingleClick != None:
            root.onSingleClick(event, root, root.onSingleClickParams)

        # disable selected widgets
        root.cellsUnselect()

        # set selected color
        x =     element.xCoordinate
        xBg =   root.xSelectColor
        xFg =   root.xSelectTextColor
        xFont = root.xSelectFont
        y =     element.yCoordinate
        yBg =   root.ySelectColor
        yFg =   root.ySelectTextColor
        yFont = root.ySelectFont
        for idx, x1 in enumerate(root.data_cells):
            if idx == y:
                for x2 in x1:
                    if yBg != "DISABLED":
                        x2["bg"] = yBg
                    if yFg != "DISABLED":
                        x2["fg"] = yFg
                    if yFont != "DISABLED":
                        x2["font"] = yFont
                    x2.bgSelected = yBg
                    x2.fgSelected = yFg
                    x2.fontSelected = yFont
            else:
                if xBg != "DISABLED":
                    x1[x]["bg"] = xBg
                if xFg != "DISABLED":
                    x1[x]["fg"] = xFg
                if xFont != "DISABLED":
                    x1[x]["font"] = xFont
                x1[x].bgSelected = xBg
                x1[x].fgSelected = xFg
                x1[x].fontSelected = xFont
        if root.cellSelectColor != "DISABLED":
            element["bg"] = root.cellSelectColor
        if root.cellSelectTextColor != "DISABLED":
            element["fg"] = root.cellSelectTextColor
        if root.cellSelectFont != "DISABLED":
            element["font"] = root.cellSelectFont
        element.bgSelected = root.cellSelectColor
        element.fgSelected = root.cellSelectTextColor
        element.fontSelected = root.cellSelectFont

        root.selected = element
        


    def tailButtonsRebuild():
        parent                  = root.tailButtons_frame
        for x in root.tailButtons:
            x.destroy()
        root.tailButtons        = []

        for idx, x in enumerate(tailButtons_text):
            btn                 = tk.Button(parent, text=x, command= lambda idx=idx: root.tailButtons_commands[idx](root, idx, root.tailButtons_cmdParams),
                bg=root.tailButtonsColor, fg=root.tailButtonsTextColor, font=root.tailButtonsTextFont)
            btn.grid            (row=0, column=idx, padx=2)
            root.tailButtons.append(btn)



    def scrollInfoUpdate():
        label                   = root.scrollInfo
        text                    = "Колесо мыши - прокрутка таблицы || ЛКМ - выбор ячейки || CTRL+C - копировать текст ячейки\n "
        textArr                 = []

        if root.onSingleClick != None:
            textArr.append("ЛКМ - {}".format(root.OnSingleClickText))
        if root.onDoubleClick != None:
            textArr.append("2xЛКМ - {}".format(root.onDoubleClickText))
        if root.onPKMClick != None:
            textArr.append("ПКМ - {}".format(root.onPKMClickText))

        for idx, x in enumerate(textArr):
            if idx != 0:
                text += " || "
            text += x
        
        label["text"]=text


    root.sort = sort
    root.onMouse = onMouse
    root.data_rebuild = data_rebuild
    root.scroll_init = scroll_init
    root.scroll = scroll
    root.cellPressCtrl = cellPressCtrl
    root.copyCellText = copyCellText
    root.cellsUnselect = cellsUnselect
    root.cellClick = cellClick
    root.tailButtonsRebuild = tailButtonsRebuild
    root.scrollInfoUpdate = scrollInfoUpdate

    root.columnsHead = []
    root_frame.bind("<ButtonPress-1>", root.cellsUnselect)

    # CREATE COLUMNS
    for idx, x in enumerate(columns):
        button = tk.Button(root_frame, text=x[0], bg=headColor, fg=headTextColor, font=headFont)
        if x[1]:
            button["command"] = lambda a=idx: sort(a)
        if headOnMouseColor != "DISABLED" or headOnMouseTextColor != "DISABLED":
            button.bind("<Enter>", lambda event, btn=button: root.onMouse(btn, "ENTER"))
            button.bind("<Leave>", lambda event, btn=button: root.onMouse(btn, "LEAVE"))

        button.bgDefault = headColor
        button.fgDefault = headTextColor
        button.xCoordinate = idx
        button.yCoordinate = -1
        root.columnsHead.append(button)
        root_frame.grid_columnconfigure(1 + idx, weight=weight)
        button.grid(row=0, column=idx+1, sticky="we")

    root.update()
    root_frame.grid_columnconfigure(0, minsize=root.columnsHead[0].winfo_height())
    tk.Label(root_frame).grid(row=0, column=0, sticky="we")
    root.sort(sortColumn)

    # TAIL PANEL
    root.grid_rowconfigure(2, minsize=20)
    tail_frame          = tk.Frame(root, bg=tailColor)
    tail_frame.grid_columnconfigure(0, weight=1)
    tail_frame.grid_columnconfigure(2, weight=1)
    tail_frame.bind("<ButtonPress-1>", root.cellsUnselect)
    tail_frame.grid(row=2, column=0, sticky="nswe")

    root.tailButtons_frame   = tk.Frame(tail_frame, bg=tailColor)
    root.tailButtons_frame.grid_rowconfigure(0, weight=1)
    root.tailButtons_frame.bind("<ButtonPress-1>", root.cellsUnselect)
    root.tailButtons_frame.grid(row=0, column=0, sticky="nswe")
    root.scrollLabel    = tk.Label(tail_frame, text="\\/ \\/ \\/", bg=tailColor, fg=tailTextColor, font=tailTextFont)
    root.scrollLabel.bind("<ButtonPress-1>", root.cellsUnselect)
    root.scrollLabel.grid(row=0, column=1, sticky="ns")
    root.scrollInfo     = tk.Label(tail_frame, bg=tailColor, fg=tailTextColor, font=tailTextFont, justify="right")
    root.scrollInfo.bind("<ButtonPress-1>", root.cellsUnselect)
    root.scrollInfo.grid(row=0, column=2, sticky="e")

    root.tailButtons     = []
    tailButtonsRebuild()
    scrollInfoUpdate()
    





    return root