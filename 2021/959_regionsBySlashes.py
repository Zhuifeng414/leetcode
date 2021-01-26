## 并查集 https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/tu-jie-bing-cha-ji-by-yexiso-nbcz/
# 未改进版本
# 作者：yexiso
# 链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/tu-jie-bing-cha-ji-by-yexiso-nbcz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Djset {
public:
    vector<int> parent;  // 记录节点的根
    Djset(int n): parent(vector<int>(n)) {
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        if (x != parent[x]) return find(parent[x]);
        return parent[x];
    }

    void merge(int x, int y) {
        int rootx = find(x);
        int rooty = find(y);
        parent[rooty] = rootx;
    }
};
'''

# 参数定义
# n：x最大取值
# parent：并查集数组，存储祖先节点
# root：哈希表，存储每个连通区域的根节点

class Solution:
    def removeStones(self, stones):
        n=10
        parent=list(range(2*n))
        # 并查集查找
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        # 合并
        def union(i,j):
            parent[find(i)]=find(j)
        # 连通横纵坐标
        for i,j in stones:
            union(i,j+n)
        # 获取连通区域的根节点
        root=set()
        for i,j in stones:
            root.add(find(i))
            print(i, j)
        return len(stones)-len(root)

if __name__ == '__main__':
    stones = [[0, 1], [0, 5], [0, 3], [2, 1], [6, 4]]
    print(Solution().removeStones(stones))




