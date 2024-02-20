from flask import Flask, request, render_template, redirect, url_for
import maildb

app = Flask(__name__)

#URL arrel, si accedeixen a l'arrel, fem redirect a getmail
@app.route("/")
def inici():
    return redirect(url_for('getmail'))
   
#URL getmail, mostra formulari per introduir el nom 
# quan omplim el formulari, mostra en una nova pàgina el resultat: el mail si l'ha trobat al diccionari o
# un missatge d'error quan no el troba.
# Permet enllaçar a la URL addmail
@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      result=True
      nom = request.form['nom']
      nom = nom.capitalize() #en majúscules la primera lletra
      correu = maildb.sqlgetmail(nom)
      return render_template('getmail.html',nom=nom,correu=correu,result=result)
   else:
      result=False
      return render_template('getmail.html',result=result)

#URL addmail, mostra formulari per introduir el nom i el correu 
# quan omplim el formulari, mostra en una nova pàgina el resultat: si ha afegit el nom/correu al diccionari o
# un missatge d'error quan ja existeix.
# Permet enllaçar a la URL getmail  
@app.route('/addmail',methods = ['POST', 'GET'])
def addmail():
   if request.method == 'POST':
      modif=False
      nom = request.form['nom']  #ull! si no ve, això acaba amb error
      nom=nom.capitalize()
      correu = request.form['correu']
      if 'modif' in request.form: #el checkbox és opcional 
         modif = True
      result_msg = maildb.sqladdUser(nom,correu,modif)
      return render_template('resultaddmail.html',nom = nom, correu=correu, result_msg = result_msg)
   else:
      return render_template('formaddmail.html')