"""
create by LYL
2022.4.20
Team 19
members: 郎逸霖, 谭奕, 冯丽萍, 张艳婷, 谢方昕 
使用: 运行 GUI_Team19_work2.0.py 即可
"""

"""
问题说明：
# tri_func 的逻辑是获取整个计算式，并用数组形式存储在 temp 变量中
# 在按键 "=" 按下时，处理模块 caculator 将整个计算式按照计算的优先级分离并计算最终结果
"""

"""
修改 UI 过程 & 说明：
# 需要给处理模块传输一个数组 Temp ，包含用户的输入式，调用方式 res = caculator.caculator(Temp)
# 另外本组自身UI里不包含反三角函数，因此不会触发 arcsin 等处理方法
"""

"""
优化说明：
# 继续引用原代码对错误的处理方式（见错误类型说明）
# 优化了计算结果缓存，"L" 键可调出上次计算结果用于本次运算
# 优化了连续计算场景下的应用，不再需要清零以开启下次运算
"""

"""
错误类型说明：
（通过对处理过程代码的阅读与理解，在输入为异常的计算式时，会返回出错提示，因此不在增加对错误的额外说明）
"""

"""
2.0修复说明：
# 修复了关于第一次开启计算器时第一个数字默认为0，会出现输入 "123" 显示为 "0123" 的问题
# 修复了计算完再次输入数字，前次的结果不会消失的问题
# 修复了存储上次计算结果无法在后续计算中调用的问题
# 修复了计算完成会弹出对话框的问题
"""