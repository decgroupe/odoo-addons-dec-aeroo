# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Mar 2020

from odoo import models


class Product(models.Model):
    _inherit = 'product.product'

    def print_manufacturer(self):
        res = ''
        categ_id = self.categ_id
        if categ_id:
            while categ_id.parent_id and (categ_id.parent_id.id != 1):
                categ_id = categ_id.parent_id
            if categ_id != self.categ_id:
                res = ('%s - %s') % (categ_id.name, self.categ_id.name)
            else:
                res = ('%s') % (categ_id.name)
        return res
