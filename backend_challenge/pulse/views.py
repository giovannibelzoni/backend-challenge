from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError
from rest_framework import status, viewsets

from .serializers import PulseSerializer
from .renderers import CSVRenderer
from .parsers import CSVParser
from .models import Pulse


class PulseUploadView(APIView):
    serializer_class = PulseSerializer
    queryset = Pulse.objects.all()
    parser_classes = (CSVParser,)

    def post(self, request, format=None):

        # Store import errors in a list and return to client
        errors = []

        # Loop rows, creating Pulses or writing errors
        for index, data in enumerate(request.data):
            try:
                self.create(data)

            except ValidationError as ex:
                errors.extend(self.format_errors(index, ex))

        # Always return OK
        response = Response(status=status.HTTP_200_OK)

        # Some rows may have had errors, let the client know
        if errors:
            self.resource_name = 'errors'
            response.data = errors

        return response

    def create(self, data):
        """
        Performs the creation of Pulses from rows. Add failed rows to errors
        and return status report to client.

        """
        serializer = PulseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def format_errors(self, index, ex):
        """
        Generate hints on what went wrong with a particular row.

        """
        for field, message in ex.detail.items():
            yield {
                'code': ex.default_code,
                'status': str(ex.status_code),
                'detail': message[0],
                'source': {
                    'pointer': '/data/attributes/{}'.format(field),
                },
                'meta': {
                    'line_no': index + 2,
                },
            }


class PulseDownloadView(GenericAPIView):
    """
    Return a CSV response as an attachment.

    """
    serializer_class = PulseSerializer
    queryset = Pulse.objects.all()
    pagination_class = None
    renderer_classes = (CSVRenderer,)

    def get(self, request, *args, **kwargs):

        # Assume no filtering required, return all records
        serializer = self.get_serializer(self.get_queryset(), many=True)

        # Return as CSV content type
        response = Response(serializer.data, content_type='text/csv')

        # Return as attachment
        response['Content-Disposition'] = 'attachment; filename="pulses.csv"'

        return response


class PulseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing pulse instances.

    """
    serializer_class = PulseSerializer
    queryset = Pulse.objects.all()
