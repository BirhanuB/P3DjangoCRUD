from email.policy import default
from courselist.viewsets import CourseViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', CourseViewset)
