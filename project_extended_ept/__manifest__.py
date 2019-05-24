{
    'name': 'Project Extended',
    'summary': ' Extend for Project Task',
    'version': '1.0',
    'author': 'Emipro Technologies Pvt. Ltd.',
    'website': 'http://www.emiprotechnologies.com',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',
    'category': 'Project',
    'depends': ['project','sale_timesheet'
                ],
    'data': [
        'views/project_task_view.xml',
        'security/ir.model.access.csv',
        'views/project_project_view.xml',
        'views/hr_employee_view.xml',
    ],

    'images': ['static/description/icon.jpg'],

    'installable': True,
    'application': True,
    'auto_install': False,
}
