from django.urls import path
from document.views import document_views as views

urlpatterns = [
    path('documents/<int:document_id>/update/', views.document_update_view, name='document-update'),

    path('documents/<int:document_id>/delete/', views.document_delete_view, name='document-delete'),

    path('documents/<int:document_id>/share/', views.share_document_view, name='share-document'),

    path('documents/search/', views.document_search_view, name='document-search'),

    path('all_documents/', views.all_document_view, name='all-document'),

    path('single_document/', views.single_document_view, name='single-document'),

    path('document_upload/', views.document_upload_view, name='document-upload'),

    path('download/<int:document_id>/', views.document_download_view, name='document-download'),

    path('shared-documents/', views.shared_document_list_view, name='shared-document-list'),
]
