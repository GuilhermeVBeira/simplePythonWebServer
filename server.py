from http.server import HTTPServer, BaseHTTPRequestHandler
from app.controllers import save_person, index, get_persons, get_person, delete_person, edit_person
from app.settings import TEMPLATE_ROOT, DATA_BASE
from app.models.tables import DataBase
import json
import urllib

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        f = open(TEMPLATE_ROOT + index())
   
        self.protocol_version='HTTP/1.1'
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(f.read(), 'UTF-8'))
        

    def do_POST(self):
    
        if self.path == '/getpersons':
            db = DataBase(DATA_BASE)
            pessoas = get_persons(db.session)
            # print(self.headers)
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(pessoas, 'UTF-8'))
            return
        elif self.path == '/createperson':
            db = DataBase(DATA_BASE)
            content_len = int(self.headers.get('content-length'))
            post_data = urllib.parse.parse_qs(self.rfile.read(content_len).decode('utf-8'))
            save_person(db.session, post_data)
            self.send_response(200)
            self.end_headers()
            return
        elif self.path == '/deleteperson':
            db = DataBase(DATA_BASE)
            content_len = int(self.headers.get('content-length'))
            post_data = urllib.parse.parse_qs(self.rfile.read(content_len).decode('utf-8'))
            delete_person(db.session, post_data)
            self.send_response(200)
            self.end_headers()
            return
        elif self.path == '/editperson':
            db = DataBase(DATA_BASE)
            content_len = int(self.headers.get('content-length'))
            post_data = urllib.parse.parse_qs(self.rfile.read(content_len).decode('utf-8'))
            pessoa = edit_person(db.session, post_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(pessoa, 'UTF-8'))
            return
        elif self.path == '/getperson':
            db = DataBase(DATA_BASE)
            content_len = int(self.headers.get('content-length'))
            post_data = urllib.parse.parse_qs(self.rfile.read(content_len).decode('utf-8'))
            pessoa = get_person(db.session, post_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(pessoa, 'UTF-8'))
            return
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

        return

    
    do_PUT = do_POST
    do_DELETE = do_GET
        

def start_server(NameVirtualHost):

    try:
        virtualhost = str.split(NameVirtualHost,":")
        if virtualhost[0] == "*":
            virtualhost[0] = ""
         
        server = HTTPServer((virtualhost[0], int(virtualhost[1])), RequestHandler)
        print ('Start server HTTP IN %s' % NameVirtualHost)
        server.serve_forever()

    except KeyboardInterrupt:
        print ('Shutting down server HTTP')
        server.socket.close()
