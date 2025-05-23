from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Consultation(models.Model):
    _name = 'medicalconsulting.consultation'
    _description = 'Consultation'

    client_id = fields.Many2one('medicalconsulting.client', string='Client', required=True)
    doctor_id = fields.Many2one('medicalconsulting.doctor', string='Doctor', required=True)
    consultation_date = fields.Datetime(string='Consultation Date', default=fields.Datetime.now)
    diagnosis = fields.Text(string='Diagnosis')
    consultation_line_ids = fields.One2many('medicalconsulting.consultation.line', 'consultation_id', string='Consultation Lines')

    total_price = fields.Float(string="Total Price", compute='_compute_total_price')

    state = fields.Selection(
        [
            ('not_processed', 'Not processed'), ('in_progress', 'In progress'), ('done', 'Done')
        ], string='State', default='not_processed', required=True
    )


    @api.depends('consultation_line_ids.quantity')
    def _compute_total_price(self):
        for record in self:
            total = 0.0
            for line in record.consultation_line_ids:
                total += (line.medication_id.unit_price or 0.0) * (line.quantity or 0.0)
            record.total_price = total

    @api.constrains('doctor_id', 'state', 'consultation_date')
    def _check_doctor_max_consultations(self):
        for record in self:
            if record.state == 'in_progress' and record.consultation_date:
                date_start = record.consultation_date.date()
                datetime_start = datetime.combine(date_start, datetime.min.time())
                datetime_end = datetime.combine(date_start, datetime.max.time())

                count = self.search_count([
                    ('doctor_id', '=', record.doctor_id.id),
                    ('state', '=', 'in_progress'),
                    ('consultation_date', '>=', datetime_start),
                    ('consultation_date', '<=', datetime_end),
                    ('id', '!=', record.id),
                ])
                if count >= 3:
                    raise ValidationError(
                        f"This doctor already has 3 consultations in progress on {date_start.strftime('%Y-%m-%d')}."
                    )


