# Copyright (C) 2019 Open Source Integrators
# Copyright (C) 2019 Serpent consulting Services
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class FSMRoute(models.Model):
    _name = 'fsm.route'
    _description = 'Field Service Route'
    _order = 'name'

    name = fields.Char('Name', required=True)
    territory_id = fields.Many2one('fsm.territory', string='Territory')
    fsm_person_id = fields.Many2one('fsm.person', string='Person')
    day_ids = fields.Many2many('fsm.route.day', string='Days')
