from django.urls import path

import main.views as views

app_name='main'
urlpatterns = [
	# Home page
	path('',views.index,name='index'),
	path('history',views.history)
]
