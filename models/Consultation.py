from odoo import models, fields

class Consultation(models.Model):
    _name = 'medicalconsulting.consultation'
    _description = 'Consultation'

    client_id = fields.Many2one('medicalconsulting.client', string='Client', required=True)
    doctor_id = fields.Many2one('medicalconsulting.doctor', string='Doctor', required=True)
    consultation_date = fields.Datetime(string='Consultation Date', default=fields.Datetime.now)
    diagnosis = fields.Text(string='Diagnosis')
    consultation_line_ids = fields.One2many('medicalconsulting.consultation.line', 'consultation_id', string='Consultation Lines')