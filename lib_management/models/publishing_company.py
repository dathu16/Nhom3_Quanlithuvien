from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PublishingCompany(models.Model):
    _name = 'publishing.company'
    _description = 'Nhà xuất bản'

    name = fields.Char(string="Nhà xuất bản", required=True)
    address = fields.Char(string="Địa chỉ")