'''

Library of Python projects by David Kundih.

'''

# ignore __pycache__ from forming inside the library directory.
import sys
sys.dont_write_bytecode = True

# meta data imports from the vandal library.
from kundih.misc._meta import (
    __author__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __documentation__,
    __contact__,
    __donate__,
    __APPversion__,
)

# all contents.
from logistics import *
from vandal import *
from duality import *

from kundih.objects.kmeans import KSrednjeVrijednosti
from kundih.objects.dijkstra import Dijkstra
from kundih.objects.linreg import LinearnaRegresija
from kundih.objects.montecarlo import MonteCarlo

if __name__ == '__main__':
    import importlib
    importlib.import_module('kundih')
    print('UPOZORENJE: Ova biblioteka kreirana je samo za potrebe izrade diplomskog rada sa značajkama na hrvatskom jeziku i kao takva je sadržana u verziji 0.0.7, nakon čega se koristi za ostale namjene definirane u README datoteci.')
    print('WARNING: This library is created for the sole purpose of translating particles into the croatian language and as such it is contained in the 0.0.7 version, after which it is being used for other purposes defined in the README file.')