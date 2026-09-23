# Analysis Report: Sisal Fibre and Banana Peel as Natural Coagulants for Greywater Treatment

## 1. Background & Objective

Household greywater — water discharged from laundry and kitchen activities — carries elevated turbidity, organic load, and dissolved solids that make it unsafe for direct reuse or discharge. Alum (aluminium sulphate) is the conventional coagulant used to treat such water, but it is a manufactured chemical with cost, supply, and residual-aluminium concerns, especially for low-income or off-grid households.

This study evaluated two **agro-waste-derived natural coagulants — sisal fibre and banana peel** — as low-cost, biodegradable alternatives to alum, testing their ability to reduce contaminant levels in two greywater streams: **clothes-washing water** and **kitchen-washing water**.

## 2. Method

- **Water sources:** untreated (control) samples of clothes-washing water and kitchen-washing water.
- **Coagulants tested:** sisal fibre, banana peel, and alum (as the benchmark/positive control), each run in **three replicate trials**.
- **Parameters measured:** pH, temperature, electrical conductivity (EC), turbidity, total dissolved solids (TDS), total suspended solids (TSS), biochemical oxygen demand (BOD), chemical oxygen demand (COD), calcium, magnesium, sodium.
- **Removal efficiency (RE%)** was calculated for each treated sample relative to the untreated control for that water source.
- **Statistical analysis:**
  - One-way ANOVA across the three coagulants, per parameter, per water source.
  - Tukey HSD post-hoc pairwise comparison, run only where ANOVA showed significance (p < 0.05).
  - Pearson correlation between physically/chemically related parameter pairs (TDS–EC, BOD–COD, TSS–turbidity, Ca–Mg), computed across the nine treated-sample readings (3 coagulants × 3 replicates); the control was excluded from this analysis.
- **Water-quality benchmarking:** treated samples were compared against **FAO (Ayers & Westcot, 1985)** irrigation water guideline thresholds for EC, TDS, and sodium adsorption ratio (SAR). FAO has no published guideline for BOD, COD, TSS, turbidity, or individual calcium/magnesium concentrations, so those are not benchmarked here.

## 3. Results — Laundry (Clothes-Washing) Water

### 3.1 Summary of treated-water quality

| Parameter | Control | Sisal Fibre (Mean ± SD) | Sisal RE% | Banana Peel (Mean ± SD) | Banana RE% | Alum (Mean ± SD) | Alum RE% |
|---|---|---|---|---|---|---|---|
| pH | 8.00 | 6.17 ± 0.17 | — | 6.03 ± 1.15 | — | 6.54 ± 0.06 | — |
| Temperature (°C) | 21.00 | 18.71 ± 0.28 | — | 18.68 ± 0.14 | — | 18.53 ± 0.06 | — |
| Electrical conductivity | 6.00 | 4.31 ± 0.10 | 28.1% | 4.47 ± 0.06 | 25.5% | 4.24 ± 0.06 | 29.4% |
| Turbidity (NTU) | 7.00 | 5.43 ± 0.12 | 22.4% | 5.48 ± 0.06 | 21.7% | 5.27 ± 0.21 | 24.7% |
| TDS (mg/L) | 807.00 | 688.00 ± 9.61 | 14.7% | 779.44 ± 63.63 | 3.4% | 686.11 ± 5.54 | 15.0% |
| TSS (mg/L) | 135.05 | 102.53 ± 11.58 | 24.1% | 110.95 ± 12.92 | 17.8% | 48.95 ± 57.49 | 63.8% |
| BOD (mg/L) | 210.00 | 112.67 ± 0.27 | 46.3% | 115.01 ± 0.01 | 45.2% | 45.02 ± 57.96 | 78.6% |
| COD (mg/L) | 125.01 | 112.05 ± 0.18 | 10.4% | 114.84 ± 2.03 | 8.1% | 110.67 ± 2.91 | 11.5% |
| Calcium (mg/L) | 222.09 | 96.94 ± 1.08 | 56.4% | 98.17 ± 0.29 | 55.8% | 86.03 ± 1.00 | 61.3% |
| Magnesium (mg/L) | 220.37 | 118.22 ± 4.55 | **46.4%** | 168.93 ± 9.84 | 23.3% | 172.56 ± 52.78 | 21.7% |
| Sodium (mg/L) | 200.00 | 214.56 ± 6.17 | -7.3% | 218.55 ± 5.70 | -9.3% | 199.11 ± 1.39 | 0.4% |

