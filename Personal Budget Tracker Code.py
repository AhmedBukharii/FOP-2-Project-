import pandas as pd
import matplotlib.pyplot as plt


while True:
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        if monthly_budget <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

categories = []
amounts = []

print("\nEnter your expense details. Type 'done' to finish.")
while True:
    category = input("Enter category (or 'done' to finish): ")
    if category.lower() == 'done':
        break
    try:
        amount = float(input(f"Enter amount for {category}: "))
        if amount < 0:
            print("Amount cannot be negative. Please enter a positive value.")
            continue
        categories.append(category)
        amounts.append(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")


data = {'Category': categories, 'Amount': amounts}
df = pd.DataFrame(data)


total_expenses = df['Amount'].sum()
df['Percentage'] = (df['Amount'] / total_expenses) * 100


# Pie Chart
plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%', startangle=140)
plt.title('Expense Distribution')
plt.show()

# Bar Chart
plt.bar(df['Category'], df['Amount'], color='skyblue')
plt.title('Spending by Category')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.show()

# Display Summary
remaining_budget = monthly_budget - total_expenses

print("\nBudget Summary:")
print(df)
print(f"\nTotal Expenses: ${total_expenses:.2f}")
print(f"Monthly Budget: ${monthly_budget:.2f}")
if remaining_budget >= 0:
    print(f"Unused Budget (Savings): ${remaining_budget:.2f}")
else:
    print(f"Over Budget by: ${-remaining_budget:.2f}")
