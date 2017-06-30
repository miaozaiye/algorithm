# 这是冒泡排序算法的python 实现 by Jane@proginn.com
# bubble 的原理，是将相邻两个数字做对比，将大的排在后面；这样每轮排下来，最后一个总是最大的；下一轮，则只用排前 n-1 个，直到 n==1。
'''
>>>bubble.py 3,6,7,2,15

2,3,6,7,15

'''

List = [1,2,3,4,5]
def bubble(List):
    l = len(List)
    l2 = l

    for count in range(l):
        print (l,l2)
        for index in range(l2):
            print (l,l2,index)
            if index == l2-1:
                pass
            else:
                temp = List[index]
                if List[index] > List[index + 1]:
                    print (l,l2,index)
                    List[index] = List[index+1]
                    List[index+1] = temp
        l2 = l2-1


    return List

print (bubble(List))