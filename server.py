
from flask_app import app
from flask_app.controllers import ninja , dojo   #need to import the file 

if __name__ == "__main__":
    app.run(debug=True, port=5002)