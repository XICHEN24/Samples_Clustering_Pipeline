# -*- coding: utf-8 -*-
"""
Created on WEd Aug  17 2016

@author: del
@author: The Gene Sets Characterization dev team
"""
import unittest
import os
import numpy as np
import scipy.sparse as spar
import scipy.stats as stats

class sample_clustering_toolbox_test(unittest.TestCase):
    def get_run_parameters(self):
        run_parameters = {'test_directory': '/Users/lanier4/BigDataTank/nbs_run',
                          'k': 3, 'number_of_iteriations_in_rwr': 100,
                          'obj_fcn_chk_freq': 50,
                          'it_max': 10000,
                          'h_clust_eq_limit': 100,
                          'restart_tolerance': 0.0001,
                          'lmbda': 1400,
                          'percent_sample': 0.8,
                          'number_of_bootstraps': 3,
                          'display_clusters': 1,
                          'restart_probability': 0.7,
                          'verbose': 1,
                          'use_now_name': 1000000}

        return run_parameters

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(sample_clustering_toolbox_test))

    return test_suite


'''# Next two lines for using this file w/o test Suite   << NOT recommended
#if __name__=='__main__':
#    unittest.main()

                                        >> Preferred Method for using unit test
import unittest
import TestKEGmodule as tkeg
mySuit = tkn.suite()
runner = unittest.TextTestRunner()
myResult = runner.run(mySuit)

OR
mySuit2 = unittest.TestLoader().loadTestsFromTestCase(TestKEGmodule)

'''