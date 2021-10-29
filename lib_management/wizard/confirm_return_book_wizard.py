from odoo import api, fields, models


class ConfirmReturnBookWizard(models.TransientModel):
    _name = 'confirm.return.book.wizard'
    _description = 'confirm.return.book.wizard'

    call_card_id = fields.Many2one('call.card', string='ID Phiếu mượn')
    comment = fields.Text(string='Ghi chú')

    def confirm(self):
        self.ensure_one()
        call_card_id = self.call_card_id
        if not call_card_id:
            call_card_id = self.env['call.card'].browse(self._context.get('ctx_call_card_id', False))
        current_employee_id = self.env['hr.employee'].search([('user_id', '=', self._uid)], limit=1)
        call_card_id.write({
            'end_date': fields.Date.today(),
            'manager_id': current_employee_id and current_employee_id.id or False,
            'return_note': self.comment,
            'state': 'returned',
        })
        return True
