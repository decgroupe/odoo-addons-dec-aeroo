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


class StockPickingCustomReport(models.TransientModel):
    _name = 'stock.picking.custom.report'
    _description = 'Customize stock picking report'

    message = fields.Text(
        'Custom message',
        help="Allow to display a custom text",
    )

    @api.multi
    def print_report(self):
        wizard_data = self.read()[0]
        report = self.env.ref('stock_report_aeroo.stock_picking_report')

        context = dict(self.env.context)
        stock_picking = self.env['stock.picking'].browse(
            context.get('active_ids')
        )

        action = report.with_context(context).report_action(
            stock_picking,
            config=False,
            data=wizard_data,
        )
        return action
