

class SingleThreadRequestUnit(object):
    """

    """
    def __init__(self, times: int=-1, headers: list=None, proxys: list=None):
        self.times = times
        self.record = {}
        self


    def getHeaders(self):
        return []

    def getProxy(self):
        return []

    def isError(self):
        return False

    def isSuccess(self):
        return True

    def isFail(self):
        return False

    def start(self):
        pass


