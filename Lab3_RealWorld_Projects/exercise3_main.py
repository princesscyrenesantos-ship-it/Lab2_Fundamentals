import exercise3_telemetry as tm

LAST_NAME = "SANTOS"
SEED_NUM = 6
FAVORITE_ARTIST = "TWICE"

def monitor_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[MONITOR] Starting Pipeline Analysis for {LAST_NAME} ({FAVORITE_ARTIST})...")
        return func(*args, **kwargs)
    return wrapper

def recursive_anomaly_trace(val):
    if val <= 10:
        return [val]
    return [val] + recursive_anomaly_trace(val // 2)

@monitor_decorator
def run_pipeline():
    valid_count = 0
    invalid_count = 0
    valid_readings = []
    
    gen = tm.telemetry_generator(SEED_NUM, len(FAVORITE_ARTIST))
    for item in gen:
        try:
            tm.validate_telemetry(item)
            valid_readings.append(item)
            valid_count += 1
        except ValueError:
            invalid_count += 1
            
    curved = list(map(lambda x: x + SEED_NUM, valid_readings))
    max_val = max(curved) if curved else 0
    anomaly_history = recursive_anomaly_trace(max_val)
    trace_str = " -> ".join(map(str, anomaly_history))
    
    print("\n=== MONITORING PIPELINE SUMMARY ===")
    print(f"Operator: {LAST_NAME} | Tag: {FAVORITE_ARTIST}")
    print(f"Valid Readings: {valid_count} | Invalid Readings: {invalid_count}")
    print(f"Curved Stream: {curved}")
    print(f"Anomaly Recursive Trace: {trace_str}")
    print("===================================")

run_pipeline()

