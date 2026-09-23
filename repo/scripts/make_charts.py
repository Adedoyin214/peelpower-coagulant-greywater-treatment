import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

params = ["Electrical\nconductivity", "Turbidity\n(NTU)", "TDS\n(mg/L)", "TSS\n(mg/L)",
          "BOD\n(mg/L)", "COD\n(mg/L)", "Calcium\n(mg/L)", "Magnesium\n(mg/L)", "Sodium\n(mg/L)"]

cloth = {
    "Sisal Fibre": [28.1, 22.4, 14.7, 24.1, 46.3, 10.4, 56.4, 46.4, -7.3],
    "Banana Peel": [25.5, 21.7, 3.4, 17.8, 45.2, 8.1, 55.8, 23.3, -9.3],
    "Alum":        [29.4, 24.7, 15.0, 63.8, 78.6, 11.5, 61.3, 21.7, 0.4],
}
kitchen = {
    "Sisal Fibre": [36.1, 16.9, 31.9, 58.7, 59.3, 52.1, 59.4, 69.9, 48.8],
    "Banana Peel": [28.0, 7.1, 24.4, 67.0, 63.1, 31.7, 70.1, 69.3, -9.1],
    "Alum":        [42.3, 24.0, 34.7, 80.2, 74.6, 50.7, 61.1, 41.9, 34.0],
}

colors = {"Sisal Fibre": "#4C9A6E", "Banana Peel": "#E0A429", "Alum": "#5E7CE2"}

def grouped_bar(data, title, fname):
    n = len(params)
    x = np.arange(n)
    width = 0.26
    fig, ax = plt.subplots(figsize=(11, 5.5))
    for i, (label, vals) in enumerate(data.items()):
        ax.bar(x + (i-1)*width, vals, width, label=label, color=colors[label])
    ax.axhline(0, color="#444", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(params, fontsize=9)
    ax.set_ylabel("Removal efficiency (%)")
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.legend(frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(fname, dpi=160)
    plt.close(fig)

grouped_bar(cloth, "Removal Efficiency by Coagulant — Laundry (Clothes-Washing) Greywater", "figures/re_cloth.png")
grouped_bar(kitchen, "Removal Efficiency by Coagulant — Kitchen-Washing Greywater", "figures/re_kitchen.png")

# Average RE per coagulant across both water types (overview chart)
def avg_re(d):
    return {k: np.mean(v) for k, v in d.items()}

avg_cloth = avg_re(cloth)
avg_kitchen = avg_re(kitchen)
labels = list(avg_cloth.keys())
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(x - width/2, [avg_cloth[l] for l in labels], width, label="Laundry water", color="#4C9A6E")
ax.bar(x + width/2, [avg_kitchen[l] for l in labels], width, label="Kitchen water", color="#5E7CE2")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel("Average removal efficiency (%)")
ax.set_title("Overall Average Removal Efficiency by Coagulant", fontsize=13, fontweight="bold")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("figures/re_overall_average.png", dpi=160)
plt.close(fig)

print("charts done", avg_cloth, avg_kitchen)
