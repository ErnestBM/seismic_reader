import os
from celery import shared_task # type: ignore
from .views import process_seismic_data

@shared_task
def fetch_seismic_data():
    print("Fetching seismic data...")
    
    # Fetch seismic data
    csv_data = process_seismic_data()
    print("Seismic data downloaded successfully")
    
    # Ensure the directory exists
    output_dir = './tmp_waveform/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Write data to file
    output_file = os.path.join(output_dir, 'seismic_data.csv')
    with open(output_file, 'w') as f:
        f.write(csv_data)
    
    print(f"Seismic data written to file at {output_file}")
