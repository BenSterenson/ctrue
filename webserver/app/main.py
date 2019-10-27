from connexion.resolver import RestyResolver
from flask_cors import CORS
import connexion

app = connexion.FlaskApp(__name__, port=80, specification_dir='swagger/')
cors = CORS(app.app)
app.add_api('api.yaml', resolver=RestyResolver('app.api'))

if __name__ == '__main__':
    app.run()
