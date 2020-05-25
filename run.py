from flask_seguro import create_app
from pagseguro import PagSeguro

app = create_app('development')


@app.shell_context_processor
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)  