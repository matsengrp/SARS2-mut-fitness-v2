import pandas as pd
rates = pd.read_csv("master_table_pre_omicron.csv")
rates.query("~nt_site_before_boundary")[["mut_type", "motif", "unpaired", "rate"]].to_csv("rates_table_after_boundary.csv", index=False)
