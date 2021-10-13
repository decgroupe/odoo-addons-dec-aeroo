# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, July 2020

from types import SimpleNamespace
from odoo import models, api, fields


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    @api.multi
    def _get_aeroo_report_filename(self):
        names = [x.name or str(x.id) for x in self]
        res = '-'.join(names)
        return res

    finished_picking_dates = fields.Text(
        compute='_compute_finished_picking_dates',
        string='Finished Pickings dates',
    )

    @api.multi
    def _compute_finished_picking_dates(self):
        for production in self:
            scheduled_dates = production.finished_picking_ids.mapped(
                'scheduled_date'
            )
            scheduled_dates = [
                fields.Datetime.to_string(s) for s in scheduled_dates
            ]
            production.finished_picking_dates = '\n'.join(scheduled_dates)

    def print_move_raw_lines(self, data=None):
        if data is None:
            data = {}
        lines = []
        for move in self.move_raw_ids.filtered(lambda x: x.state != 'cancel'):
            reserved = (move.reserved_availability == move.product_uom_qty)
            # Create a dummy python object to hold editable data without
            # updating database content
            line = SimpleNamespace(
                pack=bool(move.pack_child_move_ids.ids),
                level=move.pack_level,
                move=move,
                name=move.name,
                product_id=move.product_id,
                manufacturer=move.product_id.print_manufacturer(),
                product_uom_qty=move.product_uom_qty,
                product_uom=move.product_uom,
                reserved_availability=move.reserved_availability,
                date_expected=move.date_expected,
                picking_id=move.picking_id,
                reference=move.reference,
                state=move.state,
                received=move.received,
                reserved=reserved,
                status=move.get_mrp_status(False),
            )
            lines.append(line)

        return lines