Sodium showed a **negative removal efficiency** for all three coagulants (i.e. sodium concentration slightly increased post-treatment) — most pronounced for banana peel (-9.3%) and sisal fibre (-7.3%). This is plausible given both are plant materials that can leach small amounts of sodium and other ions into the water during treatment.

Notably, **sisal fibre outperformed alum on magnesium removal** (46.4% vs 21.7%), and was within a few points of alum on calcium removal (56.4% vs 61.3%) and EC (28.1% vs 29.4%).

### 3.2 One-way ANOVA across coagulants

| Parameter | F statistic | p-value | Significant (p<0.05)? |
|---|---|---|---|
| pH | 0.45 | 0.6560 | No |
| Temperature (°C) | 0.78 | 0.4987 | No |
| Electrical conductivity | 7.50 | 0.0233 | **Yes** |
| Turbidity (NTU) | 1.75 | 0.2519 | No |
| TDS (mg/L) | 6.14 | 0.0353 | **Yes** |
| TSS (mg/L) | 2.82 | 0.1368 | No |
| BOD (mg/L) | 4.23 | 0.0714 | No |
| COD (mg/L) | 3.23 | 0.1116 | No |
| Calcium (mg/L) | 179.39 | <0.001 | **Yes** |
| Magnesium (mg/L) | 2.86 | 0.1341 | No |
| Sodium (mg/L) | 13.09 | 0.0065 | **Yes** |

**Tukey HSD post-hoc (significant parameters only):**

- **Electrical conductivity:** Alum vs Banana Peel differ significantly (p = 0.021); Alum–Sisal and Banana–Sisal do not.
- **TDS:** no individual pair reached significance after correction, despite the overall ANOVA being significant (borderline Alum vs Banana Peel and Banana vs Sisal, both p ≈ 0.05).
- **Calcium:** Alum differs significantly from both Banana Peel (p < 0.001) and Sisal Fibre (p < 0.001); Banana Peel and Sisal Fibre do not differ from each other — i.e. the two natural coagulants perform similarly on calcium, and both are outperformed by alum.
- **Sodium:** Alum differs significantly from both Banana Peel (p = 0.007) and Sisal Fibre (p = 0.020); Banana Peel and Sisal Fibre do not differ from each other.

### 3.3 Pearson correlation (treated samples only)

| Parameter pair | r | p-value | Interpretation |
|---|---|---|---|
| TDS vs Electrical conductivity | 0.824 | 0.0063 | Strong positive (significant) |
| BOD vs COD | 0.063 | 0.8728 | Weak positive (not significant) |
| TSS vs Turbidity | 0.291 | 0.4482 | Weak positive (not significant) |
| Calcium vs Magnesium | -0.266 | 0.4897 | Weak negative (not significant) |

The strong TDS–EC correlation is expected, as both track dissolved ionic content. The lack of correlation between BOD and COD, and between TSS and turbidity, suggests the coagulants are acting on organic load and particulate matter somewhat independently rather than uniformly across all fractions.

### 3.4 FAO irrigation water guideline comparison

| Sample | pH | EC (dS/m) | EC rating | TDS (mg/L) | TDS rating | SAR | SAR rating |
|---|---|---|---|---|---|---|---|
| Control (untreated) | 8.00 | 6.00 | Severe | 807.0 | Slight to moderate | 2.28 | Safe |
| Sisal Fibre | 6.17 | 4.31 | Severe | 688.0 | Slight to moderate | 3.46 | Safe |
| Banana Peel | 6.03 | 4.47 | Severe | 779.4 | Slight to moderate | 3.10 | Safe |
| Alum | 6.54 | 4.24 | Severe | 686.1 | Slight to moderate | 2.85 | Safe |

*FAO guideline reference values — degree of restriction on use: EC < 0.7 (none), 0.7–3.0 (slight to moderate), >3.0 (severe) dS/m; TDS <450 / 450–2000 / >2000 mg/L; SAR <10 / 10–18 / >18. Normal pH range: 6.5–8.4.*

All treated samples remain in the **"Severe" EC restriction band** — none of the three coagulants, including alum, brought conductivity down far enough for unrestricted irrigation use. TDS and SAR, however, are comfortably within safe/acceptable bounds for all samples.

---

## 4. Results — Kitchen-Washing Water

### 4.1 Summary of treated-water quality

