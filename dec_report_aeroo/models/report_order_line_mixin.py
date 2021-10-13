# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import api, fields, models

class ReportOrderLineMixin(models.AbstractModel):
    _name = "report.orderline.mixin"
    _description = 'Subtotal and Hide fields for order report rendering'

    @api.multi
    def _get_report_subtotal(self):
        # The subtotal will be stored in sum
        section_subtotal = 0
        # At each new section [1] or at the last line [2]
        section_line = False
        previous_line = False
        # We need to sort order lines because the iterator does not
        # respect sequence contract
        for line in sorted(self, key=lambda x: x.sequence, reverse=False):
            # Always reset current line subtotal to 0 (False), that way
            # the report will not try to print a subtotal section
            line.report_subtotal = 0
            if line.display_type == 'line_section':
                section_line = line
                # [1] New section detected, assign current value to
                # previous non section line and reset the current
                # subtotal
                if previous_line:
                    previous_line.report_subtotal = section_subtotal
                    previous_line = False
                    section_subtotal = 0
            elif section_line:
                # We are currently browsing a section so we need
                # to increment the section subtotal
                section_subtotal = section_subtotal + line.price_subtotal
                previous_line = line
        # [2] Special case, last line reached and previous_line is
        # still assigned, so we need to output the current subtotal
        # to this line
        if previous_line:
            previous_line.report_subtotal = section_subtotal

    report_hide_line = fields.Boolean(
        'Hide Line',
        default=False,
        help="This allows the seller to hide the entire printed line",
    )
    report_hide_uom = fields.Boolean(
        'Hide Uom',
        default=False,
        help="Only hide units of this line",
    )
    report_hide_price = fields.Boolean(
        'Hide Price',
        default=False,
        help="Only hide price of this line (when equal to zero in most cases)",
    )

    # This is a legacy field used to compute the 'subtotal' of a section
    # field from OpenERP 6.1 when used with sale_layout module
    # For PDF rendering only
    report_subtotal = fields.Float(
        compute=_get_report_subtotal,
        store=False,
    )
