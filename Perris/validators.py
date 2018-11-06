from django.core.exceptions import ValidationError

def run_validation(value):
    if not "-":
        raise ValidationError('ingrese rut con guion')
]
