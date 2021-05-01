from flask import Flask
from routes import urls_blueprint
import database


app = Flask(__name__)
# register routes from urls
app.register_blueprint(urls_blueprint)
database.init_db()

if __name__ == "__main__":
    app.run(host='172.20.0.5', port=5000)
    app.run(debug=True)


#docker image build -t python-hello-world .
#docker run -p 5001:5000 -d python-hello-world