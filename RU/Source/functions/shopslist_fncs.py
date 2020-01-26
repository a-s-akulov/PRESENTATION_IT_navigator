
def shoplist_update(self):
    import other_fncs
    import tkinter as tk
    import pyodbc

    self.SHOPS.clear()
    self.HOSTS.clear()
    shops_bk        = []

    # SQL QUERY
    try:
        conn = pyodbc.connect(r'Driver={SQL Server};Server=mailserver\newbooksql;Database=ServiceDesk;Trusted_Connection=yes;')
        cur = conn.cursor()
    except:
        other_fncs.fatal_error(self, "Can't connect with 'mailserver\newbooksql'")
        return

    # SHOPS MAIN
    try:
        cur.execute("SELECT PT_ID, PT_SHORTNAME FROM dbo.PARTNERS where TP_ID != 10")
    except:
        other_fncs.fatal_error(self, "Can't execute query 'SELECT PT_ID, PT_SHORTNAME FROM dbo.PARTNERS where TP_ID != 10'")
        return

    while True:
        row = cur.fetchone()
        if not row:
            break
        self.SHOPS.append(row)

    # SHOPS BK
    try:
        cur.execute("SELECT PT_ID, PT_SHORTNAME FROM dbo.PARTNERS where TP_ID = 10")
    except:
        other_fncs.fatal_error(self, "Can't execute query 'SELECT PT_ID, PT_SHORTNAME FROM dbo.PARTNERS where TP_ID = 10'")
        return

    while True:
        row = cur.fetchone()
        if not row:
            break
        shops_bk.append(row)

    # HOSTS
    try:
        cur.execute("SELECT * FROM dbo.IPADRESES")
    except:
        other_fncs.fatal_error(self, "Can't execute query 'SELECT * FROM dbo.IPADRESES'")
        return
    
    while True:
        row = cur.fetchone()
        if not row:
            break
        self.HOSTS.append(row)

    # MASKS
    try:
        cur.execute("SELECT * FROM dbo.MASKTYPES")
    except:
        other_fncs.fatal_error(self, "Can't execute query 'SELECT * FROM dbo.MASKTYPES'")
        return
    
    while True:
        row = cur.fetchone()
        if not row:
            break
        self.MASKTYPES.append(row)

    # HOSTYPES
    try:
        cur.execute("SELECT * FROM dbo.HOSTTYPES")
    except:
        other_fncs.fatal_error(self, "Can't execute query 'SELECT * FROM dbo.HOSTTYPES'")
        return

    while True:
        row = cur.fetchone()
        if not row:
            break
        self.HOSTTYPES.append(row)




    try:
        conn.close()
    except:
        pass
    # CALC_OPERATIONS
    self.SHOPS.sort(key= lambda name: name[1])
    shops_bk.sort(key= lambda name: name[1])
    self.SHOPS.extend(shops_bk)
    shops_bk = None

    # GUI
    self.shops_list.delete(0, tk.END)
    maxCcount = 0
    for x in self.SHOPS:
        self.shops_list.insert(tk.END, x[1])
        if len(x[1]) > maxCcount:
            maxCcount = len(x[1])


    self.root.shopsCount_label["text"] = len(self.SHOPS)
    self.shops_list["width"] = maxCcount

    self.shops_list.select_set(0)
    self.shops_list.activate(self.SELECTED_SHOP)
    self.shops_list.event_generate("<<ListboxSelect>>")
    self.shops_list.focus_force()




def shoplist_select(self, event):
    import mode_main_gui

    if 0 < len(self.SHOPS):
        widget = event.widget
        try:
            selection=widget.curselection()
            self.SELECTED_SHOP = int(selection[0])

            if self.MODE == 0:
                mode_main_gui.struct_rebuild(self, self.SELECTED_SHOP)
        except:
            raise




def shoplist_keyNavigate(self, event):
    import time

    if event.keysym == "Up":
        if self.SELECTED_SHOP > 0:
            self.shops_list.select_clear(self.SELECTED_SHOP)
            self.SELECTED_SHOP -= 1
            self.shops_list.select_set(self.SELECTED_SHOP)
            self.shops_list.event_generate("<<ListboxSelect>>")
            

    elif event.keysym == "Down":
        if self.SELECTED_SHOP < (len(self.SHOPS) - 1):
            self.shops_list.select_clear(self.SELECTED_SHOP)
            self.SELECTED_SHOP += 1
            self.shops_list.select_set(self.SELECTED_SHOP)
            self.shops_list.event_generate("<<ListboxSelect>>")
            
    
    elif event.char in self.characterset and (len(event.keysym) == 1 or event.keysym == "??") or event.keysym == "space":
        key = event.char.lower()
        time = time.time()
        if (self.FINDER_HANDLE[1] + 1) > time:
            self.FINDER_HANDLE[0] += key
        else:
            self.FINDER_HANDLE[0] = key
        self.FINDER_HANDLE[1] = time
        shop_id, index = shoplist_findShop(self, 0, self.FINDER_HANDLE[0])

        if index != -1:
            self.shops_list.select_clear(self.SELECTED_SHOP)
            self.SELECTED_SHOP = index
            self.shops_list.select_set(self.SELECTED_SHOP)
            self.shops_list.activate(self.SELECTED_SHOP)
            self.shops_list.event_generate("<<ListboxSelect>>")
            self.shops_list.focus_force()
            self.shops_list.yview(self.SELECTED_SHOP)
            




def shoplist_findShop(self, mode, handle):
    if mode == 0:
        for idx, x in enumerate(self.SHOPS):
            if handle in x[1].lower():
                return x[0], idx
        return -1, -1