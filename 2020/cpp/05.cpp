#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
#include <math.h>
#include <numeric>
#include <algorithm>

int main()
{
    auto begin = std::chrono::high_resolution_clock::now();

    std::ifstream input("05.txt");
    std::string line;
    int count1{0};
    std::vector<int> seat;
    while (std::getline(input, line))
    {
        int sum{0};
        std::vector<char> v(line.begin(), line.end());
        for (size_t i = 0; i < v.size(); ++i)
        {
            if (v[i] == 'B' || v[i] == 'R')
            {
                sum += pow(2, 9 - i);
            }
        }
        if (sum > count1)
            count1 = sum;
        seat.push_back(sum);
    }
    input.close();

    int count2{0};
    //std::sort(seat.begin(), seat.end());
    int min = *std::min_element(seat.begin(), seat.end());
    int max = *std::max_element(seat.begin(), seat.end());
    for (int i = min; i < max; ++i)
    {
        if (!(std::find(seat.begin(), seat.end(), i) != seat.end()))
        {
            count2 = i;
            break;
        }
    }
    std::cout
        << "part1: " << count1 << std::endl;

    std::cout << "part2: " << count2 << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("Time measured: %f ms. \n", elapsed.count() * 1e-6);

    return 0;
}