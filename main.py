import os
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('data/ai_job_dataset.csv')

print(df['required_skills'].head())

# Extract and count skills
def extract_skills(series):
    all_skills = []
    for skills in series.dropna():
        all_skills.extend([s.strip().lower() for s in skills.split(",")])
    return all_skills

skills = extract_skills(df['required_skills'])
skill_counts = Counter(skills)

# Correct column naming
skill_df = pd.DataFrame(list(skill_counts.items()), columns=['skills', 'count'])
skill_df = skill_df.sort_values(by='count', ascending=False)

# Save output
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)
skill_df.to_csv(os.path.join(output_dir, 'skill_counts.csv'), index=False)
print("Skills counts saved to output/skill_counts.csv")

# Plot top 20
skill_df.head(20).plot(kind='bar', x='skills', y='count', figsize=(12,6), title='Top 20 AI Skills in Demand')
plt.tight_layout()

# Display the chart
plt.show()