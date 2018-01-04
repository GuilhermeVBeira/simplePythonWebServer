import os

DOCUMENT_ROOT =  os.path.abspath(os.path.dirname( __file__ ))
TEMPLATE_ROOT = os.path.join(DOCUMENT_ROOT, 'views/')
STATIC_ROOT = os.path.join(DOCUMENT_ROOT, 'static/')
CONNECTION_STRING = 'sqlite:///database.db'