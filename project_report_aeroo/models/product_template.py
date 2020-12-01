# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Dec 2020

from odoo import models, api

class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.multi
    def _get_aeroo_report_filename(self):
        names = [x.name or str(x.id) for x in self]
        res = '-'.join(names)
        return res
