from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.before_request
def before_request():
    print("antes de la peticion...")

@app.after_request
def after_request(response):
    print("despues de la peticion...")
    return response
@app.route("/")
def index():
    print("estamos procesando la peticion....")
   # return render_template('index.html', titulo = ' pagina',enca ='Bienvenido(a)')
    data = {
        'titulo':'inicio',
        'enca' : 'bienvenido(a)'
        
    }    
    return render_template('index.html',data= data)
        
@app.route("/contacto")
def contacto():
    
     data = {
        'titulo':'inicio',
        'enca' : 'bienvenido(a)'
        
    }    
     return render_template('contacto.html',data=data)
    
  
@app.route("/lenguajes")
def lenguajes():
    
     data = {
        "lenguajes":['html','c#','python','java']
        
        
    }    
     return render_template('lenguajes.html',data=data)
 
 

if __name__ =="__main__":
    app.run(debug=True,port =8000 )