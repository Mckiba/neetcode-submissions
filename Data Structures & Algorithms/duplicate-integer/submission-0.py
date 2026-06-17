class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m_dict = {}
        for num in nums:
            if num in m_dict:
                return True
            m_dict[num] = num
        return False
        
    
    