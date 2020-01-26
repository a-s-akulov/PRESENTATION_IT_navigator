def struct_rebuild(self, shop_index):
    import tkinter as tk
    import other_gui_fncs
    import mode_main_fncs
    import kat_switchFrame

    shop_key                = self.SHOPS[shop_index][0]
    root                    = self.root.act_frame

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    sortInTable = 4
    sortReverseInTable = False
    try:
        table = self.mainTable
        sortInTable = table.sorted_column
        sortReverseInTable = table.sorted_columnReverse
    except:
        pass

    try:
        self.root.act_frame.child_window.destroy()
    except:
        pass

    root_frame              = tk.Frame(root, bg='#D3D3D3')
    root_frame.grid         (row=0, column=0, sticky="nswe")
    self.root.act_frame.child_window = root_frame

    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.grid_rowconfigure(1, weight=1)

    # HEAD
    head_frame              = tk.Frame(root_frame)
    head_frame.grid         (row=0, column=0, sticky="we")

    head_frame.grid_columnconfigure(0, weight=1)

        # SHOP NAME
    head_name_frame         = tk.Frame(head_frame, bg='#D3D3D3')
    head_name_frame.grid    (row=0, column=0, sticky="we")
    head_name_frame.grid_columnconfigure(0, weight=1)
    head_name_frame.grid_columnconfigure(1, weight=1)
    tk.Label(head_name_frame, text=str(self.SHOPS[shop_index][1]), font=("Verdana", 12, "bold"), bg='#D3D3D3').grid(row=0, column=0, padx=3, pady=7, sticky="w")
    tk.Label(head_name_frame, text="ID:   {}".format(self.SHOPS[shop_index][0]), font=("Verdana", 12, "bold"), bg='#D3D3D3').grid(row=0, column=1, padx=3, pady=7, sticky="e")

    # kat_switchFrame
    switcher_frame          = tk.Frame(root_frame)
    switcher_frame.grid(row=1, column=0, sticky="nswe")
    switcher_viewes         = kat_switchFrame.create(switcher_frame, ["Устройства", "Инфо"], [view_dev_create, view_info_create], paramsActions=[self, sortInTable, sortReverseInTable])

    # TAIL
    tail_frame              = tk.Frame(root_frame, bg='#D3D3D3')
    tail_frame.grid         (row=2, column=0, sticky="we")
    tail_frame.grid_columnconfigure(0, weight=1)

    save_button             = tk.Button(tail_frame, text="Сохранить изменения", command= lambda: mode_main_fncs.changes_save(self), font=("Verdana", 8, "bold"), bg="#FFDEAD")
    save_button.grid        (row=0, column=0, padx=3, pady=5, sticky="e")
    other_gui_fncs.setActiveButton_bind(save_button, 1)



def view_dev_create(root, params):
    import tkinter as tk
    import kat_table
    import other_fncs
    import mode_main_fncs

    self = params[0]
    sortInTable = params[1]
    sortReverseInTable = params[2]

    bg = root["bg"]

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, minsize=20)
    root.grid_rowconfigure(1, weight=1)

    # head control frame
    head_frame              = tk.Frame(root, bg=bg)
    head_frame.grid         (row=0, column=0, padx=3, pady=5, sticky="we")
    root.head               = head_frame


    try:
        print(self.test1, self.test2)
    except:
        pass



    # TABLE CREATE
    table_root              = tk.Frame(root, bg=root["bg"])
    table_root.grid         (row=1, column=0, padx=3, sticky="nswe")
    data                    = mode_main_fncs.mode_main_getHosts(self, self.SELECTED_SHOP)

    table                   = kat_table.create  (
        table_root, 
        columns = [
            ["IP", True],
            ["Маска", True],
            ["Порт", True],
            ["Хост", True],
            ["Тип", True],
            ["Комментарии", False],
            ["Дата изменения", True],
            ["Изменивший", True]
        ],
        DATA = data,
        onDoubleClick = lambda event, r, params: r.copyCellText(),
        onDoubleClickText = "Копировать текст ячейки",
        sortColumn = sortInTable,
        sortColumnReverse = sortReverseInTable,
        tailButtons_text = ["Удалить строку", "Добавить строку"],
        tailButtons_commands = [ print, print]
        )
    self.mainTable = table

    
    

    # tail control frame
    tail_frame              = tk.Frame(root, bg=bg)
    tail_frame.grid         (row=2, column=0, padx=3, pady=5, sticky="we")

    infoChange_chkbtn       = tk.Checkbutton(tail_frame, text="Информация об изменениях", bg=bg, activebackground=bg)
    infoChange_chkbtn.grid  (row=0, column=0, sticky="we")


def view_info_create(root, params):
    print("view_info_create")