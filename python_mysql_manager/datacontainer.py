class DataContainer:

    def __init__(self, status: bool, message: str = "", code: int = 200):
        self.status = status
        self.message = message
        self.code = code
        self.data = []
        self.lastInsertId = None

    def setData(self, data: list):
        self.data = data

    def getData(self) -> list:
        return self.data

    def setLastInsertId(self, lastInsertId):
        self.lastInsertId = lastInsertId

    def getLastInsertId(self):
        return self.lastInsertId

    def getStatus(self) -> bool:
        return self.status

    def getMessage(self) -> str:
        return self.message

    def getCode(self) -> int:
        return self.code
