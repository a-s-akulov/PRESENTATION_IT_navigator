def firstDraw(self):
    import os
    import tkinter as tk
    import win32api
    import win32net
    import other_gui_fncs
    import shopslist_fncs

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    root = tk.Tk()
    root.state('zoomed')
    root.minsize(900, 500)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, minsize=25)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, minsize=25)

    headMenu_frame      = tk.Frame(root)
    headMenu_frame.grid         (row=0, column=0, sticky="nswe")
    tk.Frame(root, highlightcolor="#000000", highlightbackground="#000000", highlightthickness=1).grid(row=1, column=0, sticky="we") # Чёрточка
    main_frame          = tk.Frame(root)
    main_frame.grid             (row=2, column=0, sticky="nswe")
    down_frame          = tk.Frame(root)
    down_frame.grid             (row=3, column=0, sticky="nswe")


    # HEAD MENU
    headMenu_button_file        = tk.Button(headMenu_frame, text="Файл", bd=0)
    headMenu_button_loadlist    = tk.Button(headMenu_frame, command= lambda: shopslist_fncs.shoplist_update(self), text="Загрузить список магазинов", bd=0)

    other_gui_fncs.setActiveButton_bind(headMenu_button_file, 0)
    other_gui_fncs.setActiveButton_bind(headMenu_button_loadlist, 0)

    headMenu_button_file.grid       (row=0, column=0, padx=2)
    headMenu_button_loadlist.grid   (row=0, column=1, padx=2)

    # DOWN MENU
    tk.Label(down_frame, text="Пользователь: ", font=("Verdana", 8)).grid(row=0, column=0, padx=2, sticky="w")
    fr1         = tk.Frame(down_frame, highlightcolor="#000000", highlightbackground="#000000", highlightthickness=1)
    fr2         = tk.Frame(down_frame, highlightcolor="#000000", highlightbackground="#000000", highlightthickness=1)
    user1Label  = tk.Label(fr1, text=" d", font=("Verdana", 8, "bold"))
    user2Label  = tk.Label(fr2, text=" d", height=0, font=("Verdana", 8, "bold"))

    user1Label["text"] = win32net.NetUserGetInfo(win32net.NetGetAnyDCName(),   self.USERNAME, 2)["full_name"]
    user2Label["text"] = "{}\\{}".format(self.DOMAIN, self.USERNAME)

    fr1.grid        (row=0, column=1, padx=2, pady=2, sticky="w")
    fr2.grid        (row=0, column=2, padx=2, pady=2, sticky="w")
    user1Label.grid ()
    user2Label.grid ()

    # !!!!!!!!!!!!! MAIN COMPOSITION !!!!!!!!!!!!!
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)

    shops_frame                 = tk.Frame(main_frame, highlightcolor="#000000", highlightbackground="#000000", highlightthickness=1)
    root.act_frame              = tk.Frame(main_frame, bg="#A9A9A9", highlightcolor="#000000", highlightbackground="#000000", highlightthickness=1)

    shops_frame.grid            (row=0, column=0, padx=2, sticky="ns")
    root.act_frame.grid         (row=0, column=1, padx=2, sticky="nswe")

        # SHOPS FRAME CONFIGURE
    tk.Label                    (shops_frame, text="Список магазинов:").grid(row=0, column=0, padx=2, pady=5, sticky="w")
    shopsCount_frame            = tk.Frame(shops_frame)
    shopsCount_frame.grid       (row=2, column=0, padx=2, pady=5, sticky="we")
    shopsCount_frame.grid_columnconfigure(1, weight=1)
    tk.Label                    (shopsCount_frame, text="Магазинов:", font=("Verdana", 8, "bold")).grid(row=0, column=0, sticky="w")
    root.shopsCount_label       = tk.Label(shopsCount_frame, text="0", font=("Verdana", 8, "bold"))
    root.shopsCount_label.grid  (row=0, column=1, sticky="e")

            # SHOPS LIST
    shops_frame.grid_rowconfigure(1, weight=1)

    shopsList_frame             = tk.Frame(shops_frame, highlightcolor="#000000", highlightbackground="#000000", highlightthickness=1)
    shopsList_frame.grid_rowconfigure(0, weight=1)
    shopsList_frame.grid_columnconfigure(0, weight=2)
    shopsList_frame.grid        (row=1, column=0, padx=2, sticky="nswe")

    self.shops_list             = tk.Listbox(shopsList_frame, selectmode=tk.SINGLE, exportselection=False, bd=0, highlightcolor="SystemButtonFace")
    self.shops_list.grid        (row=0, column=0, sticky="nswe")

    shops_scroll                = tk.Scrollbar(shopsList_frame, orient='vertical', command=self.shops_list.yview)
    shops_scroll.grid           (row=0, column=1, sticky="ns")

    self.shops_list['yscrollcommand'] = shops_scroll.set
    self.shops_list.bind("<<ListboxSelect>>", lambda event: shopslist_fncs.shoplist_select(self, event))
    self.shops_list.bind("<KeyPress>", lambda event: shopslist_fncs.shoplist_keyNavigate(self, event))

    return root