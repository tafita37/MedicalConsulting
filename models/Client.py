from odoo import models, fields

class Client(models.Model):
    _name = 'medicalconsulting.client'
    _description = 'Client (Patient)'

    name = fields.Char(string='Full Name', required=True)
    birth_date = fields.Date(string='Date of Birth')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')