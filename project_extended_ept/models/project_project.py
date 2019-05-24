"""
    Developed By: Haresh Mori
"""

from odoo import fields, models, _



class ProjectTask(models.Model):
    _inherit = "project.project"

    projects = fields.Selection([('scr','[SCR]Screen Printing'),('vyn','[vyn]Vinyl'),('sub','[SUB]Sublimation'),('emb','[EMB]Embroidery'),('cht','[CHT]Wall Chart'),('hdg','[HDG]Heargear Wrap')])
    default_assigned_id  = fields.Many2one("res.users","Default Assignee")
    timeshets_employee_ids=fields.Many2many("hr.employee","hr_employee_project_rel",string=_('Timesheets Employee'))
    
    


