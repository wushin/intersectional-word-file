#!/usr/bin/python
# -*- encoding: utf-8 -*-

##    add_lang.py - Extract wordlist and add it to your personal dictionaries.
##
##    Copyright © 2016 Wushin <pasekei@gmail.com>
##
##    This file is part of Intersection Word List
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

import os,sys,getopt
import locale
import enchant

class IWF_Lang(object):

    def __init__(self,Lang):
        self.lang = Lang
        self.pwl_file = '%s/.config/enchant/%s.dic' % (os.getenv("HOME"), self.lang)
        try:
            self.wl_file = open('%s.wordlist' % self.lang, 'r')
        except:
            print "%s language file not found." % self.lang

    def usage(self):
        print "IWF needs more input"
        print "-i install"
        print "-c check"
        print "-l,--lang= Locale (defaults to system)"

    def install(self):
        print "Installing %s Intersectionalism..." % self.lang
        for line in self.wl_file:
            per_word_list = enchant.DictWithPWL(self.lang, pwl=self.pwl_file)
            if not per_word_list.is_added(line.rstrip('\n')):
                print "Adding %s" % (line.rstrip('\n'))
                per_word_list.add(line.rstrip('\n'))

    def check(self):
        print "Checking %s word list" % self.lang
        for line in self.wl_file:
            word_list = enchant.Dict(self.lang)
            if not word_list.check(line.rstrip('\n')):
                print "%s exists already" % (line.rstrip('\n'))
                print line.rstrip('\n')

def main(argv):
    operation = "usage"
    (Lang, encoding) = locale.getdefaultlocale()
    try:
        opts, args = getopt.getopt(argv,"icl:", ["lang="])
    except:
        iwf_langer = IWF_Lang(Lang)
        getattr(iwf_langer, operation)()
        sys.exit(0)
    for opt, arg in opts:
        if opt in ("-l", "--lang"):
            Lang = arg
        elif opt == "-i":
            operation = "install"
        elif opt == "-c":
            operation = "check"
    iwf_langer = IWF_Lang(Lang) 
    getattr(iwf_langer, operation)()

if __name__ == '__main__':
    main(sys.argv[1:])
