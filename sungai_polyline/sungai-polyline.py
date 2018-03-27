#render1
import mapnik
m = mapnik.Map(1812,1566)
m.background = mapnik.Color('lightblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('pink')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#0fe3b9'), 2)
line_symbolizer.stroke_width = 20.0

#render1
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_sungai\IND_SNG_polyline.shp")
layer = mapnik.Layer('m_habibi_04315004-3')
layer.datasource = ds 
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'m_habibi_04315004-3.pdf', 'pdf')
print "rendered image to 'm_habibi_04315004-3.pdf'"
