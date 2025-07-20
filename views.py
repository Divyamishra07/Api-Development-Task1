
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class PlaceFromCoords(APIView):
    def get(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        if not lat or not lon:
            return Response({"error": "lat and lon required"}, status=400)

        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
        headers = {'User-Agent': 'geoapi'}
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            return Response({"error": "Failed to fetch location"}, status=500)
        data = r.json()

        return Response({
            "place_name": data.get("display_name", "Unknown"),
            "address": data.get("address", {})
        })
