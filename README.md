# Intersectional word file

Smash the Spell Check Kyriarchy!

Requires: Python, python-enchant, enchant, make

Instructions:
    git clone https://github.com/wushin/intersectional-word-file.git
    cd intersectional-word-file && make install

    make install - installs the default system LANG
    make check - checks Lang list against default LANG dict
    make Lang="en_US" install-extra - installs the words from Lang file as well
    make Lang="en_US" check-extra - checks the words from Lang file as well
    make Lang="en_US" clean - Sorts and Uniques (not on case) Lang wordlist file

lang.py:
    -i install files
    -c check files
    -l,--lang= Locale (defaults to system)


Personal Word List is in ~/.config/enchant/ (Debian Stretch).
