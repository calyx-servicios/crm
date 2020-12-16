{
    'name': 'Crm suscribe all subtypes',
    'version': '11.0.1.0.0',
    'category': 'Tools',
    'author': "Calyx",
    'website': 'www.calyxservicios.com.ar',
    'license': 'AGPL-3',
    'summary': '''Makes the follower, by default, subscribed to all subtypes''',
    'depends': [
        'crm',
        'mail',
        
    ],
    'external_dependencies': {
    },
    'data': [
        'data/crm_lead_data.xml'
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
