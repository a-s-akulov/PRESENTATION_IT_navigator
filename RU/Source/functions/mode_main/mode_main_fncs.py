def changes_save(self):
    print("SAVE ME, PLEASE!")




def findMask(self, index=-1, value=""):
    if index != -1:
        for idx, x in enumerate(self.MASKTYPES):
            if x[0] == index:
                return idx
        return -1
    elif value != "":
        for idx, x in enumerate(self.MASKTYPES):
            if x[1] == value:
                return idx
        return -1




def findHostType(self, index=-1, value=""):
    if index != -1:
        for idx, x in enumerate(self.HOSTTYPES):
            if x[0] == index:
                return idx
        return -1
    elif value != "":
        for idx, x in enumerate(self.HOSTTYPES):
            if x[1] == value:
                return idx
        return -1



def mode_main_getHosts(self, shop):
    hosts = []
    shopId = self.SHOPS[shop][0]
    for x in self.HOSTS:
        if x[0] == shopId:
            arr = []
            string = ""
            for idx, x2 in enumerate(x):
                if idx == 0:
                    continue
                if x2 == None:
                    string = ""
                else:
                    if idx == 2:
                        string = self.MASKTYPES[findMask(self, index = int(x2))][1]
                    elif idx == 5:
                        string = self.HOSTTYPES[findHostType(self, index = int(x2))][1]
                    elif idx == 7:
                        string = str(x2).split(sep=".")[0]
                    else:
                        string = str(x2).strip()
                arr.append(string)
            hosts.append(arr)
    return hosts