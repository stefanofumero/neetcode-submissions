class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i] < temperatures[i+1]:
                res[i] = 1
            else:
                counter = 1
                for j in range(i+2,len(temperatures)):
                    counter += 1
                    if temperatures[j] > temperatures[i]:
                        res[i] = counter
                        break
                
        
        return res