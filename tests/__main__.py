# -*- coding: utf-8 -*-

import sys
import unittest

from .test_module_common import *
from .test_module_cache import *
from .test_module_api import *
from .test_module_interface import *
from .test_module_loaders import *
from .test_with_api_calls import *

unittest.main(argv=sys.argv)