| Parameter | Control | Sisal Fibre (Mean ± SD) | Sisal RE% | Banana Peel (Mean ± SD) | Banana RE% | Alum (Mean ± SD) | Alum RE% |
|---|---|---|---|---|---|---|---|
| pH | 9.33 | 6.20 ± 0.20 | — | 5.88 ± 0.04 | — | 6.28 ± 0.06 | — |
| Temperature (°C) | 22.00 | 18.96 ± 0.08 | — | 19.00 ± 0.00 | — | 18.42 ± 0.37 | — |
| Electrical conductivity | 8.00 | 5.11 ± 0.43 | 36.1% | 5.76 ± 0.25 | 28.0% | 4.61 ± 0.12 | 42.3% |
| Turbidity (NTU) | 7.50 | 6.23 ± 0.25 | 16.9% | 6.97 ± 0.05 | 7.1% | 5.70 ± 0.24 | 24.0% |
| TDS (mg/L) | 800.01 | 545.05 ± 67.77 | 31.9% | 605.11 ± 5.96 | 24.4% | 522.78 ± 129.84 | 34.7% |
| TSS (mg/L) | 315.00 | 130.00 ± 18.69 | 58.7% | 103.87 ± 57.20 | **67.0%** | 62.23 ± 45.45 | 80.2% |
| BOD (mg/L) | 226.99 | 92.46 ± 6.72 | 59.3% | 83.81 ± 5.41 | 63.1% | 57.60 ± 41.51 | 74.6% |
| COD (mg/L) | 294.98 | 141.39 ± 61.24 | **52.1%** | 201.48 ± 57.61 | 31.7% | 145.56 ± 50.67 | 50.7% |
| Calcium (mg/L) | 225.00 | 91.30 ± 1.78 | 59.4% | 67.27 ± 41.70 | **70.1%** | 87.63 ± 0.54 | 61.1% |
| Magnesium (mg/L) | 280.00 | 84.33 ± 5.86 | **69.9%** | 86.01 ± 5.30 | 69.3% | 162.56 ± 70.65 | 41.9% |
| Sodium (mg/L) | 299.70 | 153.55 ± 31.86 | 48.8% | 326.96 ± 222.90 | -9.1% | 197.78 ± 0.69 | 34.0% |

Kitchen water shows a markedly different picture from laundry water: **sisal fibre and banana peel are highly competitive with, and in several cases beat, alum**:

- **Sisal fibre outperformed alum on COD** (52.1% vs 50.7%) and **magnesium** (69.9% vs 41.9%) — a substantial margin on magnesium.
- **Banana peel outperformed alum on TSS** (67.0% vs 80.2% — alum still ahead here, but banana peel is close) and **calcium** (70.1% vs 61.1%).
- Sodium removal was highly variable for banana peel (RE% of -9.1%, driven by one high replicate reading), reflected in its very large standard deviation (±222.90).

### 4.2 One-way ANOVA across coagulants

| Parameter | F statistic | p-value | Significant (p<0.05)? |
|---|---|---|---|
| pH | 9.06 | 0.0154 | **Yes** |
| Temperature (°C) | 6.57 | 0.0308 | **Yes** |
| Electrical conductivity | 11.59 | 0.0087 | **Yes** |
| Turbidity (NTU) | 29.30 | 0.0008 | **Yes** |
| TDS (mg/L) | 0.76 | 0.5080 | No |
| TSS (mg/L) | 1.85 | 0.2368 | No |
| BOD (mg/L) | 1.65 | 0.2685 | No |
| COD (mg/L) | 1.05 | 0.4060 | No |
| Calcium (mg/L) | 0.87 | 0.4675 | No |
| Magnesium (mg/L) | 3.56 | 0.0958 | No |
| Sodium (mg/L) | 1.44 | 0.3082 | No |

**Tukey HSD post-hoc (significant parameters only):**

- **pH:** Alum vs Banana Peel differ significantly (p = 0.017); Banana Peel vs Sisal Fibre also differ (p = 0.041); Alum and Sisal Fibre do not differ.
- **Temperature:** Alum vs Banana Peel differ significantly (p = 0.040); the other two pairs do not.
- **Electrical conductivity:** Alum vs Banana Peel differ significantly (p = 0.007); Alum–Sisal and Banana–Sisal do not.
- **Turbidity:** all three pairs differ significantly — Alum vs Banana Peel (p < 0.001), Alum vs Sisal (p = 0.043), and Banana vs Sisal (p = 0.011) — meaning each coagulant produced a distinguishably different turbidity outcome.

