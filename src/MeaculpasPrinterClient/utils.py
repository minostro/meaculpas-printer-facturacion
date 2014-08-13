#!/usr/bin/python

from logging import Formatter
from datetime import date

ADMINS = ['minostro@crecelibre.cl', 'aotarola@crecelibre.cl']

def register_error_logger(app):
    if not app.debug:
        import logging
        from logging.handlers import SMTPHandler
        mail_handler = SMTPHandler(
            ('smtp.gmail.com','587'),
            '[Sistema Impresion] ' + date.today().strftime("%d-%m-%Y"),
            ADMINS,
            'Error!',
            ('sistema@crecelibre.cl', 's1st3m4'),
            tuple()
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)    
    
        mail_handler.setFormatter(Formatter('''
                Message type:       %(levelname)s
                Location:           %(pathname)s:%(lineno)d
                Module:             %(module)s
                Function:           %(funcName)s
                Time:               %(asctime)s
                
                Message:
                
                %(message)s
            ''')
        )

