import django_filters

from .models import document, ArchivedDocument


class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = document
        fields = ['index', 'title', 'author', 'uploader_name', 'expiry_date', 'is_lock', 'is_private']


class ArchiveFilter(django_filters.FilterSet):
    class Meta:
        model = ArchivedDocument
        fields = ['title', 'index', 'author', 'uploader_name', 'archive_date']
