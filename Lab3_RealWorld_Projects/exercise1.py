# Exercise 1: Equipment Diagnostic System
LAST_NAME = "SANTOS"
SEED_NUM = 6
FAVORITE_ARTIST = "TWICE"

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing diagnostic scan for {LAST_NAME} ({FAVORITE_ARTIST})...")
        return func(*args, **kwargs)
    return wrapper

def validate_readings(readings):
    for r in readings:
        if not isinstance(r, (int, float)) or r < 0:
            raise ValueError(f"Invalid reading detected: {r}")
    return True

def calculate_average(readings):
    return sum(readings) / len(readings)

def classify_status(avg):
    return "NORMAL OPERATIONAL STATUS" if avg >= 75 else "ATTENTION REQUIRED"

@logger
def process_diagnostics(readings):
    try:
        validate_readings(readings)
        avg = calculate_average(readings)
        status = classify_status(avg)
        return avg, status
    except ValueError as e:
        return None, f"ERROR: {e}"

r1 = float(SEED_NUM * 10 + len(LAST_NAME) + len(FAVORITE_ARTIST))
r2 = 82.5
readings = [r1, r2]

avg, status = process_diagnostics(readings)

print("=== EQUIPMENT DIAGNOSTIC REPORT ===")
print(f"Operator: {LAST_NAME} | Artist Key: {FAVORITE_ARTIST}")
print(f"Generated Readings: {readings}")
print(f"Average Reading: {avg}")
print(f"Diagnostic Status: {status}")
print("===================================")

