# -*- coding: utf-8 -*-
# from odoo import http


# class ReportToc(http.Controller):
#     @http.route('/report_toc/report_toc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_toc/report_toc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_toc.listing', {
#             'root': '/report_toc/report_toc',
#             'objects': http.request.env['report_toc.report_toc'].search([]),
#         })

#     @http.route('/report_toc/report_toc/objects/<model("report_toc.report_toc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_toc.object', {
#             'object': obj
#         })

