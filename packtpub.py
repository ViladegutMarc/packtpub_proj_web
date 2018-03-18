#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
"""
Client packtpub simple

@author: Marc Viladegut
"""

import urllib2
import bs4

class ClientPacktpub(object):

    def get_web(self, url):
        fd = urllib2.urlopen(url)
        html = fd.read()
        fd.close()
        return html

    def parse_html(self, html):
        book = []
        soup = bs4.BeautifulSoup(html, "lxml")
        soup = soup.find("div", "dotd-main-book-summary float-left")

        divs = soup.findAll("div")
        for div in divs:
            book.append(div.text.replace("\t", "").replace("\n", ""))

        return book

    def print_results(self, book):
        title = "----- " + book[1] + " -----"
        description = book[2] + "\n" + book[3]
        print title + "\n\n" + description + "\n"

    def run(self):
        try:
            html = self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
        except:
            print "Error en l'accés a la URL especificada"
            exit(-1)
        list_book = self.parse_html(html)
        self.print_results(list_book)

if __name__== "__main__":
    client = ClientPacktpub()
    client.run()
