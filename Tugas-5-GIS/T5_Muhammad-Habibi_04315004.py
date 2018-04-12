import mapnik
m = mapnik.Map(1280,720)
m.background = mapnik.Color('#86fff2')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
r.symbols.append(polygon_symbolizer) 


line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'), 'DejaVu Sans Bold',8,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap= True
r.symbols.append(point_sym)


s.rules.append(r)

highlight = mapnik.PolygonSymbolizer()
highlight.fill = mapnik.Color('magenta')
japan = mapnik.Rule()
japan.filter = mapnik.Expression("[NAME]='Japan'")
japan.symbols.append(highlight)
s.rules.append(japan)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="Natural_Earth/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)


s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('brown'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)


m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_sungai/IND_SNG_polyline.shp")
layer = mapnik.Layer('kota')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)


s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('lightblue'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)


m.append_style('My Style3',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_sungai/IND_SNG_region.shp")
layer = mapnik.Layer('pantai')
layer.datasource = ds
layer.styles.append('My Style3')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('orange'), 2)
r.symbols.append(line_symbolizer)
s.rules.append(r)


m.append_style('My Style4',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_pantai/IND_PNT_rectangle.shp")
layer = mapnik.Layer('country2')
layer.datasource = ds
layer.styles.append('My Style4')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 0.1)
r.symbols.append(line_symbolizer)
s.rules.append(r)


m.append_style('My Style5',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_pantai/IND_PNT_polyline.shp")
layer = mapnik.Layer('country3')
layer.datasource = ds
layer.styles.append('My Style5')
m.layers.append(layer)



m.zoom_all()
mapnik.render_to_file(m, 'T5_Muhammad-Habibi_04315004.pdf', 'pdf')
print "rendered image to 'T5_Muhammad-Habibi_04315004.png' "
