# -*- coding: utf-8 -*-
from odoo import http

# class HrSavane(http.Controller):
#     @http.route('/hr_savane/hr_savane/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_savane/hr_savane/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_savane.listing', {
#             'root': '/hr_savane/hr_savane',
#             'objects': http.request.env['hr_savane.hr_savane'].search([]),
#         })

#     @http.route('/hr_savane/hr_savane/objects/<model("hr_savane.hr_savane"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_savane.object', {
#             'object': obj
#         })