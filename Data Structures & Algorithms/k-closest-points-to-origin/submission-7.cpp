class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        sort(points.begin(), points.end(), [](const vector<int> a, const vector<int> b) {
            return (a[0] * a[0] + a[1] * a[1]) < (b[0] * b[0] + b[1] * b[1]);
        });

        for (vector<int> point : points) {
            printf("x: %d, y: %d\n", point[0], point[1]);
        }

        vector<vector<int>>* result = new vector<vector<int>>();
        for (int i = 0; i < k; i++) {
            result->push_back(points[i]);
        }

        return *result;
    }
};
