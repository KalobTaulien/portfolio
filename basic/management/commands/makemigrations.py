# app/management/commands/makemigrations.py
"""
Override of Django makemigrations.
This triggers the __init__ that patches models.Field.
"""
from django.core.management.commands.makemigrations import Command  # noqa
