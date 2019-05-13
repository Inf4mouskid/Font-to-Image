
import sys

from ui.window import PSFontWindow
from collections import OrderedDict

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

cmd_line_args = OrderedDict()
for arg in sys.argv[1:]:
  arg_parts = arg.split("=", 1)
  if len(arg_parts) == 1:
    cmd_line_args[arg_parts[0]] = None
  else:
    cmd_line_args[arg_parts[0]] = arg_parts[1]

qApp = QApplication(sys.argv)
window = PSFontWindow(cmd_line_args=cmd_line_args)
sys.exit(qApp.exec_())