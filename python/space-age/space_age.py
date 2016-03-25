class SpaceAge:

    def __init__(self, seconds):
        self.seconds = float(seconds)

    def on_earth(self):
        return float("%.02f" % (self.seconds / 31557600))

    def on_mercury(self):
        return float("%.02f" % (self.seconds / (0.2408467 * 31557600)))

    def on_venus(self):
        return float("%.02f" % (self.seconds / (0.61519726 * 31557600)))

    def on_mars(self):
        return float("%.02f" % (self.seconds / (1.8808158 * 31557600)))

    def on_jupiter(self):
        return float("%.02f" % (self.seconds / (11.862615 * 31557600)))

    def on_saturn(self):
        return float("%.02f" % (self.seconds / (29.447498 * 31557600)))

    def on_uranus(self):
        return float("%.02f" % (self.seconds / (84.016846 * 31557600)))

    def on_neptune(self):
        return float("%.02f" % (self.seconds / (164.79132 * 31557600)))
