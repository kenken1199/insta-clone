from flaskapp import app, db
from flaskapp.models import User

if __name__ == '__main__':
    app.run(debug=True)