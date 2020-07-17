# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, May 2020

from odoo import api, fields, models


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
