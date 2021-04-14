#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
#include <algorithm>

using Map = std::vector<std::vector<char>>;
unsigned count_trees(const Map &map, int dx, int dy) //dx = 3, dy =1
{
    unsigned count{0};
    auto x = map[0].size();
    auto y{map.size()};
    for (int i = 0; i < y / dy; i++)
    {
        auto pos = map[i * dy][(i * dx) % x];
        if (pos == '#')
        {
            count++;
        }
    }
    return count;
}
int main()
{
    auto begin = std::chrono::high_resolution_clock::now();

    std::ifstream input("03.txt");
    std::string line;
    Map map;
    while (std::getline(input, line))
    {
        map.push_back({line.begin(), line.end()});
    }
    input.close();

    int count1{0};
    long long count2{0};
    count1 = count_trees(map, 3, 1);
    count2 = count_trees(map, 1, 1) * count_trees(map, 3, 1) * count_trees(map, 5, 1) * count_trees(map, 7, 1) * count_trees(map, 1, 2);

    std::cout
        << "part1: " << count1 << std::endl;

    std::cout << "part2: " << count2 << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("Time measured: %f ms. \n", elapsed.count() * 1e-6);

    return 0;
}