# Merging Data

Merging combines data from multiple DataFrames based on common columns or indices.

## Merge Types
- Inner join (intersection)
- Outer join (union)
- Left join (all from left)
- Right join (all from right)
- Cross join (Cartesian product)

## Merge Methods
- `merge()` for database-style joins
- `join()` for index-based joins
- Concatenation for stacking
- Merge on columns
- Merge on index

## Merge Parameters
- On columns for merging
- How type of join
- Left and right DataFrames
- Suffixes for duplicate columns
- Indicator for merge type

## Use Cases
- Combining datasets
- Data integration
- Multi-source data
- Relational data
- Data enrichment