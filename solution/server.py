from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse  import urlparse,parse_qs
import json
import random
JSON = []
sw = False
class Player():
    _instance= None
    def __new__(cls,player):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.player = player
            cls._instance.number = 50
            cls._instance.attempts = []
            cls._instance.status = "En progreso"
        return cls._instance
    def to_dict(self):
        return {
            "player":self.player,
            "number":self.number,
            "attempts":self.attempts,
            "status":self.status
        }
def partida(data):
    return {
            "player":data.get("player"),
            "number":data.get("number"),
            "attempts":data.get("attempts"),
            "status":data.get("status")
        }
class RequetsHandler:
    @staticmethod
    def response(self,status_code,data):
        self.send_response(status_code)
        self.send_header("Content-type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

class RestRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        if self.path == "/guess":
            RequetsHandler.response(self,200,JSON[0])
        elif self.path.startswith("/guess/"):
            RequetsHandler.response(self,200,JSON[0])
        else:
            RequetsHandler.response(self,404,{"error":404})    
    def do_POST(self):
        if self.path == "/guess":
            content_lenght = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_lenght)
            post_data = json.loads(post_data.decode("utf-8"))
            player = Player(post_data.get("player")).to_dict()
            JSON.append({"1":partida(player)})
            RequetsHandler.response(self,201,JSON[0].get("1"))
        else:
            RequetsHandler.response(self,404,[{"Pagina No encotrada":404}])    
    def do_PUT(self):
        if self.path.startswith("/guess/"):
            id = int(self.path.split("/")[-1])
            content_lenght = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_lenght)
            post_data = json.loads(post_data.decode("utf-8"))
            number = int(post_data.get("attempt"))
            playerNumactual = int(JSON[0].get("1").get("number"))
            if(number>playerNumactual):
                JSON[0].get("1").get("attempts").append(post_data.get("attempt"))
                RequetsHandler.response(self,200,[{"message":"El numero a adivinar es mayor"}]) 
            elif(number<playerNumactual):
                JSON[0].get("1").get("attempts").append(post_data.get("attempt"))
                RequetsHandler.response(self,200,[{"message":"El numero a adivinar es menor"}]) 
            else:
                JSON[0].get("1").get("attempts").append(post_data.get("attempt"))
                RequetsHandler.response(self,200,[{"message":"Felicitaciones has adivinado el numero"}]) 
                
        else:
            RequetsHandler.response(self,404,[{"Pagina No encotrada":404}]) 
    def do_DELETE(self):
        if self.path.startswith("/guess/"):
            JSON[0] ={}
            RequetsHandler.response(self,200,[{"message":"Partida Eliminada"}])
        
        
def run_server():
    server_address = ('',8000)
    httpd = HTTPServer(server_address,RequestHandlerClass=RestRequestHandler)
    print("Servidor ejecuntado en : http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()