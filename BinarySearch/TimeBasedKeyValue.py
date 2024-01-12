class TimeMap:

    def __init__(self):
        self.dt = {}
        self.timestamp_prev =""
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dt:
            self.dt[key] =[]
        self.dt[key].append([value, timestamp])    

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dt.get(key,[])
        l = 0
        r = len(values)-1
        while l<=r:
            m = l+(r-l)//2
            if values[m][-1] == timestamp:
                return values[m][0]
            
            if values[m][1]<= timestamp:
                res = values[m][0]
                l=m+1
            else:
                r = m-1

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)



# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
 
