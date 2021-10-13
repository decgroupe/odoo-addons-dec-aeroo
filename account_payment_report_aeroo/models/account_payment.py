# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import api, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    @api.multi
    def _get_aeroo_report_filename(self):
        names = [x.name or str(x.id) for x in self]
        res = '-'.join(names)
        return res
