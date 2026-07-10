from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) 
        sol = []
        nums.sort()  # O(n log n)
        
        for p in range(0, n - 2):
            # Se il numero fisso è maggiore di 0, non possiamo più fare somma = 0
            if nums[p] > 0:
                break
                
            # Salta i duplicati per il primo elemento
            if p > 0 and nums[p-1] == nums[p]:
                continue

            l, r = p + 1, n - 1
            while l < r:
                current_sum = nums[p] + nums[l] + nums[r]
                
                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    sol.append([nums[p], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # 2. Controllo dei duplicati corretto (l < r messo prima)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Facoltativo ma consigliato: salta i duplicati anche a destra
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return sol