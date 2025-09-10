import sys
import math

def main():
    emails = [line.strip() for line in sys.stdin if line.strip()]
    
    if not emails:
        print("No input received!")
        return
    
    # Convert emails to decimal values
    decimals = [sum(ord(c) for c in email) for email in emails]
    print("Decimal values:", decimals)
    
    # Hash functions
    hash1 = lambda x: (4*x + 5) % 13
    hash2 = lambda x: (x // 3) % 5
    
    # Count trailing zeros in binary
    def count_zeros(n):
        return len(bin(n)) - len(bin(n).rstrip('0')) if n > 0 else 0
    
    # Find max trailing zeros for each hash function
    R1 = max(count_zeros(hash1(d)) for d in decimals)
    R2 = max(count_zeros(hash2(d)) for d in decimals)
    
    # Results
    actual = len(set(emails))
    est1, est2 = 2**R1, 2**R2
    
    print(f"Total emails: {len(emails)}")
    print(f"Actual unique: {actual}")
    print(f"Estimated (func1): {est1} (R={R1})")
    print(f"Estimated (func2): {est2} (R={R2})")
    
    # Error rates
    error = lambda r, m: 1 - math.exp(-m * (2**(-r)))
    err1, err2 = error(R1, len(emails)), error(R2, len(emails))
    
    print(f"Error rate 1: {err1:.3f}")
    print(f"Error rate 2: {err2:.3f}")
    print("Hash function 1 is better" if err1 < err2 else "Hash function 2 is better")

if __name__ == "__main__":
    main()