#include <iostream>
#include <fstream>
#include <chrono>
#include <unordered_set>

void print(std::unordered_set<int> const &s)
{
    for (auto const &i : s)
    {
        std::cout << i << " ";
    }
}

int main()
{
    auto begin = std::chrono::high_resolution_clock::now();

    std::ifstream input{"01.txt"};
    if (!input)
    {
        std::cout << "Can not open file 01.txt";
        return 1;
    }

    bool found = false;
    std::string number;
    std::unordered_set<int> numbers = {};

    while (std::getline(input, number))
    {
        numbers.insert(std::stoi(number));
    }

    input.close();

    // Part one
    for (int x : numbers)
    {
        for (int xx : numbers)
        {
            if (x + xx == 2020)
            {
                std::cout << "Part one: " << x * xx << "\n";
                found = true;
                break;
            }
        }
        if (found)
            break;
    }

    // Part two
    bool found2 = false;

    for (int x : numbers)
    {
        for (int xx : numbers)
        {
            for (int xxx : numbers)
            {
                if (x + xx + xxx == 2020)
                {
                    std::cout << "Part two: " << x * xx * xxx << "\n";
                    found2 = true;
                    break;
                }
            }
            if (found2)
                break;
        }
        if (found2)
            break;
    }

    //print(numbers);

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("Time measured: %f seconds.\n", elapsed.count() * 1e-9);
    return 0;
}