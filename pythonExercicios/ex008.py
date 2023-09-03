medida = float(input('Quantos metro tem: '))
km = medida / 1000
het = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('As medidas são: {}km {}het {}dam {:.0f}m {:.0f}dm {:.0f}cm {:.0f}mm'.format(km, het, dam, medida, dm, cm, mm))

#  n1 = float(input('Quantos metro tem: '))
#  print('M = {} \nCM = {} \nMM = {}'.format(n1, n1 * 100, n1 * 1000))
