from odoo import models, fields

class Doctor(models.Model):
    _name = 'medicalconsulting.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Full Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')