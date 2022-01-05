# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jan 2022

from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def get_qrcode_data(self):
        self.ensure_one()
        return self.product_tmpl_id.get_qrcode_data()

    def get_manufacturer(self):
        self.ensure_one()
        return self.product_tmpl_id.get_manufacturer()
