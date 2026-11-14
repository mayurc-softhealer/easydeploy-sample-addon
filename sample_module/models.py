from odoo import fields, models


class SampleNote(models.Model):
    _name = "sample.note"
    _description = "Sample note"

    name = fields.Char(required=True)
