"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _


class VinylMaterialEpt(models.Model):
    _name = "vinyl.material.ept"
#    _rec_name = "vinyl_material_name"

    name = fields.Char(string='Material Name')
    
    
