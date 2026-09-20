def telemetry_generator(seed, artist_len):
    base = seed * 10
    raw_data = [base + 6, base + 11, 12, "INVALID", 84, -5, 95, 60]
    for val in raw_data:
        yield val

def validate_telemetry(val):
    if not isinstance(val, (int, float)) or val < 0:
        raise ValueError(f"Bad Telemetry: {val}")
    return True

