class Enemies:
    def __init__(self, type, modifier):
        self.type = type
        self.modifier = modifier

    def __str__(self):
        return str(self.type)