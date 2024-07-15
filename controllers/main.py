from odoo import http
from odoo.http import request

class CustomController(http.Controller):

    @http.route('/my_endpoint', auth='public', methods=['GET', 'POST'], csrf=False, type='json')
    def my_endpoint(self, **kwargs):
        # Lógica del endpoint
        if request.httprequest.method == 'POST':
            data = request.jsonrequest  # Para solicitudes POST con datos JSON
            # Procesar los datos aquí
            # return http.Response('Data received', status=200)
            key_value = data.get('key', 'default_value')
            return {'response': f'Data received: {key_value}'}        
        elif request.httprequest.method == 'GET':
            return http.Response('Hello, this is a GET request', status=200)
        
        # Para probarlo
        # curl -X POST http://localhost:8311/my_endpoint -H "Content-Type: application/json" -d '{"key":"000"}'
        #  curl -X GET http://localhost:8311/my_endpoint
