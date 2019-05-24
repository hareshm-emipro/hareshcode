"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _


class EmibroideryThreadTypeColorEpt(models.Model):
    _name = "embroidery.thread.type.color.ept"
    

    thread_color_id = fields.Many2one('embroidery.thread.color.ept', string=_('Thread Color'))
    thread_type_id = fields.Many2one('embroidery.thread.type.ept', string=_('Thread Type'))
    project_id = fields.Many2one('project.task', string=_('Project Task'))
    
