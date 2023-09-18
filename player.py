class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def _get_score(self):
        return self._score

    def _set_score(self, score):
        if score > 0:
            self._score = score
            print("Score: {}".format(self._score))
        else:
            self._score = 0
            print("Score may not be negative")

    score = property(_get_score, _set_score)

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        diff = self._score + ((level - self._level) * 1000)
        if level > 0:
            self._set_score(diff)
            self._level = level
        else:
            self._level = 0
            print("Level may not be negative")

    level = property(_get_level, _set_level)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}" \
            .format(self)
