from chalice import Chalice

app = Chalice(app_name='matchwork')


@app.route('/')
def index():
    return {'hello': 'world'}
