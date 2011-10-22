Fotos
=====

A minimalist photo log application written in Django.

Although most of the functions are in place (uploading pictures / displaying them), many things still need to be implemented better. Mostly just a proof of concept at this stage.


Requirements:
-------------
Fotos requires:

* Django==1.3.1
* sorl-thumbnail==11.09
* PIL==1.1.7

(Note: above are the only versions tested. Earlier and/or later versions might work too, except Django, it has to be 1.3 or above.)


Setup
-----
Do the following to setup:

1. Preferably setup a virtualenv and run `pip install -r requirements.txt`
1. Setup the database with `./manage syncdb`. Create a user named 'user' with the password you want people to access the site with.
1. git doesn't track directories so you have to manually do `mkdir media/`
1. Run locally with `./manage runserver` to see that everything runs smoothly.
1. PROFIT!


License
-------

Fotos is free software. It is distributed under the terms of the [GNU General Public License][gpl].

[gpl]: http://www.fsf.org/licensing/licenses/gpl.html
