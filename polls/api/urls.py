from rest_framework.routers import DefaultRouter

from polls.api.views import AnswerViewSet, QuestionViewSet, TestViewSet, MarkPollViewSet

router = DefaultRouter()

router.register(r"answer", AnswerViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"test", TestViewSet)
router.register(r"mark", MarkPollViewSet)


urlpatterns = router.urls