import os
import simplekml

kml = simplekml.Kml(name='9_tours', open=1)

pnt = kml.newpoint(name="New Zealand's Southern Alps", coords=[(170.144,-43.605)])
pnt.style.iconstyle.scale = 1.0

tour = kml.newgxtour(name="Play me!")
playlist = tour.newgxplaylist()

ani_update = playlist.newgxanimatedupdate(gxduration=6.5)
ani_update.update.change = '<IconStyle targetId="{0}"><scale>10.0</scale></IconStyle>'.format(pnt.style.iconstyle.id)

flyto = playlist.newgxflyto(gxduration=4.1)
flyto.camera.longitude = 170.157
flyto.camera.latitude = -43.671
flyto.camera.altitude = 9700
flyto.camera.heading = -6.333
flyto.camera.tilt = 33.5
flyto.camera.roll = 0

wait = playlist.newgxwait(gxduration=2.4)

kml.save(os.path.splitext(__file__)[0] + ".kml")