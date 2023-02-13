class Campaign:
    def __init__(self):
        self.name
        self.description
        self.referee
        self.players = []
        self.NPCs = []
        #add locations and shit later i guess


class GameRules:
    def __init__(self, name="", description="", valueType=None):
        self.name = name
        self.description = description
        self._valueType = type(valueType)
        self.value = valueType

    def _CanToggle(self):
        if self._valueType == type(True):
            return True
        else:
            return False

    def Toggle(self):
        if self._valueType == type(True):
            if self.value == True:
                self.value = False
            else:
                self.value = True

    def SetNumber(self, value):
        if self._valueType == type(5) and type(value) == type(5):
            self.value == value


class GeneralIP(GameRules):
    def __init__(self):
        super().__init__("General IP", "All IP can be spent on anything.",
                         True)

    def Toggle(self):
        super().Toggle()
