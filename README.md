# SCRUD Webapp Example

Search, Create, Read, Update and Delete application for MySQL database table.

Implemented using Python, Flask, SQLAlchemy, DataTables, JQuery, AJAX, JSON, and MySQL.

User must create a MySQL database and table as specified in 'queries.sql'. User must define DB_USERNAME, DB_PASSWORD, and DATABASE_FILE in config.py or an operating system environment file.

References:
https://www.sitepoint.com/creating-a-scrud-system-using-jquery-json-and-datatables/

This webapp is a Python version of the sitepoint.com example which uses php. The list below indicates which files were modified.

* index.html : not modified
* layout.css : not modified
* queries.sql : not modified
* webapp.js : minor modifications
* data.php : converted to python in file views.py
* __init__.py : new file
* config.py : new file
* models.py : new file
* run.py : new file

The new files could have been combined into one file for this simple webapp, but this is the file structure I use in more complicated apps.

============================

philblower@gmail.com
20171029
