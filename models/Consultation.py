from odoo import models, fields, api

class Consultation(models.Model):
    _name = 'medicalconsulting.consultation'
    _description = 'Consultation'

    client_id = fields.Many2one('medicalconsulting.client', string='Client', required=True)
    doctor_id = fields.Many2one('medicalconsulting.doctor', string='Doctor', required=True)
    consultation_date = fields.Datetime(string='Consultation Date', default=fields.Datetime.now)
    diagnosis = fields.Text(string='Diagnosis')
    consultation_line_ids = fields.One2many('medicalconsulting.consultation.line', 'consultation_id', string='Consultation Lines')

    total_price = fields.Float(string="Total Price", compute='_compute_total_price')

    @api.depends('consultation_line_ids.quantity')
    def _compute_total_price(self):
        for record in self:
            total = 0.0
            for line in record.consultation_line_ids:
                total += (line.medication_id.unit_price or 0.0) * (line.quantity or 0.0)
            record.total_price = total

