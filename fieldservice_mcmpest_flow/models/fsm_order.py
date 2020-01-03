# Copyright (C) 2018 - TODAY, Open Source Integrators
# Copyright (c) 2019 - Brian McMaster <brian@mcmpest.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _
from odoo.exceptions import ValidationError


class FSMOrder(models.Model):
    _inherit = 'fsm.order'

    # def action_confirm(self):
    #     return self.write({'stage_id': self.env.ref(
    #         'fieldservice_mcmpest_flow.fsm_stage_confirmed').id})

    def action_assign(self):
        if self.person_id:
            return self.write({'stage_id': self.env.ref(
                'fieldservice_mcmpest_flow.fsm_stage_assigned').id})
        else:
            raise ValidationError(_("Cannot move to Assigned " +
                                    "until 'Assigned To' is filled in"))

    def action_schedule(self):
        if self.scheduled_date_start and self.person_id:
            return self.write({'stage_id': self.env.ref(
                'fieldservice_mcmpest_flow.fsm_stage_scheduled').id})
        else:
            raise ValidationError(_("Cannot move to Scheduled " +
                                    "until both 'Assigned To' and " +
                                    "'Scheduled Start Date' are filled in"))

    # def action_enroute(self):
    #     return self.write({'stage_id': self.env.ref(
    #         'fieldservice_mcmpest_flow.fsm_stage_enroute').id})

    def action_start(self):
        start_date = self.date_start or fields.Datetime.now()
        return self.write({
            'stage_id': self.env.ref(
                'fieldservice_mcmpest_flow.fsm_stage_started').id,
            'date_start': start_date,
        })

    def action_complete(self):
        if not self.resolution:
            self.launch_complete_wizard()
        date_end = self.date_end or fields.Datetime.now()
        return super(FSMOrder, self).action_complete()

    def launch_complete_wizard(self):
        return {
            'name': _("Complete %s") % self.name,
            'id': self.id,
            'type': 'ir.actions.act_window',
            'views': [[False, 'form']],
            'target': 'new',
            'context': {'default_fsm_order_id': self.id},
            'res_model': 'order.complete.wizard'
        }
