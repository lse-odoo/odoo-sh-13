# -*- coding: utf-8 -*-
# from odoo import http


# class Dummy(http.Controller):
#     @http.route('/dummy/dummy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dummy/dummy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dummy.listing', {
#             'root': '/dummy/dummy',
#             'objects': http.request.env['dummy.dummy'].search([]),
#         })

#     @http.route('/dummy/dummy/objects/<model("dummy.dummy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dummy.object', {
#             'object': obj
#         })
