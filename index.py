'''
项目名称：分数转换器
版权归属:返回工作室
使用MIT许可协议
邮箱:jbzx#return2017.top(用@替换#)
如有问题欢迎您联系!
您的设备需要装有Python3.6或更高版本
本程序功能尚未完全实现
'''

#获取您的当地满分和正确率数据
user_full_score = float(input("请输入您所在的地区满分："))
user_percentage = float(input("请输入正确率(不带'%')："))
#分数计算器核心算法，满分*正确率=分数线上的分
user_fraction_calculator_algorithm = user_full_score * (user_percentage)
print("当前总分约为：" + str(user_fraction_calculator_algorithm))