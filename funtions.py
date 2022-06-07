import pymongo

def getDB():
    try:
        client = pymongo.MongoClient("mongodb+srv://PapaOso:slavechanescanon@cluster0.xd27o.mongodb.net/Classlinks?retryWrites=true&w=majority")
        db = client.Classlinks
    except:
        print("Error de conecxion")
    return db

def insertNoteDB(note):
    db=getDB()
    result=db.DB.insert_one(note)
    
def insertNoteSO(note):
    db=getDB()
    result=db.SO.insert_one(note)

def insertNoteCE(note):
    db=getDB()
    result=db.CE.insert_one(note)
    
def insertNoteLP(note):
    db=getDB()
    result=db.LP.insert_one(note)