def transform(legacy_data):
    """Transforms legacy data into shiny new data."""
    scores = dict()

    for key, value in legacy_data.items():
        for char in value:
            scores[char.lower()] = key
    return scores
