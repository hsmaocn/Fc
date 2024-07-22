"""
项目名称：分数转换器
版权归属: 返回工作室
使用MIT许可协议
邮箱: i@hmao.top
如有问题欢迎您联系!
您的设备需要装有Python3.6或更高版本
本程序功能已更新，支持分数计算与格式化输出

改进说明：
1. 增加了数据类型检查，确保输入为数字。
2. 优化了输出格式，使结果更加清晰易读。
3. 添加了异常处理，增强程序健壮性。
"""


def calculate_score(full_score, percentage):
    """
    根据满分和正确率计算实际得分。

    参数:
    full_score (float): 满分值
    percentage (float): 正确率，范围0-100

    返回:
    float: 实际得分
    """
    # 确保正确率为0-100之间的数值
    if not 0 <= percentage <= 100:
        raise ValueError("正确率必须在0到100之间")

    # 计算实际得分
    score = full_score * (percentage / 100)
    return round(score, 2)  # 保留两位小数


def main():
    try:
        # 获取用户输入的满分和正确率
        user_full_score = float(input("请输入您所在的地区满分："))
        user_percentage = float(input("请输入正确率(不带'%')："))

        # 计算分数
        user_score = calculate_score(user_full_score, user_percentage)

        # 输出结果
        print(f"根据{user_full_score}分满分和{user_percentage}%的正确率，您的得分约为：{user_score}分")

    except ValueError as e:
        print(f"输入错误：{e}")
    except Exception as e:
        print(f"未知错误：{e}")


if __name__ == "__main__":
    main()
