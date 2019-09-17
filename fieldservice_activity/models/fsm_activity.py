# Copyright (C) 2019, Brian McMaster
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FSMActivity(models.Model):
    _name = 'fsm.activity'
    _description = 'FSM Order Activity'

    activity_template_id = fields.Many2one('fsm.activity.template',
                                           string='Activity Template')
    description = fields.Html(string='Description')
    outcome_type = fields.Selection([('single', 'One Outcome'),
                                    ('multi', 'Multiple Outcomes')],
                                    'Outcome Type', required=True)
    condition_ids = fields.Many2many(
        'fsm.condition', domain=lambda self:
            [('id', 'in', self.activity_template_id.condition_ids)])
    order_id = fields.Many2one('fsm.order', string='Order',
                               index=True, required=True)
    sequence = fields.Integer(string='Sequence', default=10)
