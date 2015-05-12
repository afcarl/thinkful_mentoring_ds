Notes on SQL JOINS
=================

Suppose we have the following tables (as in this lessons database):


cities:

	name           state
    ('Boston',     'MA')
    ('Chicago',    'IL')
    ('Miami',      'FL')
    ('Dallas',     'TX')
    ('Portland',   'OR')
    ('Atlanta',    'GA')
    ('Washington', 'DC')
    ('Houston', "  'TX')


weather:
    city              year  warmest      coolest    avg_high
 	('New York City', 2013, 'July',      'January',  62),
    ('Boston',        2013, 'July',      'January',  59),
    ('Chicago',       2013, 'July',      'January',  59),
    ('Chicago',       2012, 'August',    'January',  59),
    ('Miami',         2013, 'August',    'January',  84),
    ('Miami',         2014, 'July',      'January',  87),
    ('Dallas',        2013, 'July',      'January',  77),
    ('Seattle',       2013, 'July',      'January',  61),
    ('Portland',      2013, 'July',      'December', 63),
    ('San Francisco', 2013, 'September', 'December', 64),
    ('Los Angeles',   2013, 'September', 'December', 75)

