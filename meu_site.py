from flask import Flask, render_template

app = Flask(__name__)


#*** route--> caminho
#*** / = homepage 
#*** função --> oque voce quer exibir  

#HOMEPAGE
@app.route('/')
def homepage():
    return render_template ('homepage.html') 
#PAGINA CONTATO 
@app.route('/contatos')
def contatos(): 
     return render_template ('contatos.html') 

#PAGINA USARIO
@app.route('/usuarios/<nome_usuario>')
def usuario (nome_usuario):
    return render_template ('usuario.html', nome_usuario = nome_usuario) # nome_usuario.html = nome_usuario.py

# SITE ATUALIZA SOZINHO SE FOR MAIN
if (__name__) == ('__main__'): 
    app.run(debug=True)

    #servidos heroku    