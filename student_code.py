import math
def shortest_path(M,start,goal):#M中包含了地图中所有的点，start和goal对应intersection和road中的下标或key
    path=[]
    come_from={}#记录父节点
    explored=set()#已搜索过
    frontier={start:0.0}#前沿，用字典表示，value表示前往这个节点的开销，
    mindot=start#开销最小的那个点
    
    while goal not in explored:               
        for i in range(len(M.roads[mindot])):           
            if M.roads[mindot][i] not in explored:
                if M.roads[mindot][i] not in frontier:                    
                    frontier[M.roads[mindot][i]]=frontier[mindot]-distance(mindot,goal,M.intersections)+distance(mindot,M.roads[mindot][i],M.intersections)+distance(M.roads[mindot][i],goal,M.intersections)
                    come_from[M.roads[mindot][i]]=mindot                    
                else:                                       
                    temp=frontier[mindot]-distance(mindot,goal,M.intersections)+distance(mindot,M.roads[mindot][i],M.intersections)+distance(M.roads[mindot][i],goal,M.intersections)
                    if temp<frontier[M.roads[mindot][i]]:
                        frontier[M.roads[mindot][i]]=temp
                        come_from[M.roads[mindot][i]]=mindot
                    
        explored.add(mindot)
        del frontier[mindot]
        mindot=min(frontier,key=frontier.get)#求字典中最小开销的key值        
    temp=[goal]
    while temp[-1]!=start:
        temp.append(come_from[temp[-1]])
    for i in range(len(temp)):
        path.append(temp[len(temp)-1-i])
    print("shortest path called")
    return path
def distance(dota,dotb,listinter):#求两个intersection之间的距离，intersection是字典中的列表
    temp=math.sqrt(math.pow((listinter[dota][0]-listinter[dotb][0]),2)+math.pow((listinter[dota][1]-listinter[dotb][1]),2))
    #print(temp)
    return temp

    
    
    