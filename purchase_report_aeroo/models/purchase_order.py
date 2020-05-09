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

from types import SimpleNamespace
from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def print_purchase_order_lines(self, data=None):
        def _totalize_printed_lines(line, lines):
            for sl in lines:
                if (sl.product_id == line.product_id) \
                and (sl.product_uom == line.product_uom) \
                and (sl.price_unit == line.price_unit) \
                and (sl.taxes_id == line.taxes_id) \
                and (sl.name == line.name):
                    sl.product_qty += line.product_qty
                    sl.price_subtotal += line.price_subtotal
                    return True
            return False

        # Get back data from wizard
        if data:
            total_amounts = data.get('total_amounts')
            pack_print = data.get('pack_print', 'default')
            pack_hide_prices = data.get('pack_hide_prices')

        lines = []
        for ol in self.order_line:

            # If missing product_pack support, then set a false value to
            # continue report printing
            if not hasattr(ol, 'pack_parent_line_id'):
                ol.pack_parent_line_id = False

            # Create a dummy python object to hold editable data without
            # updating database content
            line = SimpleNamespace(
                name=ol.name,
                partner_id=ol.partner_id,
                pack_parent_line_id=ol.pack_parent_line_id,
                product_id=ol.product_id,
                product_uom=ol.product_uom,
                product_qty=ol.product_qty,
                price_subtotal=ol.price_subtotal,
                price_unit=ol.price_unit,
                taxes_id=ol.taxes_id,
                date_planned=ol.date_planned,
            )

            # Check if line should be hidden based on wizard data
            if line.pack_parent_line_id:
                if pack_print == 'hide':
                    continue

            # If line must be totalized to avoid multiple lines for same
            # the same product then check if lines could be virtually merged
            if total_amounts:
                # Browse existing added line
                if _totalize_printed_lines(line, lines):
                    continue

            # Check if price should be hidden based on wizard data
            if line.pack_parent_line_id:
                line.hide_price = pack_hide_prices
            else:
                line.hide_price = False
            
            # Set default product code and name
            line.supplier_code = line.product_id.default_code
            line.supplier_name = line.product_id.name

            # Get supplier info from current partner_id
            supplier_info = line.product_id.seller_ids.filtered(
                lambda s: (
                    s.product_id == line.product_id \
                    and s.name == line.partner_id
                )
            )
            # Try again if product variant is enabled
            if not supplier_info:
                supplier_info = line.product_id.seller_ids.filtered(
                    lambda s: (
                        s.product_tmpl_id == line.product_id.product_tmpl_id \
                        and s.name == line.partner_id
                    )
                )

            # Retrieve product code and name from supplier
            if supplier_info:
                line.supplier_code = supplier_info[0].product_code or line.supplier_code
                line.supplier_name = supplier_info[0].product_name or line.supplier_name

            # Re-format default line name from supplier product data
            # If they don't match then copy line.name (was line.notes in
            # older versions) to line.notes
            supplier_product = '[{0}] {1}'.format(
                line.supplier_code,
                line.supplier_name,
            )
            if line.name != supplier_product:
                line.notes = line.name
            else:
                line.notes = False

            # Also raise a tag to help report maker to display line notes
            line.has_notes = (line.notes is not False)

            lines.append(line)

        return lines
