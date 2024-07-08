# -*- coding: utf-8 -*-


from odoo import models, fields

class LeaseContract(models.Model):
    _name = 'lease.contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Contratos de Arrendamiento'

    name = fields.Char(string='Folio', required=True)
    start_date = fields.Date(string='Fecha de Inicio', required=True)
    end_date = fields.Date(string='Fecha de Fin', required=True)
    property_id = fields.Many2one('property', string='Propiedad', required=True,
                                  help='Propiedad arrendada en este contrato')
    lessor_id = fields.Many2one('lessor', string='Arrendador', required=True,
                                help='Arrendador en este contrato')
    