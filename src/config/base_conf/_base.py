# flake8: noqa
# isort: skip_file

# some imports are unused here, but used commonly between
# environment specific files, so we import here for convenience
from . import *

# configs that cannot have a secure default, e.g. SECRET KEY,
# are set in the specific environment config files.

# read configs from the module all dunder, so that we can add
# breaking changes whitout deprecating or exposing them right away
from .django import *
from .database import *
from .localization import *
# from .logging import *
# from .external import *
from .routing import *
