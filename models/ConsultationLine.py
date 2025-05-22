from odoo import models, fields

class ConsultationLine(models.Model):
    _name = 'medicalconsulting.consultation.line'
    _description = 'Consultation Line'

    consultation_id = fields.Many2one('medicalconsulting.consultation', string='Consultation', required=True, ondelete='cascade')
    medication_id = fields.Many2one('medicalconsulting.medication', string='Medication', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)