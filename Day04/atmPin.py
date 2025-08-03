atmpin=int(input("Set your ATM pin (e.g., 1234): "))
pin=int(input("Enter your ATM pin for Access: "))

if(pin==atmpin):
    print(f"Pin is Correct. Access Granted.")
else:
    print(f"Pin is Incorrect. Access Denied.")


