from odoo import http
from odoo.http import request

# class Reto(http.Controller):
#     @http.route('/reto', auth='public')
#     def reto(self, **kw):
#         user = request.env.user
#         if user and not user._is_public():
#             return http.Response("Hello {}!".format(user.name), content_type='text/plain;charset=utf-8', status=200)
#         else:
#             return http.Response("Hello world!", content_type='text/plain;charset=utf-8', status=200)


class RetoController(http.Controller):
    @http.route('/reto', auth='public', website=True)
    def reto(self, **kw):
        user = request.env.user
        return request.render("reto.reto_template", {'user': user if not user._is_public() else None})