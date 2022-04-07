# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 20:53:55 2020

@author: MuJS
"""

class Found():#寻路算法
    
    def __count_line(self,gray):#取样确定1/4到3/4区域是否为可观测路径
        high,weight=gray.shape
        white=[0]*4
        black=[0]*4
        count=0
        for i in range(weight):
            if gray[int(high/4)][i]==[0]:
                black[0]+=1
            else:
                white[0]+=1
            if gray[int(high/2)][i]==[0]:
                black[1]+=1
            else:
                white[1]+=1
            if gray[int(high/8*5)][i]==[0]:
                black[2]+=1
            else:
                white[2]+=1
            if gray[int(high/4*3)][i]==[0]:
                black[3]+=1
            else:
                white[3]+=1
        for i in range(4):
            if black[i]>10*white[i]:
                count+=1
        if count>=2:
            return True
        else:
            return False
    
    
    def __count_exchange(self,gray,left,right):#确定某两条直线是否在起点终点区域内
        high,weight=gray.shape
        point_ln,point_ll=0,0
        point_rn,point_rl=0,0
        count_l,count_r=0,0
        for i in range(weight):
            if gray[left][i]!=0:
                point_ln=1
            else:
                point_ln=0
            if gray[right][i]!=0:
                point_rn=1
            else:
                point_rn=0
            if point_ln!=point_ll:
                count_l+=1
                point_ll=point_ln
            if point_rl!=point_rn:
                count_r+=1
                point_rl=point_rn
        left=min(left+3,high-4)
        right=min(right+5,high-2)
        if count_l>=2 and count_r>=2:
            return True
        else:
            return False 
        
        
    def find_angel(self,gray):#寻路算法
        high,weight=gray.shape#记录传入图像高宽
        #记录四个边框上第一个白色像素点和最后一个白像素点的位置，-1为不存在
        U=[-1]*2  
        D=[-1]*2
        L=[-1]*2    
        R=[-1]*2
        i=0
        while i<weight:
            if gray[1][i]!=0:
                U[0]=i
                break
            i+=1
        i=weight-1
        while i>=0:
            if gray[1][i]!=0:
                U[1]=i
                break
            i-=1
        i=0
        while i<weight:
            if gray[high-1][i]!=0:
                D[0]=i
                break
            i+=1
        i=weight-1
        while i>=0:
            if gray[high-1][i]!=0:
                D[1]=i
                break
            i-=1
        i=0
        while i<high:
            if gray[i][1]!=0:
                L[0]=i
                break
            i+=1
        i=high-1
        while i>=0:
            if gray[i][1]!=0:
                L[1]=i
                break
            i-=1
        i=0
        while i<high:
            if gray[i][weight-1]!=0:
                R[0]=i
                break
            i+=1
        i=high-1
        while i>=0:
            if gray[i][weight-1]!=0:
                R[1]=i
                break
            i-=1
        #降噪
        if U[1]-U[0]<0.1*weight:
            U=[-1,-1]
        if D[1]-D[0]<0.1*weight:
            D=[-1,-1]   
        if U!=[-1,-1]:#当上边框存在白色像素点时  
            if D!=[-1,-1]:#当下边框也存在白色像素点时
                if self.__count_line(gray)==True:#用于检测终点（上方白色挡板，下方黑白终点线，中下区域为终点部分墙体，纯黑不可观测） 
                    return 999
                if L!=[-1,-1] and R!=[-1,-1]:#当左右边框也存在像素点时
                    if L[1]>0.8*high and R[1]>0.8*high:#检测前方较远距离是否有起点终点线
                        if self.__count_exchange(gray,L[0],R[0])==True:
                            return 2
                    if U[0]>D[0] and L[0]>R[0] and L[0]>0.1*high and U[0]>0.1*weight:#路径边缘落在左上边框时
                        if gray[int(L[0]/2)][int(U[0]/2)]==0:#路径是否内凹
                            return 15
                        else:
                            return 90
                    if U[1]<D[1] and R[0]>L[0] and R[0]>0.1*high and U[1]<0.9*weight:#路径边缘落在右上边框时
                        if gray[int(R[0]/2)][int((weight-U[1])/2)]==0:#路径是否内凹
                            return -15
                        else:
                            return -90
                    if U[0]<D[0] and L[1]<R[1] and L[1]<0.9*high and R[0]>0.1*weight:#路径边缘落在左下边框时
                        if gray[int((high-L[1])/2)][int(D[0]/2)]==0:#路径是否内凹
                            return -90
                        else:
                            return 15
                    if U[1]>D[1] and L[1]>R[1] and R[1]<0.9*high and R[1]<0.9*weight:#路径边缘落在右下边框时
                        if gray[int((high-R[1])/2)][int((weight-D[1])/2)]==0:#路径是否内凹
                            return 90
                        else:
                            return -15   
                    return 1
                if R==[-1,-1] and L==[-1,-1]:#当左右边框不存在像素点时
                    if U[0]<=0.9*D[0] and U[1]<=0.9*D[1]:#检测路径是否朝左
                        return -15
                    if U[0]>=1.1*D[0] and U[1]>=1.1*D[1]:#检测路径是否朝右
                        return 15
                    if U[0]<=0.9*D[0] and U[1]>=1.1*D[1]:#若左右都有角度
                        if U[1]-D[1]>D[0]-U[0]:#取角度大方向
                            return 15
                        else:
                            return -15
                if L==[-1,-1]:#当只有左边框不存在像素点时
                    if self.__count_line(gray)==True:#用于检测终点前朝向（上方白色挡板，下方黑白终点线，中下区域为终点部分墙体，纯黑不可观测）
                        return 60
                    if U[0]>1.5*D[0]:#根据倾斜程与方向度确定转向角度
                        if gray[int(high/2)][int((U[0]+D[0])/2)]==0:
                            return 60
                        else:
                            return 90
                    if U[0]>=1.1*D[0]:
                        if gray[int(high/2)][int((U[0]+D[0])/2)]==0:
                            return 60
                        else:
                            return 45
                    if U[0]<0.5*D[0]:
                        if gray[int(high/2)][int((U[0]+D[0])/2)]==0:
                            return -90
                        else:
                            return 60
                    if U[0]<=0.9*D[0]:
                        if gray[int(high/2)][int((U[0]+D[0])/2)]==0:
                            return -45
                        else:
                            return 60
                if R==[-1,-1]:#当只有右边框不存在像素点时
                    if self.__count_line(gray)==True:#用于检测终点前朝向（上方白色挡板，下方黑白终点线，中下区域为终点部分墙体，纯黑不可观测）
                        return -60
                    if U[1]>1.5*D[1]:#根据倾斜程度与方向确定转向角度
                        if gray[int(high/2)][int((U[0]+D[0])/2)]==0:
                            return 90
                        else:
                            return -60
                    if U[1]>=1.1*D[1]:
                        if gray[int(high/2)][int((U[0]+D[0])/2)]==0:
                            return 45
                        else:
                            return -60
                    if U[1]<0.5*D[1]:
                        if gray[int(high/2)][int((U[0]+D[0])/2)]==0:
                            return -60
                        else:
                            return -90
                    if U[1]<=0.9*D[1]:
                        if gray[int(high/2)][int((U[0]+D[0])/2)]==0:
                            return -60
                        else:
                            return -45
                return 1#若不满足以上条件，直走           
            if D==[-1,-1]:
                if L[1]>0.3*high and R[1]>0.3*high:#，能看见挡板，看不见终点线时的终点判定             
                    return 999
                return 1#若不满足以上条件，直走（其中包含但不限于路径落在左上/右上的第三种情况）  
        else:#当上边框不存在白色像素点时
            if D==[-1,-1] and L==[-1,-1] and R==[-1,-1]:#如果没有任何可观测路径
                return 60
            if L==[-1,-1]:#路径落在右下的第三种情况
                return 90
            if R==[-1,-1]:#路径落在左下的第三种情况
                return -90
            #当路径落在左右边框上时
            if self.__count_exchange(gray,L[0],R[0])==True:
                return 2
            if L[0]<0.5*R[0]:#路径偏右
                return -90
            if L[0]>1.5*R[0]:#路径偏左
                return 90
            if 0.5*R[0]<=L[0]<=1.5*R[0]:#看不出路径偏向哪里
                if self.__count_exchange(gray,L[0],R[0])==True:#当路径包含终点时
                    return 1
                else:
                    return -361
            return 1#若不满足以上条件，直走  
      
        
    def find_circle(self,gray):#寻圆算法
        high,weight=gray.shape#记录传入图像高宽
        #记录三个边框上第一个黑色像素点和最后一个黑像素点的位置，-1为不存在
        U=[-1]*2  
        L=[-1]*2    
        R=[-1]*2
        i=1
        while i<weight:
            if gray[1][i]==0:
                U[0]=i
                break
            i+=1
        i=weight-1
        while i>=1:
            if gray[1][i]==0:
                U[1]=i
                break
            i-=1
        i=1
        while i<high:
            if gray[i][1]==0:
                L[0]=i
                break
            i+=1
        i=high-1
        while i>=1:
            if gray[i][1]==0:
                L[1]=i
                break
            i-=1
        i=1
        while i<high:
            if gray[i][weight-2]==0:
                R[0]=i
                break
            i+=1
        i=high-1
        while i>=1:
            if gray[i][weight-2]==0:
                R[1]=i
                break
            i-=1
        #机器人一定停在终点前靠右位置
        if U!=[-1,-1] and R!=[-1,-1]:#检测到击打
            return 777
        else:#检测不到一直左横移
            return-361
