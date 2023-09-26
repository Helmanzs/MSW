import pandas as pd
import matplotlib.pyplot as plot

horror_movies = pd.read_csv("uloha2\horror_movies.csv")

# Movies in language
language_counts = horror_movies["original_language"].value_counts()
language_counts.plot(
    kind="bar",
    xlabel="Language",
    ylabel="Count",
    figsize=(18, 6),
    title="Movies by Language",
)
plot.xticks(rotation=45)
plot.show()

# Movie runtimes
filtered_horror_movies = horror_movies[horror_movies["runtime"] > 0]
filtered_horror_movies["runtime"].plot(
    kind="hist",
    bins=50,
    range=(0, 240),
    edgecolor="k",
    xlabel="Runtime (minutes)",
    ylabel="Frequency",
    title="Movie Runtimes",
)
plot.show()

# Budges vs revenue
horror_movies.plot(
    kind="scatter",
    x="budget",
    y="revenue",
    alpha=0.5,
    color="g",
    xlabel="Budget",
    ylabel="Revenue",
    title="Budget vs Revenue",
)
plot.show()

# Number of movies in each year
horror_movies["release_year"] = pd.to_datetime(horror_movies["release_date"]).dt.year
movies_per_year = horror_movies.groupby("release_year")["original_title"].count()
movies_per_year.plot(
    kind="line",
    marker="o",
    linestyle="-",
    xlabel="Year",
    ylabel="Number of Movies Released",
    title="Number of Movies Released Each Year",
    grid=True,
    figsize=(12, 6),
)
plot.show()

# Average popularity by year
box = horror_movies.boxplot(
    column="popularity",
    by="release_year",
    showfliers=False,
    figsize=(18, 6),
    xlabel="Release Year",
    ylabel="Popularity",
    grid=False,
)
plot.title("")
plot.suptitle("Movie Popularity by Year")
plot.xticks(rotation=45)
plot.show()
