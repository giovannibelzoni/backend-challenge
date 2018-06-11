import io
import csv

from rest_framework.renderers import BaseRenderer


class CSVRenderer(BaseRenderer):
    """
    CSV Renderer for Pulses.

    """
    media_type = 'text/csv'
    format = 'csv'

    def render(self, data, media_type=None, renderer_context=None):

        # Write to in-memory buffer. Perhas a better approach would be a
        # streaming response for larger data sets, but for the sake of
        # time and simplicity...
        buffer = io.StringIO()

        writer = csv.writer(buffer)

        # Write the values only. OrderedDict handles field order
        for row in data:
            writer.writerow(row.values())

        return buffer.getvalue()