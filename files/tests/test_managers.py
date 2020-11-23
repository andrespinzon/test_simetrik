import unittest

from config.extension import session
from files.models import Transaction
from files.managers import TransactionManager


class TestTransactionManager(unittest.TestCase):

    def setUp(self) -> None:
        transactions = TransactionManager.get_all()
        for transaction in transactions:
            session.delete(transaction)
            session.commit()
        self.transaction = Transaction(
            transaction_id='52fba4fa-3a01-4961-a809-e343dd4f9597',
            transaction_date='2020-06-01',
            transaction_amount=200000,
            client_id=1067,
            client_name='test 1'
        )
        session.add(self.transaction)
        session.commit()

    def test_get_all(self):
        transactions = TransactionManager.get_all()
        self.assertEqual(
            self.transaction.transaction_id,
            transactions[0].transaction_id
        )
        self.assertEqual(
            self.transaction.transaction_amount,
            transactions[0].transaction_amount
        )

    def test_get_by_transaction_id(self):
        transaction = TransactionManager.get_by_transaction_id(self.transaction.transaction_id)
        self.assertEqual(
            self.transaction.transaction_id,
            transaction.transaction_id
        )
        self.assertEqual(
            self.transaction.transaction_amount,
            transaction.transaction_amount
        )

