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
    """
    La classe ClientPacktpub conté diversos mètodes estàtic que serveixen per obtenir tant el codi HTML
    d'una pàgina, com parsejar el codi html i per últim mostrar les dades pertinents del llibre que està
    en oferta de la pàgina Packtpub.
    """
    @staticmethod
    def get_web(url):
        """
        Mètode estàtic on s'obté tot el codi html de l'adreça passada per paràmetre.
        :param url: Adreça la qual es vol obtenir el codi HTML.
        :return: El codi HTML de la pàgina sol·licitada.
        """
        fd = urllib2.urlopen(url)
        html = fd.read()
        fd.close()
        return html

    @staticmethod
    def parse_html(html):
        """
        Mètode estàtic on es parseja tot el codi HTML passat per paràmetre. Es queda amb un troç en concret.
        :param html: El codi HTML de la pàgina web sol·licitada.
        :return: La llista amb el títol, descripció i punt interessants del llibre.
        """
        book = []
        soup = bs4.BeautifulSoup(html, "lxml")
        soup = soup.find("div", "dotd-main-book-summary float-left")

        divs = soup.findAll("div")
        for div in divs:
            book.append(div.text.replace("\t", "").replace("\n", ""))

        return book

    @staticmethod
    def print_results(book):
        """
        Veure els resultats per pantalla
        :param book: La llista amb el títol, descripció i punt interessants del llibre.
        """
        title = "----- " + book[1] + " -----"
        description = book[2] + "\n" + book[3]
        print title + "\n\n" + description + "\n"

    def run(self):
        """
        Mètode principal per obtenir, parsejar i mostrar el llibre d'oferta actualment.
        """
        try:
            html = self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
        except Exception as e:
            print "Error en l'accés a la URL especificada: " + e
            exit(-1)

        list_book = self.parse_html(html)
        self.print_results(list_book)


if __name__ == "__main__":
    client = ClientPacktpub()
    client.run()
