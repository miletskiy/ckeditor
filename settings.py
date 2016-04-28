from django.conf import settings


configs = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Format',
             '-', 'SpellChecker', 'Scayt',
             '-', 'Maximize',
             ],
            ['HorizontalRule',
             '-', 'Table',
             '-', 'BulletedList', 'NumberedList',
             '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
             '-', 'SpecialChar', 'Image',
             '-', 'Source',
             '-', 'About',
             ]
        ],
        'width': 600,
        'height': 300,
        'toolbarCanCollapse': True,
        },
    'small': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Format',
             '-', 'SpellChecker', 'Scayt',
             '-', 'Maximize',
             ],
            ['HorizontalRule',
             '-', 'Table',
             '-', 'BulletedList', 'NumberedList',
             '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
             '-', 'SpecialChar', 'Image',
             '-', 'Source',
             '-', 'About',
             ]
        ],
        'width': 600,
        'height': 300,
        'toolbarCanCollapse': True,
        },
    'full': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Format',
             '-', 'SpellChecker', 'Scayt',
             '-', 'Maximize',
             ],
            ['HorizontalRule',
             '-', 'Table',
             '-', 'BulletedList', 'NumberedList',
             '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
             '-', 'SpecialChar', 'Image',
             '-', 'Source',
             '-', 'About',
             ]
        ],
        'width': 900,
        'height': 300,
        'toolbarCanCollapse': False,
        }

}

FILEBROWSER = getattr(settings, 'CKEDITOR_FILEBROWSER', '/admin/filebrowser/browse/?pop=3')
CONFIG = getattr(settings, 'CKEDITOR_CONFIGS', configs)
