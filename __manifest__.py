
{
    'name': 'Arrendamiento',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Modulo para administrar el arredamiento de inmuebles Kuale.',
    'author': 'Ivan Cruz Enlace',
    'depends': ['base', 'mail'],
    'data': [
        'views/property_views.xml',
        'views/property_visita_view.xml',
        'views/lessor_views.xml',
        'views/lease_contract_views.xml',
        'views/views.xml'
    ],
    'installable': True,
    'application': True,
}

