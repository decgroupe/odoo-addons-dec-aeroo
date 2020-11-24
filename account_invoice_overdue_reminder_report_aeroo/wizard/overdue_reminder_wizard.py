# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Nov 2020

import logging

from odoo import api, models

logger = logging.getLogger(__name__)

MOD = 'account_invoice_overdue_reminder_report_aeroo'


class OverdueReminderStep(models.TransientModel):
    _inherit = 'overdue.reminder.step'

    @api.multi
    def _get_aeroo_report_filename(self):
        names = [str(x.id) for x in self]
        res = '-'.join(names)
        return res

    def print_letter(self):
        action = super().print_letter()
        # Override default action
        action = action = self.env.ref(MOD + '.overdue_reminder_report') \
            .with_context(discard_logo_check=True).report_action(self)
        return action

    def print_invoices(self):
        action = super().print_invoices()
        # Override default action
        if self.user_has_groups('account.group_account_invoice'):
            return self.env.ref('account_report_aeroo.account_invoice_report')\
                .with_context(discard_logo_check=True).\
                    report_action(self.invoice_ids.ids)
        return action
