from typing import Dict

from sqlalchemy import or_, desc, asc

from config.extension import session
from common.validations import validate_allowed_fields_filters
from files.models import Transaction


class TransactionManager:

    @staticmethod
    def get_all():
        return session.query(Transaction).all()

    @staticmethod
    def get_by_transaction_id(transaction_id: str):
        return session.query(Transaction).filter(Transaction.transaction_id == transaction_id).one_or_none()

    @staticmethod
    def get_all_by_params(params: Dict):

        transaction_id = params.get('transaction_id', None)
        transaction_date = params.get('transaction_date', None)
        transaction_amount = params.get('transaction_amount', None)
        client_id = params.get('client_id', None)
        client_name = params.get('client_name', None)
        page = params.get('page', None)
        per_page = params.get('per_page', None)
        order_by = params.get('order_by', None)

        query = session.query(Transaction)
        query_params = []
        if transaction_id is not None:
            transaction_id = [transaction_id.strip() for transaction_id in transaction_id.split(',')]
            query_params.append(Transaction.transaction_id.in_(transaction_id))
        if transaction_date is not None:
            transaction_date = [transaction_date.strip() for transaction_date in transaction_date.split(',')]
            query_params.append(Transaction.transaction_date.in_(transaction_date))
        if transaction_amount is not None:
            transaction_amount = [transaction_amount.strip() for transaction_amount in transaction_amount.split(',')]
            query_params.append(Transaction.transaction_amount.in_(transaction_amount))
        if client_id is not None:
            client_id = [client_id.strip() for client_id in client_id.split(',')]
            query_params.append(Transaction.client_id.in_(client_id))
        if client_name is not None:
            client_name = [client_name.strip() for client_name in client_name.split(',')]
            query_params.append(Transaction.client_name.in_(client_name))

        if query_params:
            query = query.filter(or_(*query_params))
        if order_by is not None:
            validate_allowed_fields_filters(
                field=order_by,
                allowed_field_order={
                    'transaction_id', 'transaction_date', 'transaction_amount', 'client_id', 'client_name',
                    '-transaction_id', '-transaction_date', '-transaction_amount', '-client_id', '-client_name'
                }
            )

            order, is_asc_desc = (order_by, True) if '-' not in order_by else (order_by.replace('-', ''), False)
            if is_asc_desc:
                order = asc(order)
            else:
                order = desc(order)

            query = query.order_by(order)

        if page is not None:
            query = query.offset(int(page) - 1)
        if per_page is not None:
            query = query.limit(per_page)

        return query.all()
