
# coding: utf-8

m = float(input('Informe a medida em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('\n{:.3f} m equivale a: '.format(m))
print('<{:.3f} km>'.format(km))
print('<{:.3f} hm>'.format(hm))
print('<{:.3f} dam>'.format(dam))
print('<{:.3f} cm>'.format(cm))
print('<{:.3f} mm>'.format(mm))
