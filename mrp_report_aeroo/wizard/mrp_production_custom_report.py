# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import api, fields, models


class MrpProductionCustomReport(models.TransientModel):
    _name = 'mrp.production.custom.report'
    _description = 'Customize manufacturing order report'

    message = fields.Text(
        'Custom message',
        help="Allow to display a custom text",
    )

    @api.multi
    def print_report(self):
        wizard_data = self.read()[0]
        report = self.env.ref('mrp_report_aeroo.mrp_production_report')

        context = dict(self.env.context)
        production = self.env['mrp.production'].browse(
            context.get('active_ids')
        )

        action = report.with_context(context).report_action(
            production,
            config=False,
            data=wizard_data,
        )
        return action
