# Copyright (C) DEC SARL, Inc - All Rights Reserved.
#
# CONFIDENTIAL NOTICE: Unauthorized copying and/or use of this file,
# via any medium is strictly prohibited.
# All information contained herein is, and remains the property of
# DEC SARL and its suppliers, if any.
# The intellectual and technical concepts contained herein are
# proprietary to DEC SARL and its suppliers and may be covered by
# French Law and Foreign Patents, patents in process, and are
# protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from DEC SARL.
# Written by Yann Papouin <y.papouin@dec-industrie.com>, May 2020

from odoo import api, fields, models, _


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
