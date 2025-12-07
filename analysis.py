import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
satisfaction_scores = [1.13, 1.15, 6.31, 6.01]
average_satisfaction = np.mean(satisfaction_scores)
industry_target = 4.5

# Print the average satisfaction score to verify the value
print(f"Average Patient Satisfaction Score: {average_satisfaction:.2f}")

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(quarters, satisfaction_scores, color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

# Add the industry target line
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target})')

# Add labels and title
plt.xlabel('2024 Quarters')
plt.ylabel('Patient Satisfaction Score')
plt.title('Patient Satisfaction Scores vs. Industry Target')
plt.ylim(0, 7)
plt.legend()

# Add data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom', ha='center') # va: vertical alignment

# Save the chart to a file
plt.savefig('patient_satisfaction_trend.png')

print("Chart saved as patient_satisfaction_trend.png")
