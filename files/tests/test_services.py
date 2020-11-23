from django.test import TestCase

from config.extension import session, Base, engine
from files.services import TransactionService
from files.models import Transaction
from files.managers import TransactionManager


class TestTransactionService(TestCase):

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

    def test_get_detail_transaction(self) -> None:
        transaction = TransactionService.get_detail_transaction(self.transaction.transaction_id)
        self.assertEqual(
            self.transaction.transaction_id,
            transaction['transaction_id']
        )

    def test_get_all_transaction(self) -> None:
        service = TransactionService()
        transactions = service.get_transactions(params={})
        self.assertEqual(
            self.transaction.transaction_id,
            transactions[0]['transaction_id']
        )
        self.assertEqual(
            self.transaction.transaction_amount,
            transactions[0]['transaction_amount']
        )
