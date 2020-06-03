# -*- coding: utf-8 -*-
{
    'name': "final",

    'summary': """
       Aplicacion final desarrollada por Cristobal
       Cenalmor para el modulo de ERPs""",

    'description': """
        Aplicacion final para ERPs que administrara y 
        gestionara informacion relativa a libros, autores
        y editoriales y sus relaciones. 
    """,

    'author': "cristobalcp",
    'website': "https://github.com/cristobalcp/final",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/final.xml',
        'views/reports.xml',
    ],
    'application':'True',
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
