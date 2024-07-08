


from odoo import models, fields

class Lessor(models.Model):
    _name = 'lessor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Arrendadores'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electronico')
    phone = fields.Char(string='Telefono')
    properties_ids = fields.One2many('property', 'lessor_id', string='Propiedades')
    lease_contract_ids = fields.One2many('lease.contract', 'lessor_id', string='Contratos de Arrendamiento')