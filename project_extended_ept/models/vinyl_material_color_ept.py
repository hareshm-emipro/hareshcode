"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _


class vinylMaterialColorEpt(models.Model):
    _name = "vinyl.material.color.ept"
    

    
    vinyl_material_id = fields.Many2one('vinyl.material.ept', string=_('Vinyl Material'))
    vinyl_color_id = fields.Many2one('vinyl.color.ept', string=_('Vinyl Color'))
    project_id = fields.Many2one('project.task', string=_('Project Task'))
    
