#!/usr/bin/python
# -*- encoding: utf-8 -*-

##    add_lang.py - Extract wordlist and add it to your personal dictionaries.
##
##    Copyright © 2016 Wushin <pasekei@gmail.com>
##
##    This file is part of Intersection World List
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os,sys
import locale
import enchant

def main():
    home = os.getenv("HOME")
    (lang, encoding) = locale.getdefaultlocale()
    for line in open(('%s.wordlist' % (lang)), 'r'):
        per_word_list = enchant.DictWithPWL(lang, pwl=('%s/.config/enchant/%s.dic' % (home, lang)))
        if not per_word_list.is_added(line.rstrip('\n')):
            per_word_list.add(line.rstrip('\n'))

if __name__ == '__main__':
    main()
