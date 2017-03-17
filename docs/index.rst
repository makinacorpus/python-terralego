.. Terralego documentation master file, created by
   sphinx-quickstart on Fri Mar 17 11:44:53 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Terralego's documentation!
=====================================

Getting started
---------------

Install using pip::

   pip install terralego

Set your credentials using the environment variables::

   export TERRALEGO_USER="my_user"
   export TERRALEGO_PASSWORD="my_password"

You can now use terralego::

   from terralego import geocoding

   results = geocoding.search('paris france')

Contents:

.. toctree::
   :maxdepth: 2

   geocoding
   geodirectory


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

