from classes import Card,Prof

blk=""#u always need to specify global var if ure usig outer scope vars inside inner scope / inner funcs as given below, a better approach is value passing

def getCard():
    x=Card(input("title"),input("content"))
    global blk
    blk+=(x.passer())+forMatter()
    del x

    return True if "card" in input("\nenter card to create card") else False

def getProf():
    x=Prof(input("name"),input("age"),input("phone"))
    global blk
    blk+=(x.passer())+forMatter()
    del x

def writeBlk():
    f=open(input("file to save"),"w+")
    f.write(blk)
    f.close()

def forMatter():
    return "::::::::::::::::::::::::::::::::::::::::::::::::::"




