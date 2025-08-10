from django.urls import path, include

urlpatterns = [
    path('video/', include('VideoProcessing.dispatchers.dispatcher.video_dispatcher')),
    path('video/upload/', include('VideoProcessing.dispatchers.dispatcher.video_dispatcher')),
    path('user/', include('VideoProcessing.dispatchers.dispatcher.user_dispatcher')),
    path('sign_up/', include('VideoProcessing.dispatchers.dispatcher.signup_dispatcher')),
    path('login/', include('VideoProcessing.dispatchers.dispatcher.login_dispatcher')),
]