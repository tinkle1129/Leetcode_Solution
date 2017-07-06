class Solution(object):
    def back(self,a,t,s):
        if len(a)==1:
            return s+str(a[0])
        start=0;end=len(a)-1
        x=len(a)-1;quad=1
        while(x):
            quad=quad*x
            x=x-1
        while(True):
            mid=(end-start)/2+start
            tmp=mid*quad
            if end-start>1:
                if tmp<(t-1):
                    start=mid
                elif tmp>(t-1):
                    end=mid
                else:
                    s=s+str(a[mid])
                    a.remove(a[mid])
                    for i in a:
                        s=s+str(i)
                    return s
            else:
                flag=start
                tmp=start*quad
                if end*quad<=(t-1):
                    flag=end
                    tmp=end*quad
                s=s+str(a[flag])
                a.remove(a[flag])
                s=self.back(a,(t)-tmp,s)
                return s
    def getPermutation_(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s=''
        a=[i for i in range(1,n+1)]
        t=k
        s=self.back(a,t,s)
        return s

    def getPermutation(self,n,k):
        #print n,k
        ans = [i for i in range(1,n+1)]
        cnt = 0
        ret = ''
        while(cnt<n):
            in_cnt = len(ans)-1
            inner_count = 1
            while(in_cnt>1):
                inner_count = in_cnt*inner_count
                in_cnt -=1
            for j in range(1,len(ans)+1):
                if k<=j*inner_count:
                    break
            ret+=str(ans[j-1])
            k = k-(j-1)*inner_count
            ans.remove(ans[j-1])
            cnt+=1
        return ret

S= Solution()
print S.getPermutation(1,1)
print S.getPermutation(3,4)