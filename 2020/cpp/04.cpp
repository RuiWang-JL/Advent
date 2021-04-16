#include <iostream>
#include <sstream>
#include <fstream>
#include <chrono>
#include <vector>
#include <regex>
#include <boost/algorithm/string.hpp>

int str_to_num(std::string str)
{
    int num{0};
    std::stringstream sstr(str);
    sstr >> num;
    return num;
}

bool in_range(int input, int low, int high)
{
    return (input >= low && input <= high);
}

bool str_in_range(std::string str, int low, int high)
{
    int num = str_to_num(str);
    return in_range(num, low, high);
}

int main()
{
    auto begin = std::chrono::high_resolution_clock::now();

    std::ifstream input("04.txt");
    std::string line;
    int cnt_7_fields{0};
    int cnt_7_valid{0};
    int count1{0};
    int count2{0};
    while (std::getline(input, line))
    {
        if (line.length() > 0)
        {
            std::string fields;
            std::vector<std::string> strs;
            boost::split(strs, line, boost::is_any_of(" "));
            for (auto itr : strs)
            {
                std::string field = itr.substr(0, 3);
                std::string value = itr.substr(4);
                if (field != "cid")
                {
                    cnt_7_fields++;
                    if (field == "byr" && str_in_range(value, 1920, 2002) ||
                        field == "iyr" && str_in_range(value, 2010, 2020) ||
                        field == "eyr" && str_in_range(value, 2020, 2030))
                    {
                        cnt_7_valid++;
                    }
                    else if (field == "hgt")
                    {
                        std::string unit{""};
                        int height{0};
                        std::stringstream svalue(value);
                        svalue >> height >> unit;
                        if ("cm" == unit && in_range(height, 150, 193) ||
                            "in" == unit && in_range(height, 59, 76))
                            cnt_7_valid++;
                    }
                    else if (field == "hcl")
                    {
                        if (std::regex_search(value, std::regex("#([0-9]|[a-f]){6}")))
                            cnt_7_valid++;
                    }
                    else if (field == "ecl")
                    {
                        if (std::regex_search(value, std::regex("^(amb|blu|brn|gry|grn|hzl|oth)$")))
                            cnt_7_valid++;
                    }
                    else if (field == "pid")
                    {
                        if (std::regex_search(value, std::regex("^([0-9]){9}$")))
                            cnt_7_valid++;
                    }
                }
            }
        }
        else
        {
            if (cnt_7_fields == 7)
                count1++;
            if (cnt_7_valid == 7)
                count2++;
            cnt_7_fields = 0;
            cnt_7_valid = 0;
        }
    }
    input.close();

    std::cout
        << "part1: " << count1 << std::endl;

    std::cout << "part2: " << count2 << std::endl;

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("Time measured: %f ms. \n", elapsed.count() * 1e-6);

    return 0;
}