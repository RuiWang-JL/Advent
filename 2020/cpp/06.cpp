#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
#include <math.h>
#include <numeric>
#include <algorithm>
#include <unordered_set>

int main()
{
    auto begin = std::chrono::high_resolution_clock::now();

    std::ifstream input("06.txt");
    std::string line;
    std::array<int, 26> count;
    count.fill(0);
    int ans1{0}, ans2{0}, member{0};

    while (std::getline(input, line))
    {
        if (line.empty())
        {
            for (const auto &i : count)
            {
                if (i > 0)
                    ans1++;
                if (i == member && member != 0)
                    ans2++;
            }
            count.fill(0);
            member = 0;
        }
        else
        {
            for (const auto &i : line)
            {
                count[i - 'a']++;
            }
            member++;
        }
    }

    input.close();

    std::cout << "part1: " << ans1 << std::endl;
    std::cout << "part2: " << ans2 << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("Time measured: %f ms. \n", elapsed.count() * 1e-6);

    return 0;
}