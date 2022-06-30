[SA Launch] Team 5 - Extending DNS into AWS VPC
=======================

Overview
----------

* Django backend server runs at IDC (on-premise) network and connects to RDS by resolving its service name.

Setup
-------
1. Configure Route53 to forward DNS queries for both your AWS VPC and On-prem
2. Setup RDS in your one of AWS VPC and subnet connected via Route53 resolver
3. Setup django app server
    * ``docker-compose -f local.yml build``
    * ``docker-compose -f local.yml up -d``
4. To see logs,
    * ``docker-compose -f local.yml logs -f``
5. Create superuser
    * ``docker-compose -f local.yml run --rm django python manage.py createsuperuser``

