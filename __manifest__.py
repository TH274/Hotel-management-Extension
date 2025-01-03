{
    'name': 'Hotel Room Extension',
    'version': '1.0',
    'summary': 'Add more fields to hotel room model and add a hotel booking history',
    'author': 'Odoo S.A',
    'depends': ['hotel_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_room_views.xml',
        'views/hotel_history_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
