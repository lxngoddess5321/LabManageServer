"""lab_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import add, change, add_bot, change_bot, equipment_using_record, trial_record, ear_records, add_comment, \
    delete_records

urlpatterns = [
    path('add/', add),
    path('change/', change),
    path('addbot/', add_bot),
    path('changebot/', change_bot),
    path('addcomment/', add_comment),
    path('findrecords/', equipment_using_record),
    path('trialrecords/', trial_record),
    path('earrecords/', ear_records),
    path('deleterecords/', delete_records),
]
