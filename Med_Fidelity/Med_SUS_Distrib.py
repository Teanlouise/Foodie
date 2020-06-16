from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

# Get converted data
results_df = pd.read_csv(
    'F:/TEAN/Portfolio/Foodie/Med_Fidelity/Med_SUS_Scores.csv', index_col=0)

# 4 - Get distribution
distrib_df = results_df.transpose()

plt.figure(figsize=(10, 4))
sns.boxplot(data=distrib_df)
plt.ylabel('Converted Responses (1-5)')
plt.title('SUS Distribution')
plt.savefig('Med_Fidelity/Med_SUS_distrib.png')