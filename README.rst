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
