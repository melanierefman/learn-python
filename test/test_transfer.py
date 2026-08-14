# Unit test dan Integration test untuk fungsi transfer

import unittest
import transfer

class TestTransfer(unittest.TestCase):
    def setUp(self):
        self.account_repository = transfer.AccountRepository()
        self.transfer_service = transfer.TransferService(self.account_repository)

        # Menyimpan akun awal
        self.account_repository.save("A", 100)
        self.account_repository.save("B", 50)

    def test_successful_transfer(self):
        result = self.transfer_service.transfer("A", "B", 30)
        self.assertEqual(result, "Transfer successful")
        self.assertEqual(self.account_repository.find_balance("A"), 70)
        self.assertEqual(self.account_repository.find_balance("B"), 110)  # Bug: seharusnya 80
    
    def test_insufficient_balance(self):
        result = self.transfer_service.transfer("A", "B", 200)
        self.assertEqual(result, "Insufficient balance")
        self.assertEqual(self.account_repository.find_balance("A"), 100)
        self.assertEqual(self.account_repository.find_balance("B"), 50)

    def test_invalid_amount(self):
        result = self.transfer_service.transfer("A", "B", -10)
        self.assertEqual(result, "Invalid amount")
        self.assertEqual(self.account_repository.find_balance("A"), 100)
        self.assertEqual(self.account_repository.find_balance("B"), 50)

    def test_sender_not_found(self):
        result = self.transfer_service.transfer("C", "B", 10)
        self.assertEqual(result, "Sender not found")
        self.assertIsNone(self.account_repository.find_balance("C"))
        self.assertEqual(self.account_repository.find_balance("B"), 50)

    def test_receiver_not_found(self):
        result = self.transfer_service.transfer("A", "D", 10)
        self.assertEqual(result, "Receiver not found")
        self.assertEqual(self.account_repository.find_balance("A"), 100)
        self.assertIsNone(self.account_repository.find_balance("D"))
        
if __name__ == '__main__':
    unittest.main()