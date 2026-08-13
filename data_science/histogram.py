import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

sns.set_style("whitegrid")

# Load the example diamonds dataset
diamonds = sns.load_dataset("diamonds")

# -- Histogram
f, ax = plt.subplots(figsize=(7, 5))
sns.despine(f)

sns.histplot(
    diamonds,
    x="price", hue="cut",
    multiple="stack",
    palette="light:m_r",
    edgecolor=".3",
    linewidth=.5,
    log_scale=True,
)
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.set_xticks([500, 1000, 2000, 5000, 10000])
plt.savefig("histogram.png", dpi=300)