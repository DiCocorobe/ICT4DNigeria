import csv

def filter_conflict(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        if 'Analysis_Region' not in fieldnames:
            fieldnames.append('Analysis_Region')
        if 'official_conflict_type' not in fieldnames:
            fieldnames.append('official_conflict_type')
            
        rows = []
        for row in reader:
            try:
                lat = float(row['latitude'])
                lon = float(row['longitude'])
            except (ValueError, TypeError):
                continue
                
            region = None
            if (3.5 <= lon <= 9.0) and (9.3 <= lat <= 14.0):
                if not (lat < 10.0 and lon > 6.8):
                    region = "North West"
            
            if not region and (9.0 <= lon <= 15.0) and (6.5 <= lat <= 14.0):
                region = "North East"
                
            if region:
                row['Analysis_Region'] = region
                # Simple mapping for official_conflict_type if it doesn't exist
                # type_of_violence: 1=state, 2=non-state, 3=one-sided
                v_type = row.get('type_of_violence')
                if v_type == '1': row['official_conflict_type'] = 'State-based conflict'
                elif v_type == '2': row['official_conflict_type'] = 'Non-state conflict'
                elif v_type == '3': row['official_conflict_type'] = 'One-sided violence'
                else: row['official_conflict_type'] = 'Other'
                
                rows.append(row)
                
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Filtered {input_file} -> {output_file}. Kept {len(rows)} rows.")

filter_conflict('conflict_data_nga.csv', 'filtered_conflict_data.csv')
