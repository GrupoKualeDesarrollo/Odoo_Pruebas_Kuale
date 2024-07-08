# -*- coding: utf-8 -*-
 from odoo import http
 import json


class ApiKuale(http.Controller):
     @http.route('/reclutamiento_kuale/reclutamiento_kuale', auth='public')
           def index(self, **kw):
           return "Hello, world"

     @http.route('/reclutamiento_kuale/reclutamiento_kuale/objects', auth='public')
          def list(self, **kw):
          return http.request.render('reclutamiento__kuale.listing', {
                'root': '/reclutamiento_kuale/reclutamiento_kuale',
                'objects': http.request.env['reclutamiento_kuale.reclutamiento_kuale'].search([]),
          })

     @http.route('/reclutamiento_kuale/reclutamientokuale/objects/<model("reclutamientokuale.reclutamiento_kuale"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('reclutamiento__kuale.object', {
             'object': obj
         })

     @http.route('/arrendamiento/programar_visita', auth='none', methods=['POST'], type='json', csrf=False)
         def programarVisita(self, **kw):
         return json.dumps({'respuesta': 1})
             