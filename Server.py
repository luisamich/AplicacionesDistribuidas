import cherrypy
import json 

class OperacionesBasicas(object): 
    @cherrypy.expose
    def index(self):
        return 'Web Services con operaciones básicas'
    
    @cherrypy.expose
    def suma(self, x,y): 
        resul = int(x)+int(y); 
        return json.dumps({"Suma: ":resul})
    
    @cherrypy.expose
    def resta(self, x,y): 
        resul = int(x)-int(y); 
        return json.dumps({"Resta: ":resul})

    @cherrypy.expose
    def multiplicacion(self, x,y): 
        resul = int(x)*int(y); 
        return json.dumps({"Multipliacion: ":resul})
    
    @cherrypy.expose
    def division(self, x,y): 
        resul = int(x)/int(y); 
        return json.dumps({"Division: ":resul})

if __name__ == '__main__': 
    cherrypy.quickstart(OperacionesBasicas())
        
    
    

    
