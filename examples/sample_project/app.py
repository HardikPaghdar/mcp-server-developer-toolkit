def normalize_email(value):
    value=value.strip().lower()
    if '@' not in value: raise ValueError('Email must contain @')
    return value
