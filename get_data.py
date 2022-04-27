# skript na automaticke stazeni a rozbaleni dat GTFS
import requests, zipfile, io
r = requests.get("http://data.pid.cz/PID_GTFS.zip")
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("gtfs")