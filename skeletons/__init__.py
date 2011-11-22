# -*- coding: utf-8 -*-
from paste.script.templates import Template, var
from paste.util.template import paste_script_template_renderer
import re

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
    ]

    def pre(self, command, output_dir, vars):
        vars.update({
            'folder': vars['package'],
            'dbname': vars['package'],
        })

class LighttpdModFastCGI(BaseTemplate):
    _template_dir = 'templates/lighttpd_fcgi'
    summary = 'Set of configs for lighttpd and monit for site launch via mod_fcgi'

    vars = [
        var('domain', 'Main domain(s)'),
        var('redirects', 'Site redirects'),
        var('project_root', 'Where your site is located'),
    ]

    def build_regexp(self, value):
        domains = []
        for domain in value.split(','):
            domains.append('(^%s$)' % self.prepare_domain(domain))
        return '|'.join(domains)

    def prepare_domain(self, value, escape=True):
        domain = value.strip()
        domain = unicode(domain.decode('utf-8')).encode('idna')
        if escape:
            return re.escape(domain)
        else:
            return domain

    def pre(self, command, output_dir, vars):
        vars['site_domains'] = self.build_regexp(vars['domain'])
        vars['redirects'] = self.build_regexp(vars['redirects'])
        vars['main_domain'] = self.prepare_domain(vars['domain'].split(',', 1)[0], escape=False)
