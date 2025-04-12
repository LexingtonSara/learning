"""1. 算法：解决问题的方法和步骤。"""
# 评价算法的好坏：正确性和效率（渐近时间复杂度、渐近空间复杂度）。
# O(1) 常量时间复杂度：布隆过滤器、哈希表
# O(log n) 对数时间复杂度：二分查找、二叉搜索树
# O(n) 线性时间复杂度：简单排序算法、线性扫描算法、计数排序
# O(n log n) 线性对数时间复杂度：快速排序、归并排序
# O(n^2) 平方时间复杂度：简单选择排序、冒泡排序、插入排序
# O(n^3) 立方时间复杂度：三重循环、Floyd算法、矩阵乘法
# O(2^n) 指数时间复杂度：递归算法、动态规划
# O(n!) 阶乘时间复杂度：全排列、旅行推销员问题

# 1.简单选择排序：
def simple_selection_sort(arr,compare=lambda x,y:x<y):
    arr=arr.copy()
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if compare(arr[j],arr[min_index]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
    #遍历整个数组，每一次遍历该值后面所有的值，记录最小的值的索引，然后交换位置n*(n-1)//2

# 2.冒泡排序：
def bubble_sort(arr,compare=lambda x,y:x<y):
    arr=arr.copy()
    n=len(arr)
    for i in range(n):
        flag=False
        for j in range(n-i-1):
            if compare(arr[j],arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if not flag:
            break
    return arr
    # 与简单选择排序类似，遍历整个数组，每一次遍历该值后面所有的值，如果满足条件则交换位置，将一个最大值/最小值移动到最后面
    # 最坏的情况是需要n*(n-1)//2次交换

# 3.搅拌排序：双向冒泡排序
def shake_sort(arr,compare=lambda x,y:x<y):
    # 冒泡排序升级版
    arr=arr.copy()
    n=len(arr)
    for i in range(n-1):
        flag=False
        for j in range(n-i-1):
            if compare(arr[j],arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if flag:
            flag=False
            for j in range(n-i-2,i,-1):
                if compare(arr[j-1],arr[j]):
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                    flag=True
        if not flag:
            break
    return arr

# 4.归并排序：
def merge(left,right,compare=lambda x,y:x<y):
    # 合并两个有序数组
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if compare(left[i],right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

def merge_sort(arr,compare=lambda x,y:x<y):
    # 递归调用，将数组分成两半，分别排序，然后合并
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid],compare)
    right=merge_sort(arr[mid:],compare)
    return merge(left,right,compare)
    # 时间复杂度：O(nlogn)

# 5.二分查找：
def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
    # 时间复杂度：O(logn)

# 6.计数排序：
def count_sort(arr):
    # 计数排序
    n=max(arr)+1
    m=len(arr)
    count=[0]*n
    for i in arr:
        count[i]+=1

    result=[0]*m
    index=0
    for i in range(1,n):
        while count[i]:
            result[index]=i
            count[i]-=1
            index+=1
    return result
    # 时间复杂度：O(n+k)

# 7.常用算法：
# 7.1 穷举法：暴力破解法，枚举所有可能的解法，找到最优解。
# 7.2 贪心法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最求解，快速找到满意解
# 7.3 分治法：将原问题分解成一些规模较小的相同问题，递归求解这些问题，最后合并其结果得到原问题的解。
# 7.4 动态规划：将复杂问题分解成子问题，利用子问题的解来求解原问题。
# 7.5 回溯法：一种选优搜索法，按选优条件向前搜索，发现解而回溯。

# 7.1 穷举法例子：百钱百鸡问题（公鸡5元一只，母鸡3元一只，小鸡1元三只，用100元买100只鸡，问公鸡、母鸡、小鸡各有多少只？）
for x in range(20):
    for y in range(33):
        z=100-x-y
        if 5*x+3*y+z//3==100 and z%3==0:
            print(x,y,z)
    # 五人分鱼问题
# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
fish=6#E分鱼的时候最少有6条
while True:
    total=fish
    enough=True
    for _ in range(5):#A、B、C、D、E各自分鱼
        if (total-1)%5==0:#如果剩余鱼数可以整除5
            total=(total-1)//5*4
        else:#否则只能捕剩下的鱼
            enough=False
            break
    if enough:
        print(fish)
        break
    fish+=5#尝试下一个数

# 7.2 贪心法例子：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，
# 发现如下表所示的物品。很显然，他不能把所有物品都装进背包，
# 所以必须确定拿走哪些物品，留下哪些物品。
# 电脑 200 20
# 收音机 20 4
# 钟 175 10
# 花瓶 50 2
# 书 10 1
# 油画 90 9
# 如何选择物品，才能使得装入背包的总重量不超过20公斤，且价值总和最大？

class Item:
    def __init__(self,name,weight,price):
        self.name=name
        self.weight=weight
        self.price=price
    
    @property
    def value(self):
        return self.price/self.weight

items=[Item('电脑',200,20),Item('收音机',20,4),
       Item('钟',175,10),Item('花瓶',50,2),
       Item('书',10,1),Item('油画',90,9)]
#按照价值排序，如果价值相同，再按照重量排序
items.sort(key=lambda x:(-x.value,-x.weight))
total_weight=0
total_value=0
max_weight=20
for item in items:
    if total_weight+item.weight<=max_weight:
        total_weight+=item.weight
        total_value+=item.value

print(total_value)

# 7.3 分治法例子：快速排序
def quick_sort(arr,start,end,compare=lambda x,y:x<y):
    if start<end:
        pivot_index=_partition(arr,start,end,compare)
        quick_sort(arr,start,pivot_index-1,compare)
        quick_sort(arr,pivot_index+1,end,compare)
    return arr

def _partition(arr,start,end,compare):
    pivot=arr[end]
    i=start-1
    for j in range(start,end):
        if compare(arr[j],pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1

def quick_sort(arr,start,end,compare=lambda x,y:x<y):
    if start<end:
        pivot_index=_partition(arr,start,end,compare)
        quick_sort(arr,start,pivot_index-1,compare)
        quick_sort(arr,pivot_index+1,end,compare)
    return arr

def _partition(arr,start,end,compare):
    pivot=arr[start]
    while start<end:
        while start<end and compare(arr[end],pivot):
            end-=1
        arr[start]=arr[end]
        while start<end and not compare(arr[start],pivot):
            start+=1
        arr[end]=arr[start]
    arr[start]=pivot
    return start

# 7.4 回溯法例子：八皇后问题
# 7.5 动态规划例子：最长公共子序列问题