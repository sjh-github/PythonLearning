# Python中使用队列
# 导入模块
import queue

q = queue.Queue()
q.put("元素1")
q.put(2)
q.put(True)

print(q.get())
