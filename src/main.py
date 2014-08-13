#!/usr/bin/python
# -*- coding: cp850 -*-

from MeaculpasPrinterClient import app
from MeaculpasPrinterClient.utils import register_error_logger

if __name__ == '__main__':
    app = app.getMain()
    register_error_logger(app)
    app.run('0.0.0.0', 80, True)
