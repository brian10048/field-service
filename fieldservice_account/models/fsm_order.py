# Copyright (C) 2018 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class FSMOrder(models.Model):
    _inherit = 'fsm.order'

    invoice_ids = fields.Many2many(
        'account.invoice', 'fsm_order_account_invoice_rel',
        'fsm_order_id', 'invoice_id', string='Invoices/Bills')
    invoice_count = fields.Integer(
        string='Invoice Count',
        compute='_compute_account_invoice_count', readonly=True)

    @api.depends('invoice_ids')
    def _compute_account_invoice_count(self):
        for order in self:
            order.invoice_count = len(order.invoice_ids)

    @api.multi
    def action_view_invoices(self):
        action = self.env.ref('account.action_invoice_tree').read()[0]
        invoices = self.mapped('invoice_ids')
        invoice_ids = [invoice.id for invoice in invoices if
                       invoice.type == 'out_invoice']
        if len(invoice_ids) > 1:
            action['domain'] = [('id', 'in', invoice_ids)]
        elif invoices:
            action['views'] = [(self.env.ref('account.invoice_form').id,
                                'form')]
            action['res_id'] = invoice_ids[0]
        return action