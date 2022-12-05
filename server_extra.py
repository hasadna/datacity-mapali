from flask import send_file

def extra_server_init(app):
    @app.route('/')
    def mapali(subpath=None):
        return send_file(f'ui/dist/ui/index.html')

    @app.route('/new')
    def mapali_new(subpath=None):
        return send_file(f'ui/dist/ui/index.html')

    @app.route('/[a-z0-9]{16}')
    def mapali_map(subpath=None):
        return send_file(f'ui/dist/ui/index.html')
