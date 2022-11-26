from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    EmailField,
    DecimalField,
    URLField,
    DateTimeField,
    FloatField,
    SlugField,
    TextField,
    TimeField,
    IntegerField,
    PositiveSmallIntegerField,
    PositiveBigIntegerField,
    ForeignKey,
    ManyToManyField,
    OneToOneField,
    GenericIPAddressField,
    Sum
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField

class User(AbstractUser):
    """
    Default custom user model for coraka.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class Subscribe(TimeStampedModel):
    email = EmailField(blank=False)

    def __str__(self):
        return self.email
    
class Consent(TimeStampedModel):
    ipAddress = CharField(max_length=255, blank=True)
    consented = BooleanField(default=False)

    def __str__(self):
        return self.ipAddress

    class Meta:
        managed = True
        verbose_name = "Consent"
        verbose_name_plural = "Consents"
        ordering = ["-modified"]

class Porttfolio(TimeStampedModel):
    logo = URLField(blank=False)
    name = CharField(max_length=255)
    service = CharField(max_length=255)
    sector = CharField(max_length=255)
    website = URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
        ordering = ["-modified"]


class Career(TimeStampedModel):
    logo = URLField(blank=False, default="https://panteracapital.com/wp-content/uploads/2022/10/Logo-2.png")
    title = CharField(max_length=500)
    description = HTMLField()
    requirements = HTMLField()
    salary = DecimalField(default=0.00, decimal_places=2, max_digits=20)
    application_email = EmailField(blank=False)

    active = BooleanField(default=True)

    def __str__(self) -> str:
        return self.title.title()

    class Meta:
        managed = True
        verbose_name = "Careers"
        verbose_name_plural = "Careers"
        ordering = ["-modified"]

