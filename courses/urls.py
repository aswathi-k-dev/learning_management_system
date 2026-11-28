from django.urls import path

from courses.views import CourseListView,CourseCreateView,CourseRetrieveUpdateDeleteView

urlpatterns = {
    path("list/",CourseListView.as_view()),
    path("create/",CourseCreateView.as_view()),
    path("retrieve/<int:pk>",CourseRetrieveUpdateDeleteView.as_view()),
    path("update/<int:pk>",CourseRetrieveUpdateDeleteView.as_view()),
    path("delete/<int:pk>",CourseRetrieveUpdateDeleteView.as_view())

}