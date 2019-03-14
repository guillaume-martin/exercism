class SpaceAge(object):    
    def __init__(self, seconds):
        self.seconds = seconds
        
    @staticmethod    
    def _convert_age(self, planet):
        orbital_periods = {'Mercury':0.2408467, 'Venus':0.61519726, 'Earth':1,
                            'Mars':1.8808158, 'Jupiter':11.862615, 'Saturn':29.447498,
                            'Uranus':84.016846, 'Neptune':164.79132}

        return  round((self.seconds / 31557600) / orbital_periods[planet], 2)

    def on_mercury(self):
        return self._convert_age(self, 'Mercury')

    def on_venus(self):
        return self._convert_age(self, 'Venus')

    def on_earth(self):
        return self._convert_age(self, 'Earth')

    def on_mars(self):
        return self._convert_age(self, 'Mars')

    def on_jupiter(self):
        return self._convert_age(self, 'Jupiter')

    def on_saturn(self):
        return self._convert_age(self, 'Saturn')

    def on_uranus(self):
        return self._convert_age(self, 'Uranus')

    def on_neptune(self):
        return self._convert_age(self, 'Neptune')
