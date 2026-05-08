import pandas as pd

DK_WEIGHTS = {
    'pts': 1.0,
    'reb': 1.25,
    'ast': 1.5,
    'stl': 2.0,
    'blk': 2.0,
}

DOUBLE_DOUBLE_BONUS = 1.5
TRIPLE_DOUBLE_BONUS = 3.0


def calculate_fantasy_points(pts, reb, ast, stl, blk):
    base = (
        pts * DK_WEIGHTS['pts']
        + reb * DK_WEIGHTS['reb']
        + ast * DK_WEIGHTS['ast']
        + stl * DK_WEIGHTS['stl']
        + blk * DK_WEIGHTS['blk']
    )

    double_digit_count = sum(x >= 10 for x in [pts, reb, ast, stl, blk])

    if double_digit_count >= 3:
        base += TRIPLE_DOUBLE_BONUS
    elif double_digit_count >= 2:
        base += DOUBLE_DOUBLE_BONUS

    return round(base, 2)


def add_fantasy_points(df):
    df = df.copy()
    df['fantasy_pts'] = df.apply(
        lambda row: calculate_fantasy_points(
            row['pts'], row['reb'], row['ast'], row['stl'], row['blk']
        ),
        axis=1,
    )
    return df
