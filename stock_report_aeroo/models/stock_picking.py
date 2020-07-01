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
# Written by Yann Papouin <y.papouin@dec-industrie.com>, July 2020

from odoo import models, api, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def _get_aeroo_report_filename(self):
        names = [x.name for x in self]
        res = '-'.join(names)
        return res

    production_order_names = fields.Text(
        compute='_compute_production_order_names',
        string='Manufacturing Orders',
    )

    @api.multi
    def _compute_production_order_names(self):
        for picking in self:
            picking.production_order_names = '\n'.join(
                o.name for o in picking.production_ids
            )

    original_creator_user_id = fields.Many2one(
        'res.users',
        compute='_compute_original_creator',
        string='Original creator',
    )

    @api.multi
    def _compute_original_creator(self):
        for picking in self:

            picking_ids = False
            if picking:
                picking_ids = picking.search(
                    [('backorder_id.id', '=', picking.id)]
                )

            if picking_ids:
                picking.original_creator_user_id = picking_ids[
                    0].original_creator_user_id
            elif picking.create_uid:
                picking.original_creator_user_id = picking.create_uid.id
            else:
                picking.original_creator_user_id = False
