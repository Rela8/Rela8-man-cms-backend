from rest_framework import generics, permissions
from publications.models import Publication, PublicationType
from publications.serializers import PublicationSerializer, PublicationSerializerPaid, PublicationTypeSerializer
from rest_framework.parsers import FormParser
from utils import custom_parsers, custom_response

# Create your views here.


class PublicationView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = PublicationSerializer
    parser_classes = (custom_parsers.NestedMultipartParser, FormParser,)

    def perform_create(self, serializer):
        return serializer.save(writer=self.request.user)

    def get_queryset(self):
        queryset = Publication.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return custom_response.Success_response(data=serializer.data, msg="publications")


class PublicationDatialView(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (custom_parsers.NestedMultipartParser, FormParser,)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated,]
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset


class PublicationTypeView(generics.ListCreateAPIView):
    serializer_class = PublicationTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PublicationType.objects.all()

    def perform_create(self, serializer):
        return serializer.save(writer=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return custom_response.Success_response(msg="all publication types", data=serializer.data)


class PublicationTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublicationTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return PublicationType.objects.all()

# PUBLIC CLASS HERE


class PublicationViewPublic(generics.ListAPIView):
    serializer_class = PublicationSerializer

    def get_queryset(self):
        queryset = Publication.objects.filter(is_paid=False)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return custom_response.Success_response(data=serializer.data, msg="free publications")


class PublicationViewPaidPublic(generics.ListAPIView):
    serializer_class = PublicationSerializerPaid

    def get_queryset(self):
        queryset = Publication.objects.filter(is_paid=True)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return custom_response.Success_response(data=serializer.data, msg="paid publications")


class PublicationTypePublicView(generics.ListAPIView):
    serializer_class = PublicationTypeSerializer

    def get_queryset(self):
        return PublicationType.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return custom_response.Success_response(data=serializer.data, msg="publication type")
