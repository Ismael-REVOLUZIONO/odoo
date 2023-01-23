{
    'name': 'Qweb PDF',
    'version': '16.0.0',
    'author': 'QUADIT',
    'website': 'http://www.quadit.mx',
    'license': 'AGPL-3',
    'summary': 'proyecto reporte pdf QWEB',
    'depends': ['contacts','base'],
    'data': [
        'report/pdf_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}