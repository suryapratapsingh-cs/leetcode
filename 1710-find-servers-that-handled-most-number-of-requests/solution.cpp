#include <vector>
#include <set>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::vector<int> busiestServers(int k, std::vector<int>& arrival, std::vector<int>& load) {
        std::set<int> available;
        for (int i = 0; i < k; ++i) {
            available.insert(i);
        }

        // Min-heap storing pairs of {free_time, server_id}
        std::priority_queue<std::pair<long long, int>, 
                            std::vector<std::pair<long long, int>>, 
                            std::greater<std::pair<long long, int>>> busy;

        std::vector<int> request_count(k, 0);
        int max_requests = 0;

        for (int i = 0; i < arrival.size(); ++i) {
            long long curr_time = arrival[i];
            long long duration = load[i];

            // Free up servers that have completed their tasks by the current arrival time
            while (!busy.empty() && busy.top().first <= curr_time) {
                available.insert(busy.top().second);
                busy.pop();
            }

            // If no servers are available, drop the request
            if (available.empty()) {
                continue;
            }

            // Find the preferred server using lower_bound
            int target = i % k;
            auto it = available.lower_bound(target);
            if (it == available.end()) {
                it = available.begin(); // Wrap around
            }

            int server_id = *it;
            available.erase(it);

            // Assign the task to the server
            busy.push({curr_time + duration, server_id});
            request_count[server_id]++;
            max_requests = std::max(max_requests, request_count[server_id]);
        }

        // Collect all servers that handled the maximum number of requests
        std::vector<int> result;
        for (int i = 0; i < k; ++i) {
            if (request_count[i] == max_requests) {
                result.push_back(i);
            }
        }

        return result;
    }
};
