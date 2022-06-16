from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
from database_meta import DataBaseMeta


class FireBase(metaclass=DataBaseMeta):
    def __init__(self, name: str):
        self.connect()
        self.__DB = firestore.client()
        self.__name = name

    def connect(self):
        cred = credentials.Certificate("clave.json")
        firebase_admin.initialize_app(cred)

    def close_conection(self):
        pass

    def read(self):
        pass

    def write(self, txt: str, msg: str):
        time: str = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        doc: str = "[" + time + " " + "]  >> " + msg
        doc_reference = self.__DB.collection(self.__name).document(doc)
        data = {
            f'Tipo': msg,
            f'Fecha': time,
            f'Msg': txt
        }
        doc_reference.set(data)
