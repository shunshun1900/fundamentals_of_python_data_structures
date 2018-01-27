import math

r = float(input('请输入球体的半径:\n'))
dia = 2 * r  # 球体直径
perimeter = 2 * math.pi * r  # 球体圆周长
s = 4 * math.pi * r * r  # 球体表面积
v = (4 / 3) * math.pi * (r**3)


print('球体直径为%.3f' % dia)
print('球体圆周长%.3f' % perimeter)
print('球体表面积%.3f' % s)
print('球体体积%.3f' % v)
