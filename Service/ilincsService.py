#!/usr/bin/env python
#
# Author: Behrouz Shamsaei <behrouz.shamsaei@uc.edu>
# Date: Sep 2016
#
import requests
#import csv
#from requests.exceptions import Timeout

class IlincsSearch(object):
    """Client class is to connect the prosite server and psi-mod csv file to search2 for motifs.
    :param motifs: List of motifs to be searched.
    :param timeout: API request timeout
    :param retries: Number of times to retry request if timeout received
    """

    # API URLs for searching for motifs
    ilincs_URL_BASE = 'http://www.ilincs.org/api/SignatureMeta?filter=%7B%22where%22%3A%7B%22treatment%22%3A%22'
    ilincs_URL_END = '%22%2C%20%22libraryid%22%3A%22LIB_6%22%7D%7D'
    TIMEOUT = 120
    RETRIES = 3

    sigid_URL_BASE = 'http://www.ilincs.org/api/SignatureMeta/findConcordantSignatures?sigID=%22'
    sigid_URL_END = '%22&lib=%22LIB_5%22'


    #PROSITE_URL_FORMAT = '&lineage=9606&db=sp&output=json'


    def __init__(self,
                 timeout=TIMEOUT,
                 retries=RETRIES):

        assert(timeout >= 0)
        self.timeout = timeout or self.TIMEOUT

        assert(isinstance(retries, int) and retries >= 0)
        self.retries = retries or self.RETRIES

    def search_gene(self, gene_name):
        """Prosite search2 for motif API request

        :param gene_name: motif search2 string
        """
        print "finding gene-KD signatures"
        url = self.ilincs_URL_BASE + gene_name + self.ilincs_URL_END

        response = self._request(url)
        search_result = self._extract_response(response)
        #print response.text
        return search_result

    def search_sigid(self, id):
        """Prosite search2 for motif API request

        :param id: motif search2 string
        """

        url = self.sigid_URL_BASE + id + self.sigid_URL_END

        response = self._request(url)
        search_result = self._extract_response(response)
        #print response.text
        return search_result


    def _request(self, url):
        """Generic prosite request which attaches meta info (e.g. auth)

        :param url: URL of endpoint
        :param gene_name: GET params of request
        """

        response = requests.get(url,
                                timeout=self.timeout)

        return response


    def _extract_response(self, response):
        """Extract data from api resposne"""
        return response.json()


