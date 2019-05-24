"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _


class VinylColorEpt(models.Model):
    _name = "vinyl.color.ept"
    _rec_name = "vinyl_material_color"

    vinyl_material_color = fields.Char(string='Color Name')
    vinyl_material_type_id = fields.Many2one('vinyl.material.ept', string=_('Vinyl Material'))
    
