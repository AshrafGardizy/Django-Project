from django.urls import path
from blog import views
app_name = "blog"
urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('blog_create',views.form_create),
    path('detail/<int:my_id>',views.detail_view,name='detail'),
    path('archive',views.arch_blog_list),
    path('delete/<int:my_id>',views.delete_post)

]