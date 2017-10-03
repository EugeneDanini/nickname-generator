##################
Nickname generator
##################
(supports cyrillic and latin)

Installation and usage
----------------------

From pypi:

.. code-block:: bash

    $ pip install nickname_generator

From dist:

.. code-block:: bash

    $ pip install dist/nickname_generator-*.tar.gz


Script usage:

.. code-block:: python

    >>> from nickname_generator import generate
    >>> print(generate())
    Nickname


Console usage:

.. code-block:: bash

    $ python nickname_generator
    Nickname

Options
-------

You can specify locale (available 'en' and 'ru' values).

For example:

.. code-block:: python

    >>> from nickname_generator import generate
    >>> print(generate('ru'))
    Никнейм

Or pass it as argument in console:

.. code-block:: bash

    $ python nickname_generator ru
    Никнейм