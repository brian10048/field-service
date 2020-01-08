# Copyright (C) 2020 Brian McMaster
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class FSMLocation(models.Model):
    _inherit = 'fsm.location

    fsm_recurring_count = fields.Float(
        string='FSM Recurring Orders', compute='_compute_fsm_recurring_ids')

    @api.multi
    @api.depends('order_line.product_id')
    def _compute_fsm_recurring_ids(self):
        for location in self:
            locations = self.get_action_views(0, 0, location)
            location.fsm_order_count = self.env['fsm.order'].search_count([
                ('fsm_location_id', 'in', locations.ids)])

    @api.multi
    def action_view_fsm_recurring(self):
        for location in self:
            locations = self.get_action_views(0, 0, location)
            fsm_recurrings = locations.mapped('fsm_recurring_ids')
            action = self.env.ref(
                'fieldservice_recurring.action_fsm_recurring').read()[0]
            if len(fsm_recurrings) > 1:
                action['domain'] = [('id', 'in', fsm_recurrings.ids)]
            elif len(fsm_recurrings) == 1:
                action['views'] = [
                    (self.env.ref(
                        'fieldservice_recurring.fsm_recurring_form_view').id,
                        'form')]
                action['res_id'] = fsm_recurrings.id
            else:
                action = {'type': 'ir.actions.act_window_close'}
            return action
