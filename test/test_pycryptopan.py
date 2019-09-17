#!/usr/bin/env python3
import unittest
from cryptopan import CryptoPan


class TestPyCryptoPan(unittest.TestCase):

    # XXX FIXME! replace by YOUR key of course
    key = "boojahyoo3vaeToong0Eijee7Ahz3yee"
    c = CryptoPan(key)

    def test_good_encryption(self):
        print("correctness test")
        self.assertEqual("206.2.124.120", self.c.anonymize("192.0.2.1"))
        print("OK")
        print("-" * 70)

    def test_perf(self):
        import time
        nb_tests = 1000
        print("starting performance check")
        stime=time.time()
        for i in range(0, nb_tests):
            self.c.anonymize("192.0.2.1")
        dtime=time.time() - stime
        print("%d anonymizations in %s s" %(nb_tests, dtime))
        print("rate: %f anonymizations /sec " %(nb_tests / dtime))
        self.assertTrue(True)
        print("OK")


if __name__ == '__main__':
    unittest.main()
