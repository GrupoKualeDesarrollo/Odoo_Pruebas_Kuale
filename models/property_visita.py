from odoo import models, fields

class Property_Visita(models.Model):
    _name = 'property.visita'

    name = fields.Char(string='Nombre del Inmueble', required=True)
    lugar = fields.Char(string='Lugar (Direccion del Inmueble)', required=True)
    fecha_hora = fields.Datetime(string='Fecha y Hora', required=True)
    comentarios = fields.Text(string='Comentarios')


    def action_save(self):
        # Lógica para guardar el registro
        pass