from flaskapp import app, db
from flaskapp.models import User

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)