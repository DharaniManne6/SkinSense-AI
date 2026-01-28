import pandas as pd
import re


def clean_text(value):
    """
    Turns:
    "[' ', 'Oily', ' ', 'Radiance']"
    into:
    "Oily, Radiance"
    """
    if pd.isna(value):
        return "Not specified"

    value = str(value)

    # Remove brackets and quotes
    value = re.sub(r"[\[\]'\" ]+", " ", value)

    # Split by comma, clean items
    items = [v.strip() for v in value.split(",") if v.strip()]

    return ", ".join(items) if items else "Not specified"


def score_ingredient(row, skin_type, concern):
    score = 0

    good_for = str(row["who_is_it_good_for"]).lower()
    avoid = str(row["who_should_avoid"]).lower()
    benefits = str(row["what_does_it_do"]).lower()

    if skin_type.lower() in good_for:
        score += 3

    if concern.lower() in benefits:
        score += 2

    if skin_type.lower() in avoid:
        score -= 5

    return score


def recommend_ingredients(df, skin_type, concern):
    df = df.copy()

    df["score"] = df.apply(
        lambda row: score_ingredient(row, skin_type, concern), axis=1
    )

    df = df[df["score"] > 0]
    df = df.sort_values(by="score", ascending=False)

    results = []

    for _, row in df.head(10).iterrows():
        results.append({
            "name": row.get("name"),
            "short_description": str(row.get("what_does_it_do", "")).split(".")[0] + ".",
            "who_is_it_good_for": clean_text(row.get("who_is_it_good_for", "")),
            "who_should_avoid": clean_text(row.get("who_should_avoid", "")),
            "url": row.get("url", "")
        })

    return results
