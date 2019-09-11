#!/usr/bin/python

# import pg as pg
import psycopg2 as pg
import requests
import numpy as np


# conn = pg.DB(host="localhost", user="postgres", passwd="postgres", dbname="lincs2lincs")


# connection = psycopg2.connect("dbname=lincs2lincs user=NAME password=PASSWORD")
# cursor = connection.cursor()
#print('We made it this far')

# result = conn.query("SELECT similarity FROM lsm_ids WHERE lsm_id = 'LSM-17536' and similarity > 0.9615 ")

distance_list = []
list_of_match_sims = []


class SearchQuery:
    def __init__(self):
        pass
    def report_matrix(self, lsm_input, concordance_input, size, input_compound_df):
    # def report_lsm(self, list_input):
    #     list_of_500 = list_input
        #output = np.zeros((size + len(input_compound_df),size+ len(input_compound_df)))

        output = np.zeros((size , size ))

        lsm_list = lsm_input.split(',')
        concordance_list = concordance_input.split(',')
        i = 0
        j = 0
        #print "before loop inside searchQuery"
        while i < size:
            output[i][i] = 1.0
            j = i + 1
            while j < size:
                if lsm_list[i] == lsm_list[j]:
                    output[i][j] = 1.0
                    output[j][i] = 1.0
                j += 1
            i += 1




        print "inside searchQuery"

        # print(np.unique(lsm_list))
        # print len(np.unique(lsm_list))
        #
        # print len(lsm_list)
        # print lsm_list
        # print len(lsm_list)
        # print len(concordance_list)


        for item in range(len(lsm_list)):
            dictname = dict(the_lsm=lsm_list[item], concord=concordance_list[item])
            list_of_match_sims.append(dictname)


        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
        }

        data = {
          'lsmList': lsm_list,
          # 'minSimilarity': '0.03'
        }

        data2 = {
            'lsmList': ['LSM-4132','LSM-3359'],
            # 'minSimilarity': '0.03'
        }
        response = requests.post('http://dev.ilincs.org/api/ilincsR/lsmConcordances', headers=headers, data=data)

        response2 = requests.post('http://dev.ilincs.org/api/ilincsR/lsmConcordances', headers=headers, data=data2)
        #print 'Concordances Retrieved.'



        # print len(response.json())
        # print "inside searchQuery response.json():"
        #

        print response
        print response.json()
        # print response
        # print lsm_list
        for item in response.json():
            print item
            lsm1 = str(item['firstChemID'])
            lsm2 = str(item['secondChemID'])
            similarity = item['similarity']
            indices1 = [i for i, x in enumerate(lsm_list) if x == lsm1]
            indices2 = [i for i, x in enumerate(lsm_list) if x == lsm2]
            # print "-----"
            # print item
            # print indices1
            # print indices2
            # print similarity
            # print "-----"
            for item1 in indices1:
                for item2 in indices2:
                    output[item1][item2] = similarity
                    output[item2][item1] = similarity

        # print "inside searchQuery response2.:"
        #
        # print response2.json()
        # print len(response2.json())

        return output


