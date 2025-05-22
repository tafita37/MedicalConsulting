from odoo import models, fields

class Medication(models.Model):
    _name = 'medicalconsulting.medication'
    _description = 'Medication'

    name = fields.Char(string='Medication Name', required=True)
    description = fields.Text(string='Description')
    unit_price = fields.Float(string='Unit Price', digits=(6, 2))