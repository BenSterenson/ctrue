from connexion.resolver import RestyResolver
import connexion

app = connexion.FlaskApp(__name__, port=80, specification_dir='swagger/')
app.add_api('api.yaml', resolver=RestyResolver('app.api'))

if __name__ == '__main__':
    app.run()
