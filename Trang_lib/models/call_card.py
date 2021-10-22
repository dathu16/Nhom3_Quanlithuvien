from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CallCard(models.Model):
    _name = 'call.card'
    _description = 'call.card'
    _rec_name = 'code'

    code = fields.Char(string='Số phiếu mượn', default="/")
    reader_id = fields.Many2one('res.partner', string='Tên độc giả', required=True)
    reader_code = fields.Char(string='Mã độc giả')
    start_date = fields.Date(string='Ngày mượn sách', default=lambda self: fields.Date.context_today(self), required=True)
    end_date = fields.Date(string='Ngày trả sách')
    due_date = fields.Date(string='Ngày đáo hạn')
    manager_id = fields.Many2one('hr.employee', string='Người xác nhận')
    description = fields.Text(string='Ghi chú mượn')
    return_note = fields.Text(string='Ghi chú trả')
    line_ids = fields.One2many('call.card.details', 'card_id', string='Chi tiết mượn')
    state = fields.Selection([
        ('confirmed', 'Đang mượn'),
        ('returned', 'Đã trả'),
        ('violate', 'Vi Phạm'),
    ], string='Trạng thái')
    total_book = fields.Integer(string='Tổng số sách mượn', compute='_compute_total_book', store=True, compute_sudo=True)


class CallCardDetails(models.Model):
    _name = 'call.card.details'
    _description = 'call.card.details'

    card_id = fields.Many2one('call.card', string='ID phiếu mượn sách')
    book_id = fields.Many2one('product.template', string='Tên sách', domain="[('is_book','=',True)]")
    book_code = fields.Char(string='Mã sách', related='book_id.default_code')
    publishing_company = fields.Char(string='Nhà xuất bản', related='book_id.publishing_company')
    quantity = fields.Integer(string='Số lượng', default=1)
    description = fields.Text(string='Ghi chú')
