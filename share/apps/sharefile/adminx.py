# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-15 23:47'

from .models import FileUsedfor
import xadmin

class FileUsedforAdmin(object):
    list_display = ['Usedfor', 'add_time']

    search_fields = ['Usedfor', 'add_time']

    list_filter = ['Usedfor', 'add_time']


xadmin.site.register(FileUsedfor, FileUsedforAdmin)