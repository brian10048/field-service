# Copyright (C) 2019, Brian McMaster
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FSMTemplate(models.Model):
    _inherit = 'fsm.template'

    activity_line_ids = fields.One2many('fsm.template.activity.line',
                                        'fsm_template_id', auto_join=True,
                                        string='Activity Templates')


class FSMTemplateActivityLine(models.Model):
    _name = 'fsm.template.activity.line'
    _description = 'Order Template Activity Line'
    _order = 'sequence'

    activity_template_id = fields.Many2one('fsm.activity.template',
                                            string='Activity Template')
    fsm_template_id = fields.Many2one('fsm.template', string='Order Template',
                                      index=True, required=True)
    sequence = fields.Integer(string='Sequence', default=10)
