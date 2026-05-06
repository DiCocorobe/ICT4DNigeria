import json

def filter_geo(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    filtered_features = []
    for feature in data['features']:
        # Get coordinates based on geometry type
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        elif geom['type'] == 'Polygon':
            # Use the first point of the outer ring for region check
            lon, lat = geom['coordinates'][0][0]
        elif geom['type'] == 'MultiPolygon':
            lon, lat = geom['coordinates'][0][0][0]
        else:
            continue
            
        region = None
        # North West: Jigawa, Kaduna, Kano, Katsina, Kebbi, Sokoto, Zamfara
        # North East: Adamawa, Bauchi, Borno, Gombe, Taraba, Yobe
        
        # Approximate bounding boxes
        # NW: 3.5-9.0 E, 9.3-14.0 N
        if (3.5 <= lon <= 9.0) and (9.3 <= lat <= 14.0):
            # Exclude FCT/Plateau area
            if not (lat < 10.0 and lon > 6.8): 
                region = "North West"
        
        # NE: 9.0-15.0 E, 6.5-14.0 N
        if not region and (9.0 <= lon <= 15.0) and (6.5 <= lat <= 14.0):
            region = "North East"
            
        if region:
            feature['properties']['Analysis_Region'] = region
            filtered_features.append(feature)
            
    data['features'] = filtered_features
    with open(output_file, 'w') as f:
        json.dump(data, f)
    print(f"Filtered {input_file} -> {output_file}. Kept {len(filtered_features)} features.")

filter_geo('hotosm_nga_education_facilities_points_geojson.geojson', 'filtered_education_points.geojson')
filter_geo('hotosm_nga_education_facilities_polygons_geojson.geojson', 'filtered_education_polygons.geojson')
