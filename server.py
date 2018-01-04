import os
import json
import urllib
import mimetypes

from http.server import HTTPServer, BaseHTTPRequestHandler

from app.controllers import get_home, get_people, get_person, save_person, delete_person, edit_person
from app.settings import STATIC_ROOT, CONNECTION_STRING
from app.models import DataBase


class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        response = None
        response_code = 200
        response_mimetype = 'text/html'

        if self.path == '/':            
            response = get_home()
        elif self.path.split('/')[1] == 'static':
            filename = STATIC_ROOT + '/'.join(self.path.split('/')[2:])
            if os.path.isfile(filename):
                response = open(filename).read()
                response_mimetype = mimetypes.MimeTypes().guess_type(filename)[0]
            else:
                response = 'Page not found'
                response_code = 404
        else:
            response = 'Page not found'
            response_code = 404
        
        self.protocol_version='HTTP/1.1'
        self.send_response(response_code, 'OK')
        self.send_header('Content-type', response_mimetype)
        self.end_headers()
        
        if response:
            self.wfile.write(bytes(response, 'UTF-8'))
        

    def do_POST(self):
        db_session = DataBase(CONNECTION_STRING).session
        response = None
        response_code = 200

        content_len = int(self.headers.get('content-length'))
        data = urllib.parse.parse_qs(self.rfile.read(content_len).decode('utf-8'))

        if self.path == '/getpeople':            
            response = get_people(db_session, data)
        elif self.path == '/createperson':
            response = save_person(db_session, data)
        elif self.path == '/deleteperson':
            response = delete_person(db_session, data)
        elif self.path == '/editperson':
            response = edit_person(db_session, data)
        elif self.path == '/getperson':
            response = get_person(db_session, data)
        else:
            response_code = 404

        self.send_response(response_code)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        if response:
            self.wfile.write(bytes(response, 'UTF-8'))


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
