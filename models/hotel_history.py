from odoo import models, fields, api, _

class HotelHotel(models.Model):
    _inherit = 'hotel.hotel'

    booking_ids = fields.One2many('hotel.booking', 'hotel_id', string='Booking History')

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'

    guest_name = fields.Char(string='Guest Name', required=True)
    hotel_id = fields.Many2one('hotel.hotel', string='Hotel', required=True)
    room_number = fields.Char(string='Room Number', required=True)
    check_in_date = fields.Date(string='Check-in Date', required=True)
    check_out_date = fields.Date(string='Check-out Date', required=True)

    @api.model
    def _create_booking_from_customer(self, customer):

        if not customer:
            return

        self.create({
            'guest_name': customer.name,
            'hotel_id': customer.hotel_id.id,
            'room_number': customer.room_id.room_number,
            'check_in_date': customer.check_in_date,
            'check_out_date': customer.check_out_date,
        })
