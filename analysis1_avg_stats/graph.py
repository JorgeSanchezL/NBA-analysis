import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output", sep="\t", header=None, names=["Year", "Stats"])
df_stats = df["Stats"].str.split(",", expand=True).astype(float)
df_stats.columns = ["PTS", "AST", "TRB"]
df = df.drop(columns=["Stats"]).join(df_stats)
df["Year"] = df["Year"].astype(int)

plt.style.use("seaborn-v0_8-darkgrid")
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["PTS"], marker="o", label="Points")
plt.plot(df["Year"], df["AST"], marker="o", label="Assists")
plt.plot(df["Year"], df["TRB"], marker="o", label="Rebounds")
plt.title("Average Total Player Stats Per Season")
plt.xlabel("Season")
plt.ylabel("Average Total")
plt.xticks(df["Year"][::2], rotation=45)
plt.tight_layout()
plt.legend()
plt.grid(True)
plt.show()
