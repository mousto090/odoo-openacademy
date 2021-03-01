from odoo import models, fields


class Session(models.Model):
    """ A Session is an occurrence of a Course taught at a given time for a given Audience."""

    _name = 'openacademy.session'

    name = fields.Char(string="Title", required=True)
    start_date = fields.Datetime()
    duration = fields.Float(digits=(6, 2), help='Duration in days')
    seats = fields.Integer(string="Number of seats")
    # res.partner is a built-in model
    # When selecting the instructor for a Session, only instructors
    # (partners with instructor set to True) should be visible.
    instructor_id = fields.Many2one('res.partner', string='Instructor', domain=[('instructor', '=', True)])
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string='Course', required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
