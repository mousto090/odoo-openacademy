import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    """This class inherit the built-in odoo stock.move"""
    _inherit = 'stock.move'
    color_id = fields.Many2one('savane.color', string='Couleur', required=True)
    brand_id = fields.Many2one('savane.brand', string='Marque', required=True)

    # def action_confirm(self, cr, uid, ids, context=None):
    #     _logger.debug(self, cr, uid, ids, context)
