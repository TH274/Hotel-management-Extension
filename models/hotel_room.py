from odoo import models, fields

class HotelRoom(models.Model):
    _inherit = 'hotel.room'

    room_size = fields.Float(string='Room Size (sqm)', required=True, tracking=True)
    max_people = fields.Integer(string='Max Occupancy', required=True, default=1, tracking=True)
    smoking_allowed = fields.Selection(
        [('yes', 'Yes'), ('no', 'No')],
        string='Smoking Allowed',
        default='no',
        required=True,
        tracking=True
    )
