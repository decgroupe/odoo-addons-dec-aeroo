# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, May 2020

from odoo import api, fields, models


class PurchaseCustomReport(models.TransientModel):
    _name = 'purchase.custom.report'
    _description = 'Customize purchase report'

    total_amounts = fields.Boolean(
        'Total the amounts',
        help=
        "Total the amounts for lines with same product, uom, unit price and notes",
        default=True
    )

    pack_print = fields.Selection(
        [
            ('default', 'Default (by line setting)'),
            ('hide', 'Hide pack content'), ('show', 'Show full pack content')
        ],
        'Pack printing',
        default='default',
        size=16,
    )

    pack_hide_prices = fields.Boolean(
        'Hide pack line prices',
        help="Hide prices if equal to zero",
    )

    @api.multi
    def print_report(self):
        wizard_data = self.read()[0]
        report = self.env.ref('purchase_report_aeroo.purchase_order_report')

        context = dict(self.env.context)
        purchase_order = self.env['purchase.order'].browse(
            context.get('active_ids')
        )

        action = report.with_context(context).report_action(
            purchase_order,
            config=False,
            data=wizard_data,
        )
        return action
