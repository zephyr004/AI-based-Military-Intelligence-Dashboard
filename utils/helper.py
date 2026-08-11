import pandas as pd

def format_number(num):
    if num >= 1_000_000:
        return f"{num/1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num/1_000:.1f}K"
    return str(int(num))

def total_attacks(df):
    return len(df)

def total_countries(df):
    return df["country_txt"].nunique()

def total_groups(df):
    return df["gname"].nunique()

def total_killed(df):
    return int(df["nkill"].fillna(0).sum())