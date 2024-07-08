


from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools import float_utils

class Property(models.Model):
    _name = 'property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Propiedades Inmobiliarias'

    name = fields.Char(string='Nombre', required=True)
    address = fields.Char(string='Direccion')
    description = fields.Text(string='Descripcion')
    size = fields.Float(string='Tamano')
    
    status = fields.Selection([
        ('1', 'Disponible'),
        ('0', 'No Disponible'),
    ], string='Estado', default='1', tracking=True)

    # Relaciones
    lessor_id = fields.Many2one('lessor', string='Arrendador', required=True, ondelete='restrict',
                                help='Arrendador de esta propiedad')
    lease_contract_ids = fields.One2many('lease.contract', 'property_id', string='Contratos de Arrendamiento')

    
    def action_programar_visita(self):
            return {
                'name': 'Programar Visita',
                'type': 'ir.actions.act_window',
                'res_model': 'property.visita',
                'view_mode': 'form',
                'target': 'new',
            }