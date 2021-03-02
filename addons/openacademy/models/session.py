import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class Session(models.Model):
    """ A Session is an occurrence of a Course taught at a given time for a given Audience."""

    _name = 'openacademy.session'

    name = fields.Char(string="Title", required=True)
    start_date = fields.Datetime(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help='Duration in days')
    active = fields.Boolean(default=True)
    seats = fields.Integer(string="Number of seats")
    # res.partner is a built-in model
    # When selecting the instructor for a Session, only instructors
    # (partners with instructor set to True) should be visible.
    instructor_id = fields.Many2one('res.partner', string='Instructor', domain=[('instructor', '=', True)])
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string='Course', required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    # percentage of taken seats to the Session
    taken_seats = fields.Float(string='Percentage of taken seats', compute='_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for record in self:
            _logger.debug('Session ' + str(record.id) + ' Nb seats ==>' + str(record.seats)
                          + ' Attendees ==> ' + str(record.attendee_ids))
            if not record.seats:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }
