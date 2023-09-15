from netwix.__init__ import __version__
from netwix.types import Movies, Series

def testVers():
    assert __version__ == '0.1.8'

def testMovies():
    movie = Movies("81161626")
    assert movie.name == 'Red Notice'

def testSeries():
    serie = Series("70126228")
    assert serie.name == 'The Office'
