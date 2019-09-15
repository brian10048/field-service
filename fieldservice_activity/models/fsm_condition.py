# Copyright (C) 2019, Brian McMaster
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FSMCondition(models.Model):
    _name = 'fsm.condition'
    _description = 'FSM Order Condition'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
