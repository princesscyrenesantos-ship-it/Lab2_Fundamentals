# Exercise 2: Recursive Fault Trace
LAST_NAME = "SANTOS"
SEED_NUM = 6
FAVORITE_ARTIST = "TWICE"

call_count = 0

def trace_fault(code):
    global call_count
    call_count += 1
    print(f"[TRACE] Call {call_count}: Processing Fault Code {code}")
    
    if code <= 10:
        return [code]
    
    return [code] + trace_fault(code // 2)

fault_code = SEED_NUM * 100 + len(LAST_NAME) * 10 + len(FAVORITE_ARTIST)
trace_history = trace_fault(fault_code)

trace_str = " -> ".join(map(str, trace_history))

print("\n=== RECURSIVE FAULT TRACE REPORT ===")
print(f"Operator: {LAST_NAME} | Code Origin: {FAVORITE_ARTIST}")
print(f"Initial Fault Code: {fault_code}")
print(f"Recursive Trace: {trace_str}")
print(f"Total Recursive Calls: {call_count}")
print("====================================")

