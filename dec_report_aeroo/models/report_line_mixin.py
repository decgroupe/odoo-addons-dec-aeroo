# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import api, fields, models


class ReportLineMixin(models.AbstractModel):
    _name = "report.line.mixin"
    _description = 'Name and note fields for report rendering'

    @api.multi
    def _get_report_fields(self):
        for line in self:
            # Use partition to split our line text into three parts
            # The first one is the left part (title), the second one is the
            # delimiter and the last one is the right part (description)
            parts = line.name.partition('\n')
            line.report_name = parts[0]
            line.report_note = parts[2]

    # This is a legacy field used to mimic the 'name' field from OpenERP 6.1
    # For PDF rendering only
    report_name = fields.Char(
        compute=_get_report_fields,
        store=False,
    )
    # This is a legacy field used to mimic the 'note' field from OpenERP 6.1
    # For PDF rendering only
    report_note = fields.Char(
        compute=_get_report_fields,
        store=False,
    )
