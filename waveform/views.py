from django.http import HttpResponse
import pandas as pd
from obspy.clients.fdsn import Client
from obspy import UTCDateTime

def get_seismic_data(request):
    client = Client("GFZ")

    t = UTCDateTime.now() - 300

    inventory = client.get_stations(
        network="GX", sta="CAMPI", loc="*", channel="*",
        level="response"
    )

    station_info = []
    for network in inventory: # type: ignore
        for station in network:
            station_info.append({
                'StationCode': station.code,
                'Latitude': station.latitude,
                'Longitude': station.longitude
            })

    st = client.get_waveforms(
        network="GX", station="CAMPI", location="*", channel="*",
        starttime=t, endtime=t + 60
    )

    sample_data = {}
    for trace in st: # type: ignore
        sampling_interval = trace.stats.delta
        timestamps = [trace.stats.starttime + i * sampling_interval for i in range(100)]
        formatted_timestamps = [timestamp.isoformat() for timestamp in timestamps]
        sample_data[trace.id] = trace.data[:100]

    df = pd.DataFrame(sample_data)

    df.insert(0, "StationCode", station_info[0]['StationCode'])
    df.insert(0, "Latitude", station_info[0]['Latitude'])
    df.insert(0, "Longitude", station_info[0]['Longitude'])
    df.insert(0, "Timestamp", formatted_timestamps) # type: ignore

    csv_data = df.to_csv(index=False)

    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="seismic_samples_with_station_info.csv"'

    return response
