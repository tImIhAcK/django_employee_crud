# Generated by Django 4.1.1 on 2022-09-14 11:02

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("name", models.CharField(max_length=100, verbose_name="fullname")),
                ("email", models.EmailField(max_length=254)),
                (
                    "contact",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("", "Select gender"), ("M", "Male"), ("F", "Female")],
                        max_length=1,
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("", "Select role"),
                            ("CEO", "Cheif Executive Officer"),
                            ("MD", "Managing Director"),
                            ("CTO", "Chief Technology Officer"),
                            ("CFO", "Chief Financial Officier"),
                            ("DAT", "Data Analyst Team Lead"),
                            ("SDA", "Senior Data Analyst"),
                            ("JNA", "Junior Data Analyst"),
                            ("WDT", "Web Developer Team Lead"),
                            ("SBD", "Senior Back-End Developer"),
                            ("JBD", "Junior Back-End Developer"),
                            ("SFD", "Senior Front-End Developer"),
                            ("JFD", "Junior Front-End Developer"),
                            ("INT", "Intern"),
                        ],
                        max_length=3,
                    ),
                ),
                ("salary", models.IntegerField(verbose_name="salary ($)")),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
            options={"ordering": ("id",),},
        ),
    ]
