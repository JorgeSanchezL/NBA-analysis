import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output", sep="\t", header=None, names=["Year", "Stats"])

df_stats = df["Stats"].str.split(",", expand=True).astype(float)
df_stats.columns = ["3P", "3PA", "MP", "3P%"]
df = df.drop(columns=["Stats"]).join(df_stats)
df["Year"] = df["Year"].astype(int)

plt.style.use("seaborn-v0_8-darkgrid")

# Graph 1
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["3P%"], marker="o", color="crimson", label="3P%")
plt.title("Average 3-Point Percentage Over the Years")
plt.xlabel("Season")
plt.ylabel("3P%")
plt.xticks(df["Year"], rotation=45)
plt.tight_layout()
plt.legend()
plt.grid(True)
plt.show()

# Graph 2
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["3P"], marker="o", label="3P Made")
plt.plot(df["Year"], df["3PA"], marker="o", label="3P Attempted")
plt.title("3P Made vs Attempted Over the Years")
plt.xlabel("Season")
plt.ylabel("Average per Player")
plt.xticks(df["Year"], rotation=45)
plt.tight_layout()
plt.legend()
plt.grid(True)
plt.show()

# Graph 3
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["MP"], marker="o", color="teal", label="Minutes Played")
plt.title("Average Minutes Played Over the Years")
plt.xlabel("Season")
plt.ylabel("Minutes")
plt.xticks(df["Year"], rotation=45)
plt.tight_layout()
plt.legend()
plt.grid(True)
plt.show()
