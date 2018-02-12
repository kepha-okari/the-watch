from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name='hoodNews'),
    url(r'^new/hood/',views.create_hood, name='newHood'),
    url(r'^all/hoods/',views.view_neighborhoods, name='allHoods'),
    url(r'^neighborhood/(\d+)',views.hood_details, name='pickHood'),
    url(r'^new/post/',views.post_message, name='message'),
    url(r'^new/business/',views.create_business, name='newBusiness'),
    url(r'^business/(\d+)',views.business_details, name='business'),
    url(r'^create/profile/', views.create_profile, name='createProfile'),
    url(r'^follow/(\d+)', views.follow, name='follow'),
    url(r'^unfollow/(\d+)', views.unfollow, name='unfollow'),
    # url(r'^other/profile/(\d+)',views.other_profile, name='otherProfile'),
    # url(r'^post/',views.new_post, name='postImage'),
    # url(r'^manage/(\d+)',views.manage_image, name='manageImage'),
    # url(r'^comment/(\d+)', views.new_comment, name='Comment'),
    # url(r'^single/image/(\d+)', views.single_image, name='singleImage'),
    # url(r'^follow/(\d+)', views.follow, name="follow"),
    # url(r'^delete/post/(\d+)', views.delete_post, name="removePost"),
    # url(r'^unfollow/(\d+)', views.unfollow, name="unfollow"),
    # url(r'^like/(\d+)', views.like, name="like"),
    # url(r'^update/profile/', views.create_profile, name="createProfile"),
    # url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

]
