class Tracks:
    def __init__(self, name, difficulty, weather, speed, handling):
        self.name = name
        self.difficulty = difficulty
        self.weather = weather
        self.speed = speed
        self.handling = handling
    def stats(self):
        return """
        %s:
        Difficulty: %.1f
        Weather: %.1f
        Speed: %.1f
        Handling: %.1f
        """ % (self.name, self.difficulty, self.weather, self.speed, self.handling)

class Track_1(Tracks):
    def __init__(self, name = "Suzuka", difficulty = 6, weather = 0, speed = 8, handling = 8):
        super().__init__(name, difficulty, weather, speed, handling)


class Track_2(Tracks):
    def __init__(self, name = "Fuji", difficulty = 9, weather = 8, speed = 4, handling = 3):
        super().__init__(name, difficulty, weather, speed, handling)


class Track_3(Tracks):
    def __init__(self, name = "Inagawa", difficulty = 12, weather = 5, speed = 3, handling = 5):
        super().__init__(name, difficulty, weather, speed, handling)


class Track_4(Tracks):
    def __init__(self, name = "Tsukuba", difficulty = 15, weather = 0, speed = 7, handling = 4):
        super().__init__(name, difficulty, weather, speed, handling)