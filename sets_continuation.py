
# Define a new set
rich_countries = {
    "USA",
    "Canada",
    "China",
    "Japan",
    "Italy",
    "Germany",
    "Korea",
    "Saudi Arabia"
}

some_countries = {
    "USA",
    "Canada",
    "Italy",
    "Germany"
}
# Example of a set difference
non_english = rich_countries - some_countries
print(f"These countries are rich but they dont speak english {non_english}")

# Example of set union
all_rich_countries = rich_countries | some_countries
print(f"These are all rich countries {all_rich_countries}")


# Example of set intersection
common_in_both = rich_countries & some_countries
print(f"These countries are common in both {common_in_both}")

#Example of superset
bigger_one = rich_countries > some_countries
print(f"The rich_countries set is bigger than the some_countries set True/False = {bigger_one}")

#Example of subset
subset_one = some_countries < rich_countries
print(f"The some_countries set is a subset of the rich_countries set True/False = {subset_one}")
