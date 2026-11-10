
import hashlib

# Customer information
order_info = "Product: Laptop"
payment_info = "Card Payment: 50000"

# Generate hashes
order_hash = hashlib.sha256(
    order_info.encode()
).hexdigest()

payment_hash = hashlib.sha256(
    payment_info.encode()
).hexdigest()

# Generate simplified dual signature
dual_signature = hashlib.sha256(
    (order_hash + payment_hash).encode()
).hexdigest()

print("Order Information:", order_info)
print("Payment Information:", payment_info)

print("\nOrder Hash:", order_hash)
print("Payment Hash:", payment_hash)

print("\nDual Signature:", dual_signature)

# Verification process

# Merchant verifies order information
verify_order = hashlib.sha256(
    order_info.encode()
).hexdigest()


# Payment gateway verifies payment information
verify_payment = hashlib.sha256(
    payment_info.encode()
).hexdigest()



# Verify dual signature
verify_signature = hashlib.sha256(
    (verify_order + verify_payment).encode()
).hexdigest()


# Final transaction condition
if (verify_order == order_hash and
    verify_payment == payment_hash and
    verify_signature == dual_signature):

    print("\nTransaction Completed Successfully")
else:
    print("\nTransaction Rejected")
