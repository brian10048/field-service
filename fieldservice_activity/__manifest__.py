
# Copyright (C) 2019, Brian McMaster
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Field Service - Activities',
    'summary': 'Manage Actitivies and Outcomes on Field Service Orders',
    'version': '12.0.0.1.0',
    'license': 'AGPL-3',
    'author': 'McMaster Lawn & Pest Services, '
              'Open Source Integrators, '
              'Odoo Community Association (OCA)',
    'category': 'Field Service',
    'website': 'https://github.com/OCA/field-service',
    'depends': [
        'fieldservice',
    ],
    'data': [
        'views/fsm_activity_template.xml',
        'views/fsm_activity.xml',
        'views/fsm_condition.xml',
        'views/fsm_template.xml',
        'views/fsm_order.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'development_status': 'Beta',
    'maintainers': [
        'wolfhall',
        'max3903',
        'brian10048',
    ],
}
