# Project Development Process: Conflict Impact on Education Dashboard

This document outlines the end-to-end process of building the "Conflict Impact on Education" interactive dashboard for the North East and North West regions of Nigeria.

## 1. Research & Data Analysis Phase
- **Data Source Identification:** Analyzed multiple datasets including conflict incidents (UCDP/ACLED style), education facilities (OpenStreetMap/HOTOSM), and initial literacy data.
- **Data Quality Audit:** Identified inconsistencies in CSV parsing, specifically shifted columns in conflict data due to complex quoted strings.
- **Geographic Filtering:** Developed Python scripts (`refilter_conflict.py`, `refilter_education.py`) to isolate data specifically for the North West and North East regions using coordinate bounding boxes.

## 2. Design & Planning Phase
- **Objective:** Create a prototype that visualizes the spatial relationship between conflict intensity and educational infrastructure.
- **Visual Strategy:** 
    - Use a **Yellow-Orange-Red** scale for conflict clusters to represent intensity/danger.
    - Use a **Green** scale for education clusters to represent facility density.
    - Implement a modular layout with a sidebar for controls and a primary map area.
- **Tech Stack:** React (Frontend), Leaflet (Mapping), PapaParse (CSV Parsing), and Vanilla CSS.

## 3. Implementation Phase
- **Component Architecture:**
    - `MapContainer`: Handles Leaflet initialization, tile layer switching (Dark/Light mode), and layer management.
    - `SimpleChart`: A zero-dependency SVG-based bar chart for temporal analysis.
    - `Sidebar`: Contains statistical summaries and interactive filters (Conflict Type, Region, Date Range).
- **Advanced Mapping Features:**
    - **Incident Clustering:** Grouped conflict events to prevent visual overlap.
    - **Education Area Integration:** Integrated both point-based schools and polygon-based campuses.
    - **Centroid Clustering:** Implemented logic to calculate centroids for area polygons so they are included in the numerical cluster counts.

## 4. Refinement & Validation Phase
- **Chart Accuracy:** Refactored the "Annual Conflict Events" chart to ensure every year in the timeline (2000-2024) is represented, fixing a previous "steep rise" visualization bug.
- **Data Syncing:** Implemented a robust data-cleaning layer in the frontend to handle parsing errors and ensure map markers and chart bars are perfectly synchronized.
- **Prototype Logic:** Transitioned the "Field Report" system to a prototype-only mode (frontend-only) to allow for demonstration without a persistent backend.

## 5. Final Branding & Cleanup
- **Branding:** Renamed the project to "Conflict Impact on Education" to better align with the integrated data approach.
- **Repository Tidy-up:** Removed unused literacy datasets to focus the repository on the primary dashboard mission.

---
*Developed as part of the ICT4DNigeria Project.*
