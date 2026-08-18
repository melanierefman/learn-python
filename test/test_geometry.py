import unittest
import geometry

class TestGeometry(unittest.TestCase):
    
    # PERSEGI
    ### Luas
    def test_luas_persegi(self):
        self.assertEqual(geometry.luas_persegi(2), 4)
        self.assertEqual(geometry.luas_persegi(0), 0)
        self.assertEqual(geometry.luas_persegi(-3), 9)  # Test with negative side length
    ### Keliling
    def test_keliling_persegi(self):
        self.assertEqual(geometry.keliling_persegi(2), 8)
        self.assertEqual(geometry.keliling_persegi(0), 0)
        self.assertEqual(geometry.keliling_persegi(3), 12)  # Test with negative side length
        
    # PERSEGI PANJANG
    ### Luas
    def test_luas_persegi_panjang(self):
        self.assertEqual(geometry.luas_persegi_panjang(2, 3), 6)
        self.assertEqual(geometry.luas_persegi_panjang(0, 5), 0)
        self.assertEqual(geometry.luas_persegi_panjang(4, 5), 20)
    ### Keliling
    def test_keliling_persegi_panjang(self):
        self.assertEqual(geometry.keliling_persegi_panjang(2, 3), 10)
        self.assertEqual(geometry.keliling_persegi_panjang(0, 5), 10)
        self.assertEqual(geometry.keliling_persegi_panjang(4, 5), 18)
    
    # LINGKARAN
    ### Luas
    def test_luas_lingkaran(self):
        self.assertAlmostEqual(geometry.luas_lingkaran(1), 3.14, places=2)
        self.assertAlmostEqual(geometry.luas_lingkaran(0), 0, places=2)
        self.assertAlmostEqual(geometry.luas_lingkaran(2), 12.57, places=2)
    ### Keliling
    def test_keliling_lingkaran(self):
        self.assertAlmostEqual(geometry.keliling_lingkaran(1), 6.28, places=2)
        self.assertAlmostEqual(geometry.keliling_lingkaran(0), 0, places=2)
        self.assertAlmostEqual(geometry.keliling_lingkaran(2), 12.57, places=2)

if __name__ == '__main__':
    unittest.main()
    