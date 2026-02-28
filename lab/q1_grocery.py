import pandas as pd

df = pd.read_csv('q1_grocery.csv')

discount_rate = 10  # 10%
tax_rate = 8        # 8%

df['subtotal'] = df['price'] * df['quantity']
total_before_discount = df['subtotal'].sum()
discount_amount = total_before_discount * (discount_rate / 100)
after_discount = total_before_discount - discount_amount
tax_amount = after_discount * (tax_rate / 100)
total_cost = after_discount + tax_amount

print(f"Items Summary:\n{df[['item','price','quantity','subtotal']].to_string(index=False)}")
print(f"\nSubtotal:          ${total_before_discount:.2f}")
print(f"Discount ({discount_rate}%):    -${discount_amount:.2f}")
print(f"After Discount:    ${after_discount:.2f}")
print(f"Tax ({tax_rate}%):          +${tax_amount:.2f}")
print(f"Total Cost:        ${total_cost:.2f}")
