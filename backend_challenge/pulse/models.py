from django.db import models

from .validators import (
    rambi_rate_min, rambi_rate_max, polar_angle_min, polar_angle_max)


class Pulse(models.Model):
    """
    An over-simplified model of a pulse.

    "You know, I have one simple request. And that is to have sharks with
    frickin' laser beams attached to their heads! Now evidently my cycloptic
    colleague informs me that that cannot be done. Ah, would you remind me
    what I pay you people for, honestly? Throw me a bone here! What do we have?"

    - Dr. Evil

    """
    PRIMITAVE = 'primitive'
    CORPSE = 'corpse'
    GAUSSIAN = 'gaussian'
    CINSK = 'cinsk'
    CINBB = 'cinbb'

    TYPE_CHOICES = (
        (PRIMITAVE, 'Primitive'),
        (CORPSE, 'CORPSE'),
        (GAUSSIAN, 'Gaussian'),
        (CINBB, 'CinBB'),
        (CINSK, 'CinSK'),
    )

    name = models.CharField(
        help_text="The name of the pulse (e.g. 'My Awesome Pulse')",
        max_length=300)

    type = models.CharField(
        help_text="The type of pulse. Valid pulse types are: primitive, corpse,"
                  "gaussian, cinbb, cinsk",
        max_length=50,
        choices=TYPE_CHOICES,
        default=PRIMITAVE)

    maximum_rabi_rate = models.FloatField(
        help_text="A floating-point number between 0 and 100",
        validators=[rambi_rate_min, rambi_rate_max],
        default=0)

    polar_angle = models.FloatField(
        help_text="A floating-point number between 0 and 1",
        validators=[polar_angle_min, polar_angle_max],
        default=0)

    class Meta:
        ordering = ['-id']

    class JSONAPIMeta:
        resource_name = 'pulse'

    def __str__(self):
        return "{0}".format(self.name)

    @property
    def fieldnames(self):
        return [x.name for x in self._meta.fields]