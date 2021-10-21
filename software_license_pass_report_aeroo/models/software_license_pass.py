# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Oct 2021

from odoo import models, api


class SoftwareLicensePass(models.Model):
    _inherit = 'software.license.pass'

    @api.multi
    def _get_aeroo_report_filename(self):
        names = [x.serial or str(x.id) for x in self]
        res = '-'.join(names)
        return res
