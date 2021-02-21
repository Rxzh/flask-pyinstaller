# flask-pyinstaller
Personal notes &amp; tests to compile a Python Flask app using Pyinstaller





Commande pour build: 


$ pyinstaller --onefile --add-data 'templates:templates' --add-data 'static:static' flaskapp.py