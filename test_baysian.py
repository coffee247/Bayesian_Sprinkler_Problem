#!/usr/bin/env python3

import unittest
import Bayesian

''' Tests by James M. Stallings '''

class TestMain(unittest.TestCase):

    ''' Test creation of bayesion object from class definition '''
    def test_create_beysian_object(self):
        raised = False
        try:
            mysprinkler = Bayesian.bayesian_sprinkler()
        except:
            raised = True
        self.assertFalse(raised, 'Exception raised')

    ''' Test creation of mask from user input '''
    def test_create_mask_FFF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, False, False)
        self.assertEqual(mask, 0)

    def test_create_mask_FFT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, False, True)
        self.assertEqual(mask, 1)

    def test_create_mask_FTF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, True, False)
        self.assertEqual(mask, 2)

    def test_create_mask_FTT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, True, True)
        self.assertEqual(mask, 3)

    def test_create_mask_TFF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, False, False)
        self.assertEqual(mask, 4)

    def test_create_mask_TFT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, False, True)
        self.assertEqual(mask, 5)

    def test_create_mask_TTF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, True, False)
        self.assertEqual(mask, 6)

    def test_create_mask_TTT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, True, True)
        self.assertEqual(mask, 7)


    ''' test for No None's in input values '''
    def test_summing_out_FFF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, False, False)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 1.0)

    def test_summing_out_FFT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, False, True)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.0)

    def test_summing_out_FTF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, True, False)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.2)

    def test_summing_out_FTT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, True, True)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.8)

    def test_summing_out_TFF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, False, False)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.1)

    def test_summing_out_TFT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, False, True)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.9)

    def test_summing_out_TTF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, True, False)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.01)

    def test_summing_out_TTT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, True, True)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.99)

    ''' test for when None is in wetgrass place in input values '''
    def test_summing_out_FFN(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, False, None)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 'Wetgrass must have a value (cannot be None)')

    def test_summing_out_FTN(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, True, None)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 'Wetgrass must have a value (cannot be None)')

    def test_summing_out_TFN(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, False, None)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 'Wetgrass must have a value (cannot be None)')

    def test_summing_out_TTN(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, True, None)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 'Wetgrass must have a value (cannot be None)')

    ''' test for when None is in rain place in input values '''
    def test_summing_out_FNF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, None, False)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 1.2)

    def test_summing_out_FNT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, None, True)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.8)

    def test_summing_out_TNF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, None, False)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.11)

    def test_summing_out_TNT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, None, True)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 1.89)

    ''' test for when None is in sprinkler place in input values '''
    def test_summing_out_NFF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(None, False, False)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 1.1)

    def test_summing_out_NFT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(None, False, True)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.9)

    def test_summing_out_NTF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(None, True, False)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 0.21)

    def test_summing_out_NTT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(None, True, True)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 1.79)

    ''' test for when None is in both sprinkler AND rain place in input values '''
    def test_summing_out_NNT(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(None, None, True)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 1.0)

    def test_summing_out_NNF(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(None, None, False)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 1.0)

    ''' test for when None is in both sprinkler AND wetgrass place in input values '''
    def test_summing_out_NTN(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(None, True, None)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 'Wetgrass must have a value (cannot be None)')

    def test_summing_out_NFN(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(None, False, None)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 'Wetgrass must have a value (cannot be None)')

    ''' test for when None is in both rain AND wetgrass place in input values '''
    def test_summing_out_TNN(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(True, None, None)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 'Wetgrass must have a value (cannot be None)')

    def test_summing_out_FNN(self):
        mysprinkler = Bayesian.bayesian_sprinkler()
        #    mask = mysprinkler.makeMask(sprinkler=True, rain=False, wetGrass=None)
        mask, removed = mysprinkler.makeMask(False, None, None)
        self.assertEqual(mysprinkler.pIsWet(mask, removed), 'Wetgrass must have a value (cannot be None)')

if __name__ == '__main__':
    unittest.main()
