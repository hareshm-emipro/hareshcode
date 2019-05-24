"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _


class GarmentMaterial(models.Model):
    _name = "garment.material.ept"
    _rec_name = "material_name"

    material_name = fields.Char(string='Material_Name')
    
