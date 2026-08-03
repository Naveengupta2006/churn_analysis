import json

BROKEN_MARKER = "corr_df['escalations'].corr(df['churn_flag'])"

FIXED_SOURCE = [
    "# 10. correlation escalation vs churn\n",
    "corr_df = df[['escalations','churn_flag']].dropna().copy()\n",
    "corr_df['escalations'] = np.where(corr_df['escalations'] == 'Y', 1, 0)  # encode Y/N to 1/0\n",
    "correlation = corr_df['escalations'].corr(corr_df['churn_flag'])\n",
    "print(\"Correlation between escalation vs churn is = \", round(correlation, 2))"
]

with open('churn.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

fixed = 0
for cell in nb['cells']:
    if cell.get('cell_type') == 'code':
        src = ''.join(cell.get('source', []))
        if BROKEN_MARKER in src:
            cell['source'] = FIXED_SOURCE
            cell['outputs'] = []
            cell['execution_count'] = None
            fixed += 1

print(f"Fixed {fixed} cell(s)")
with open('churn.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Saved churn.ipynb successfully.")
