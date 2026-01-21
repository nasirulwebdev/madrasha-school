# routine/context_processors.py
from .models import CLASS_CHOICES

def class_options(request):
    """
    Returns a list of all valid classes (Class 1 - Class 12)
    for the navbar dropdown.
    Ignores database to prevent messy entries.
    """
    classes = [c[0] for c in CLASS_CHOICES]  # ['Class 1', 'Class 2', ... 'Class 12']
    return {'class_options': classes}
