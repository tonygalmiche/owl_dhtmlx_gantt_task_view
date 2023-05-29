from odoo import fields, models


class View(models.Model):
    _inherit = "ir.ui.view"

    type = fields.Selection(selection_add=[
        ("dhtmlx_gantt_task", "Vue OWL Dhtmlx Gantt Task"),
    ])

