class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    unordered_set<int> found;                 // declared with a type, on the stack (no new)
    for (int i = 0; i < nums.size(); i++) {   // semicolons, not commas
        if (found.count(nums[i])) return true; // seen before -> duplicate
        found.insert(nums[i]);
    }
    return false;                              // must return a bool
    }
};