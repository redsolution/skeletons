# -*- coding: utf-8 -*-
from paste.script.templates import Template, var
from paste.util.template import paste_script_template_renderer

class BaseTemplate(Template):
    template_renderer = staticmethod(paste_script_template_renderer)

class DuplyTemplate(BaseTemplate):
    _template_dir = 'templates/duply'
    summary = 'Duply code and database backup config, uses Amazon S3 backend'
    
    vars = [
        var('passphrase', 'Passphrase for synchromous encryption', default='__top_secrect__'),
        var('bucket', 'Bucket name', default='ru.redsolution.hammy'),
        var('key', 'S3 Key', default='__KEY__'),
        var('secret', 'S3 secret', default='__SECRET__'),
#        var('folder', 'Backups S3 folder', should_echo=False),
#        var('dbname', 'Database name', should_echo=False),
    ]

    def pre(self, command, output_dir, vars):
        vars.update({
            'folder': vars['package'],
            'dbname': vars['package'],
        })
