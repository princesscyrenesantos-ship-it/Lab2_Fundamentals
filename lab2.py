# LAB 2 - FULL EXECUTABLE SCRIPT

# [CELL 1] CONFIGURATION
ENGINEER = "SANTOS"
STUDENT_ID = "TUPM-26-1866"
SEED_NUM = int(STUDENT_ID[-1])
print(f"System Initialized for : {ENGINEER}")
print(f"Algorithmic Seed Value: {SEED_NUM}\n")

# [CELL 2] ARCHITECTURE TEST
actual = 0.1 + 0.2
print(f"Python stores: {actual}")
if actual == 0.3:
    print("Result: Perfect Match\n")
else:
    print("Result: PRECISION ERROR (Binary Artifact)\n")

# [CELL 3] ASCII INSPECTION
first_letter = ENGINEER[0]
byte_val = ord(first_letter)
print(f"Character: {first_letter}")
print(f"ASCII Value: {byte_val}")
print(f"Next in Sequence: {chr(byte_val + 1)}\n")

# [CELL 4] SANITIZATION
raw_in = input("Enter Name (add messy spaces): ")
clean_in = raw_in.strip().upper()
print(f"Original: '{raw_in}' | Cleaned: '{clean_in}'\n")

# [CELL 5] DATA EXISTENCE
user_input = input("Press Enter (leave empty) or type data: ")
if user_input:
    print(f"Data Detected: {user_input}\n")
else:
    print("ALERT: No data stream detected.\n")

# [CELL 6] SLICING & PARSING
campus = STUDENT_ID[0:4]
unique_id = STUDENT_ID[8:]
tokens = STUDENT_ID.split("-")
print(f"Campus Code: {campus}")
print(f"Unique Sequence: {unique_id}")
print(f"Token List: {tokens}\n")

# [CELL 7] MODULO OPERATOR
if SEED_NUM % 2 == 0:
    priority = "LOW (Even Seed)"
else:
    priority = "HIGH (Odd Seed)"
print(f"System Priority: {priority}\n")

# [CELL 8] DYNAMIC LIMITS
limit = (SEED_NUM * 10) + 20
print(f"--- SAFETY LIMIT: {limit} ---")
val = int(input("Enter Sensor Reading: "))
if val > limit:
    print("ALERT: Over Limit\n")
elif val < 5:
    print("ALERT: Low Signal\n")
else:
    print("STATUS: Nominal\n")

# [CELL 9] ROBUST INPUT
try:
    voltage = int(input("Enter Voltage (Numeric): "))
    print(f"Voltage Captured: {voltage} V\n")
except ValueError:
    print("SYSTEM ERROR: Input must be numeric. Resetting to 0.")
    voltage = 0
    print(f"System continues... Current Voltage: {voltage} V\n")

# [CELL 10] LOGIC GATES
has_power = False
if has_power and (10 / 0 == 0):
    print("System On\n")
else:
    print("System Off (Short-Circuit Triggered)\n")

# [CELL 11] FOR LOOP
loops = SEED_NUM + 3
print(f"--- RUNNING {loops} CYCLES ---")
for i in range(1, loops + 1):
    print(f"Cycle {i}/{loops} Complete")
print()

# [CELL 12] NESTED LOOPS
rows = int(tokens[2][0])
cols = int(tokens[2][-1])
print(f"Generating {rows}x{cols} Matrix:")
for r in range(rows):
    for c in range(cols):
        print("#", end=" ")
    print()
print()

# [CELL 13] INPUT VALIDATION
while True:
    pwd = input("Type 'ADMIN' to exit: ")
    if pwd == "ADMIN":
        print("Unlocked.\n")
        break
    else:
        print("Access Denied.\n")

# [CELL 14] FORENSIC HASH CALCULATION
A = byte_val
B = SEED_NUM
C = loops
verification_hash = (A * B) - C
print(f"User: {ENGINEER}")
print(f"Forensic Signature: {verification_hash}")