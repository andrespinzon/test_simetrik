from django.urls import path
from files.views import upload_file_view, get_transactions, detail_transaction

file_urlpatterns = [
    path('upload-file/', upload_file_view),
]

transaction_urlpatterns = [
    path('', get_transactions),
    path('<str:transaction_id>/', detail_transaction),
]
