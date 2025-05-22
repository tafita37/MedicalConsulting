{
    'name': 'MedicalConsulting',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  
        'views/medical_consulting_doctor_views.xml',
        'views/medical_consulting_client_views.xml',
        'views/medical_consulting_medication_views.xml',
        'views/medical_consulting_menus.xml'
    ],
    'author': 'Moi',
    'category': 'Uncategorized',
    'description': 'Medical consultation module.',
    'installable': True,
    'application': True,
}
