Nickname generator
(supports cyrillic and latin)

Installation:
$ pip install nickname_generator
or (replace * with proper version)
$ pip install dist/nickname_generator-*.tar.gz

Usage:
>>> from nickname_generator import generate
>>> print(generate())
Nickname

or

$ python nickname_generator
Nickname

Options:
You can specify locale (available 'en' and 'ru' values).
>>> from nickname_generator import generate
>>> print(generate('ru'))
Никнейм

Or pass it as argument in console:

$ python nickname_generator ru
Никнейм