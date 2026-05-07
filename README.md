# Conflict Impact on Education
Nigerian Chapter: North East and North West Regions

Interactive dashboard for analyzing the relationship between conflict intensity and educational infrastructure in Northern Nigeria.

## [🚀 View Interactive Dashboard](https://dicocorobe.github.io/ICT4DNigeria/)

## Features
- **Temporal Analysis:** Visualizing annual conflict trends from 2000 to 2024.
- **Geospatial Mapping:** Incident clustering with intensity scaling (Yellow-Orange-Red).
- **Education Infrastructure:** Integrated school facility mapping (points and polygons) with density-aware clustering.
- **Interactive Filtering:** Filter by conflict type, region, and custom year ranges.
- **Prototype Reporting:** Built-in "Field Report" prototype for event recording.

## Data Processing
Datasets are filtered geographically specifically for the North West and North East regions using coordinate bounding boxes.
- `data/filtered_conflict_data.csv`: Conflict incident records.
- `data/filtered_education_points.geojson`: Specific educational facility locations.
- `data/filtered_education_polygons.geojson`: Educational campus boundaries.

## Documentation
For a detailed breakdown of the development cycle and technical decisions, see [docs/PROCESS.md](./docs/PROCESS.md).
