import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output", sep="\t", header=None, names=["Year", "PlayerCount"])
df["Year"] = df["Year"].astype(int)

plt.style.use("seaborn-v0_8-darkgrid")
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["PlayerCount"], marker="o", color="darkgreen", label="Players >20 PTS or >10 AST")
plt.title("High-Scoring or High-Assist Players Per Season")
plt.xlabel("Season")
plt.ylabel("Number of Players")
plt.xticks(df["Year"][::2], rotation=45)
plt.tight_layout()
plt.legend()
plt.grid(True)
plt.show()
