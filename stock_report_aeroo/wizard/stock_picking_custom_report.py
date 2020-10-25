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

    state_draft = fields.Boolean(
        'New',
        help='draft',
    )
    state_cancel = fields.Boolean(
        'Cancelled',
        help='cancel',
    )
    state_waiting = fields.Boolean(
        'Waiting Another Move',
        help='waiting',
    )
    state_confirmed = fields.Boolean(
        'Waiting Availability',
        help='confirmed',
    )
    state_assigned = fields.Boolean(
        'Available',
        default=True,
        help='assigned or partially_available',
    )
    state_done = fields.Boolean(
        'Done',
        default=True,
        help='done',
    )

    @api.multi
    def print_report(self):
        wizard_data = self.read()[0]
        report = self.env.ref('stock_report_aeroo.stock_picking_report')

        context = dict(self.env.context)
        stock_picking = self.env['stock.picking'].browse(
            context.get('active_ids')
        )

        states = []
        if self.state_draft:
            states.append('draft')
        if self.state_cancel:
            states.append('cancel')
        if self.state_waiting:
            states.append('waiting')
        if self.state_confirmed:
            states.append('confirmed')
        if self.state_assigned:
            states.append('partially_available')
            states.append('assigned')
        if self.state_done:
            states.append('done')
        wizard_data['states'] = states

        action = report.with_context(context).report_action(
            stock_picking,
            config=False,
            data=wizard_data,
        )
        return action
