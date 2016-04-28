import re
try:
    import simplejson as json
except ImportError:
    import json

from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from ckeditor.settings import *

configs = dict((k, json.dumps(v)) for k, v in CONFIG.items())
grapelli = 'grappelli' in getattr(settings, 'INSTALLED_APPS', [])
media = '%s' % settings.STATIC_URL.rstrip('/')


class CKEditorCommon(object):
    def render(self, name, value, attrs=None, **kwargs):
        rendered = super(CKEditorCommon, self).render(name, value, attrs)
        context = {
            'name': name,
            'config': configs[self.ckeditor_config],
            'filebrowser': FILEBROWSER,
            # This "regex" should match the ID attribute of this field.
            # The reason we use a regex is so we can handle inlines, which will have
            # IDs like: id_subsection-6-description
            'regex': attrs['id'].replace('__prefix__', r'\d+'),
        }
        return rendered +  mark_safe(render_to_string(
            'ckeditor/ckeditor_script.html', context
        ))

    def value_from_datadict(self, data, files, name):
        val = data.get(name, u'')
        r = re.compile(r"""(.*?)(\s*<br\s*/?>\s*)*\Z""", re.MULTILINE | re.DOTALL)
        m = r.match(val)
        return m.groups()[0].strip()

    class Media:
        js = (
            media + '/ckeditor/js/ckeditor/ckeditor.js',
            media + '/ckeditor/js/init.js',
        )
        css = {
            'screen': (
                media + '/ckeditor/css/' + ('grappelli.css' if grapelli else 'standard.css'),
            ),
        }


class CKEditor(CKEditorCommon, forms.Textarea):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.get('attrs', {})
        attrs['class'] = 'django-ckeditor'
        kwargs['attrs'] = attrs
        self.ckeditor_config = kwargs.pop('ckeditor_config', 'default')
        super(CKEditor, self).__init__(*args, **kwargs)


class AdminCKEditor(CKEditorCommon, forms.Textarea):
    def __init__(self, attrs={}, ckeditor_config=None):
        if 'class' in attrs:
            attrs['class'] += ' django-ckeditor'
        else:
            attrs.update({'class': 'django-ckeditor'})
        self.ckeditor_config = ckeditor_config
        super(AdminCKEditor, self).__init__(attrs=attrs)
