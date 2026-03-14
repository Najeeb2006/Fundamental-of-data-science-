import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('q15_clinical.csv')
control = df[df['group'] == 'control']['score'].values
treatment = df[df['group'] == 'treatment']['score'].values

# t-test
t_stat, p_value = stats.ttest_ind(control, treatment)

print(f"Control group   - Mean: {np.mean(control):.2f}, Std: {np.std(control):.2f}")
print(f"Treatment group - Mean: {np.mean(treatment):.2f}, Std: {np.std(treatment):.2f}")
print(f"\nt-statistic: {t_stat:.4f}")
print(f"p-value:     {p_value:.4f}")

if p_value < 0.05:
    print("Result: Statistically significant (p < 0.05) - treatment has effect!")
else:
    print("Result: Not statistically significant (p >= 0.05)")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Box plot
axes[0].boxplot([control, treatment], labels=['Control', 'Treatment'])
axes[0].set_title('Score Distribution by Group')
axes[0].set_ylabel('Score')

# Bar chart with p-value annotation
axes[1].bar(['Control', 'Treatment'], [np.mean(control), np.mean(treatment)],
            color=['gray', 'blue'], yerr=[np.std(control), np.std(treatment)],
            capsize=5, edgecolor='black')
axes[1].set_title(f'Mean Scores (p-value = {p_value:.4f})')
axes[1].set_ylabel('Mean Score')

plt.tight_layout()
plt.savefig('q15_hypothesis.png')
plt.show()
print("Plot saved as q15_hypothesis.png")
