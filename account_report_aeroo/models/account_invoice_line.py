# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Mar 2020

from odoo import models

class AccountInvoiceLine(models.Model):
    _inherit = ['account.invoice.line', 'report.line.mixin']
    _name = 'account.invoice.line'
