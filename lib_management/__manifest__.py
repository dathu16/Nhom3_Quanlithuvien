{
    'name': 'Library Management',
    'version': '14.0.1.0.0',
    'summary': """Module help library management.""",
    'description': """
    Author: Nhóm 44K21.2
    Members:
    - Nguyễn Thùy Dung
    - Đỗ Anh Thư
    - Phan Thị Thùy Trang
    """,
    'category': 'Library',
    'author': '44K21.2',
    'company': '',
    'maintainer': '44K21.2',
    'website': '',
    'depends': [
        'hr', 'product'
    ],
    'data': [
        # SECURITY
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        # DATA
        'data/ir_sequence_data.xml',
        # VIEWS
        'views/assets.xml',
        'views/shelve_book_views.xml',
        'views/book_views.xml',
        'views/book_category_views.xml',
        'views/reader_views.xml',
        'views/call_card_views.xml',
        'views/violation_views.xml',
        # .. reports
        'views/report_views.xml',
        # .. wizards
        'wizard/confirm_return_book_wizard_views.xml',
        # Menus
        'menu/menu_views.xml',
    ],
    'demo': [],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
