from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api.models import TestModels
from api.serializer import TestSerializer


class TestPostView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestGetView(APIView):
    def get(self, request):
        test = TestModels.objects.all()
        serializer = TestSerializer(
            test,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class TestListView(TemplateView):
    template_name = 'test_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = TestModels.objects.all()
        return context
