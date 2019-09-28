# Copyright (C) 2019, Brian McMaster
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class FSMOrder(models.Model):
    _inherit = 'fsm.order'

    fsm_activity_ids = fields.One2many('fsm.activity', 'order_id',
                                       string='Activities', auto_join=True)

    @api.onchange('template_id')
    def _onchange_template_id(self):
        super()._onchange_template_id()
        if self.template_id:
            self.prepare_activities()

    def prepare_activities(self):
        template = self.template_id
        activity_lines = [(5, 0, 0)]
        for line in template.activity_line_ids:
            act_template = line.activity_template_id
            vals = {
                'activity_template_id': act_template.id,
                'description': act_template.description,
                'outcome_type': act_template.outcome_type,
                'sequence': line.sequence,
                'order_id': self.id,
            }
            activity_lines.append((0, 0, vals))
        self.fsm_activity_ids = activity_lines
