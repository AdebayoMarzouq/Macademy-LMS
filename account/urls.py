from django.urls import path
from .views import SignUpView, ProfileEditView

app_name = 'account'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit-profile/<int:pk>', ProfileEditView.as_view(), name='profile_edit')
]
