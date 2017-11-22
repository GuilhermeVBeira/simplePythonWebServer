import sys, os

DOCUMENT_ROOT =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', ''))
TEMPLATE_ROOT = os.path.join(DOCUMENT_ROOT, 'views/')
DATA_BASE = 'sqlite:///database.db'
# DATA_BASE = 'mysql+pymysql://user:pass@host/database'