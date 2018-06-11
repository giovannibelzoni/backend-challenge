import io
import csv

from django.conf import settings
from rest_framework.parsers import BaseParser
from rest_framework.exceptions import ParseError

from .utils import header_to_field
from .models import Pulse


class CSVParser(BaseParser):
    """
    Parse CSV upload and return dictionary of field name, value pairs.

    """
    media_type = 'text/csv'

    def parse(self, stream, media_type=None, parser_context=None):

        # Read request body into string
        stream_str = stream.read().decode(settings.DEFAULT_CHARSET)

        # Use DictReader to preserve header names
        reader = csv.DictReader(io.StringIO(stream_str))

        # Convert csv headers to Pulse field names
        reader.fieldnames = [header_to_field(x) for x in reader.fieldnames]

        # Field names must match Pulse model, raise 400 if not
        if not set(reader.fieldnames).issubset(set(Pulse().fieldnames)):
            raise ParseError(
                detail="An invalid header or field title was found.",
                code='invalid_header')

        # Return generator for rows
        for x in reader:
            yield x