Note that for the parameters where the two natural coagulants showed their best relative performance in kitchen water — TSS, BOD, COD, calcium, magnesium, sodium — **ANOVA did not find a statistically significant difference between coagulants**. This means the apparent gaps in mean removal efficiency for those parameters cannot be considered statistically robust at this sample size (n=3 per group); more replicates would be needed to confirm whether sisal fibre's edge on COD and magnesium, for example, is a real effect or sampling noise.

### 4.3 Pearson correlation (treated samples only)

| Parameter pair | r | p-value | Interpretation |
|---|---|---|---|
| TDS vs Electrical conductivity | 0.469 | 0.2024 | Moderate positive (not significant) |
| BOD vs COD | 0.137 | 0.7247 | Weak positive (not significant) |
| TSS vs Turbidity | 0.350 | 0.3557 | Weak positive (not significant) |
| Calcium vs Magnesium | 0.164 | 0.6736 | Weak positive (not significant) |

Unlike the laundry water dataset, none of the correlations reach statistical significance in kitchen water, likely reflecting the greater variability (higher SDs) across replicates in this dataset.

### 4.4 FAO irrigation water guideline comparison

| Sample | pH | EC (dS/m) | EC rating | TDS (mg/L) | TDS rating | SAR | SAR rating |
|---|---|---|---|---|---|---|---|
| Control (untreated) | 9.33 | 8.00 | Severe | 800.0 | Slight to moderate | 3.15 | Safe |
| Sisal Fibre | 6.20 | 5.11 | Severe | 545.0 | Slight to moderate | 2.79 | Safe |
| Banana Peel | 5.88 | 5.76 | Severe | 605.1 | Slight to moderate | 6.23 | Safe |
| Alum | 6.28 | 4.61 | Severe | 522.8 | Slight to moderate | 2.89 | Safe |

As with laundry water, all treated kitchen-water samples improved on TDS and remain within the "Safe" SAR band, but EC stays in the "Severe" restriction category across every treatment, including alum.

---

## 5. Discussion

1. **Alum remains the strongest all-round performer**, particularly for turbidity, TSS, and BOD — parameters most directly tied to particulate and organic removal, where its charge-neutralisation mechanism is well suited.
2. **Sisal fibre is the more promising of the two natural coagulants overall**, consistently matching or approaching alum's performance — and even exceeding it on magnesium (both water types) and COD (kitchen water) — while banana peel's results were more variable, including a negative removal efficiency for sodium in both water sources.
3. **Natural coagulants perform relatively better on kitchen greywater than on laundry greywater.** This is plausibly linked to the different pollutant profile: kitchen water carries more organic/particulate load (higher control-sample TSS, BOD, COD), which plant-fibre-based coagulation appears to handle comparatively well, whereas laundry water's higher surfactant and dissolved-solid content may be less responsive to natural coagulant mechanisms.
4. **Statistical power is limited (n=3 per group).** Several parameters — especially in kitchen water — show promising average differences that did not reach statistical significance. This should be read as *"not yet demonstrated,"* not as *"no difference exists."* A larger-scale follow-up with more replicates would sharpen these conclusions.
5. **None of the treatments, including alum, resolve the electrical conductivity problem** relative to FAO's irrigation guideline. If irrigation reuse is a target application, an additional or different treatment step for salinity reduction would be needed regardless of which coagulant is used.

## 6. Conclusion

Sisal fibre and banana peel — both freely available agricultural waste materials — demonstrate real, measurable coagulation ability for household greywater treatment, and in several parameters (notably magnesium, and COD for kitchen water) **sisal fibre performs on par with or better than alum**. While alum retains an edge in turbidity and organic-load reduction overall, the natural coagulants' low cost, biodegradability, and accessibility make them a credible, sustainable option for decentralised greywater pre-treatment in low-resource settings — particularly for kitchen wastewater.

## 7. Recommendations

- Increase replicate count per treatment group to strengthen statistical power, especially for kitchen-water parameters that trended favourably but were not significant.
- Investigate a combined/hybrid dosing of sisal fibre or banana peel with a reduced alum dose, to see whether blending natural and chemical coagulants can match alum's turbidity/TSS performance while cutting chemical usage.
- Add a dedicated salinity-reduction step (e.g. post-treatment filtration) if the goal is FAO-compliant water for irrigation reuse, since EC remained in the "Severe" band across all treatments.
- Investigate the cause of elevated sodium in banana-peel-treated samples, to rule out leaching from the peel material itself.

---

*Data source: `data/raw/` (triplicate lab readings) and `data/processed/` (summary statistics, ANOVA/Tukey, correlation, FAO comparison), University of Jos Civil Engineering research project.*
