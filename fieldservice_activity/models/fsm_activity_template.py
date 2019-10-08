# Copyright (C) 2019, Brian McMaster
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FSMActivityTemplate(models.Model):
    _name = 'fsm.activity.template'
    _description = 'FSM Order Activity Template'

    name = fields.Char(string='Name', required=True)
    description = fields.Html(string='Description')
    outcome_type = fields.Selection([('text', 'Text'),
                                     ('single', 'One Outcome'),
                                     ('multi', 'Multiple Outcomes')],
                                    'Outcome Type', required=True)
    condition_ids = fields.Many2many('fsm.condition',
                                     string="Possible Conditions")
