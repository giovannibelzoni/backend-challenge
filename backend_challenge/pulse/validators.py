from django.core.validators import MinValueValidator, MaxValueValidator


# DRF refuses to pass error messages to validators. #wontfix

rambi_rate_min = MinValueValidator(
    float(0),
    message="Maximum Rambi Rate must be greater than 0")

rambi_rate_max = MaxValueValidator(
    float(100),
    message="Maximum Rambi Rate must be less than 100")

polar_angle_min = MinValueValidator(
    float(0),
    message="Polar Angle must be greater than 0")

polar_angle_max = MaxValueValidator(
    float(1),
    message="Polar Angle must be less than 1")
