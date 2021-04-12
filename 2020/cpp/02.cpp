#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
#include <algorithm>

int main()
{
    auto begin = std::chrono::high_resolution_clock::now();

    std::fstream infile("02.txt", std::fstream::in);

    int least{0}, most{0}, count1{0}, count2{0};
    char target{}, x{};
    std::string password;

    while (infile >> least >> x >> most >> target >> x >> password)
    {
        int times;
        times = std::count(password.begin(), password.end(), target);
        if (times <= most && times >= least)
        {
            count1++;
        }
        if (password[least - 1] == target && password[most - 1] != target ||
            password[least - 1] != target && password[most - 1] == target)
        {
            count2++;
        }
    }

    infile.close();
    std::cout << "part1: " << count1 << std::endl;
    std::cout << "part2: " << count2 << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("Time measured: %f ms. \n", elapsed.count() * 1e-6);

    return 0;
}