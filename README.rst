Generate config files from 'skeleton' templates
===============================================

Requirements
------------

python, python-paster

Usage
-----

1. Install skeletons
2. In target directory run: ::

    paster create -t <template name>

Options
--------

For more options run ``paster create --help``


Templates
----------

Duply config
````````````

**Template name** duply

This template contains configuration for duply backups with Amazon S3 backend.
Variables:

**passphrase**
    Passphrase for synchromous encryption. Default: '__top_secrect__'
**bucket**
    Bucket name. Default: 'ru.redsolution.hammy'
**key**
    S3 Key. Default: '__KEY__'
**secret**
    S3 secret. Default: '__SECRET__'

Lighttpd + mod_fcgi
````````````````````

**Template name** lighttpd_mod_fcgi

This template contains configuration for lighttpd web server to run website
 as separate process, launched and monitored by monit deamon.

**domain**
    Main domain(s). For example: mysite.com, mysite.org, мойсайт.рф
    IDN domains will be automatically quoted.

**redirects**
    Alternate hostnames, which will show only redirect to the firdst main site.
    Example: www.mysite.com, www.mysite.org
**project_root**  Where your sites are located. Tempaltes suppose that your
    code located at: ``{{ project_root}}/{{package}}``, so do not include
    package name into ``project_root``.
