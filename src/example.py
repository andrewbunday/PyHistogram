from PIL import Image
import pylab
import os
#import PythonMagick

file_path = '%s/../reference/aa_van_and_bike.jpg' % os.path.dirname(os.path.abspath(__file__))
ncolors = 255

im = pylab.array(Image.open(file_path))
#raw_data = file(file_path,'rb').read()
#img = PythonMagick.Image(PythonMagick.Blob(raw_data))

#img.depth = 8
#img.magick = "RGB"

#blob = PythonMagick.Blob()
#img.write(blob)

#pil_img = Image.fromstring('RGB', (img.columns(), img.rows()), PythonMagick.get_blob_data(blob))
#im = pylab.array(pil_img)

blue  = [ b for channel in im[:,:,2] for b in channel ]
green = [ g for channel in im[:,:,1] for g in channel ]
red   = [ r for channel in im[:,:,0] for r in channel ]

pylab.figure()
b_n, b_bins, var = pylab.hist(blue, ncolors, histtype='stepfilled', align='left',alpha=0.5,aa=False,ec='none')
g_n, g_bins, var = pylab.hist(green, ncolors, histtype='stepfilled', align='left',alpha=0.5,aa=False,ec='none')
r_n, r_bins, Var = pylab.hist(red, ncolors, histtype='stepfilled', align='left',alpha=0.5,aa=False,ec='none')

#figure()
#plot(b_bins[1:], b_n, 'b-', linewidth=3, aa=False)
#plot(g_bins[1:], g_n, 'g-', linewidth=3, aa=False)
#plot(r_bins[1:], r_n, 'r-', linewidth=3, aa=False)

max_samples = pylab.amax([len(b_n), len(g_n), len(r_n)])
max_density = pylab.amax([b_n.max(), g_n.max(), r_n.max()])
pylab.imshow(im, interpolation='bilinear', extent=[0,max_samples,0,max_density])

pylab.axis('tight')
axes = pylab.gca()
axes.get_xaxis().set_ticks([])
axes.get_yaxis().set_ticks([])
pylab.xlabel('Saturation (0-1)')
pylab.ylabel('Density')

pylab.title('Color Density Analysis of %s' % os.path.basename(file_path))
pylab.show()

