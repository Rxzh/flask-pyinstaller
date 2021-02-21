import sys
import os
import webbrowser
from threading import Timer
from flask import Flask, render_template

"""
determine si l'application est un script ou une appli frozen
ensuite récupère en fonctiond de ça le path de l'exe ou du .py
Pour ouvrir un fichier ensuite, il faudra à chaque fois l'appeler avec 'os.path.join(application_path,"fichier_name")'
"""
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

text_path = os.path.join(application_path, 'text.txt')


print("========================================")
print (os.getcwd())
print(application_path)
print("========================================")

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)








def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

file = open(text_path)
for l in file:
    text = l



@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    #return render_template('hello.html', name=name)
    return  """<!doctype html>
        <title>Hello from Flask</title>
        <h1>{}</h1>
        <img src="/static/logo.png" />
        """.format(text)


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run()