"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _


class EmibroideryThreadColorEpt(models.Model):
    _name = "embroidery.thread.color.ept"
    _rec_name = "thread_color"

    thread_color = fields.Char(string='Thread_Color')
    embroidery_thread_type_id = fields.Many2one('embroidery.thread.type.ept', string=_('Embroidery Thread'))

    
