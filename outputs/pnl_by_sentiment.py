import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.boxplot(x="sentiment", y="Closed PnL", data=merged)
plt.title("PnL by Market Sentiment")
plt.savefig("outputs/pnl_by_sentiment.png")
plt.show()
