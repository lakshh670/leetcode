class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        state=[]
        ans=[]
        for x in asteroids:
            if x<0:
                while state and state[-1]>0 and state[-1]<abs(x):
                    state.pop()
                if not state:
                    ans.append(x)
                if state and state[-1]==abs(x):
                    state.pop()
                
            else:
                state.append(x)
        for x in state:
            ans.append(x)
        return ans
        