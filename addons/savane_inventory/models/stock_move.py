from odoo import models, fields


class StockMove(models.Model):
    """This class inherit the built-in odoo stock.move"""
    _inherit = 'stock.move'
    color_id = fields.Many2one('savane.color', ondelete='cascade', string='Couleur', required=True)
    brand_id = fields.Many2one('savane.brand', ondelete='cascade', string='Marque', required=True)
