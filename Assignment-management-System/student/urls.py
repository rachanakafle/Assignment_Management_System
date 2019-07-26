from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from student.views import base,signin, signout, signup, create_assignment, assignment_submission, \
    submitted, delete_assignment, edit_assignment,Assignmentsubmit, student_submitted,submit_button

app_name = "student"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', base, name="base"),
    path('', signin, name="signin"),
    path('signout/', signout, name="signout"),
    path('signup/', signup, name="signup"),
    path('teachers/', create_assignment, name="teachers"),
    path('students/', assignment_submission, name="students"),
    path('submitted/(?P<id>[0-9]+)/$', submitted, name="submitted"),
    path('submitted/', student_submitted, name="student_submitted"),
    path('detail/<pk>/', Assignmentsubmit.as_view(),name="assignment-detail"),
    path('delete/(?P<id>\d+)/$', delete_assignment, name='delete_assignment'),
    path('edit/(?P<id>[0-9]+)/$', edit_assignment, name='edit_assignment'),
    path('submit/(?P<id>[0-9]+)/$', submit_button, name='submit_button'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]