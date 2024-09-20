import pandas as pd
wine_reviews = pd.read_csv("../wine-reviews-exercise-kfrancis812/data/winemag-data-130k-v2.csv.zip")
reviews_per_country = pd.DataFrame({
    'count': wine_reviews.country.value_counts(),
    'points': wine_reviews.points.mean().round(1)
        })
reviews_per_country.to_csv('data/reviews-per-country.csv')