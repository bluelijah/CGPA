#include <iostream>
#include <random>
#include <algorithm>

using namespace std;

int main(){
    string playerchoice, computerchoice;
    getline(cin,playerchoice);
    vector<string> vec = {"rock", "paper", "scissors"};
    random_device rd;
    mt19937 g(rd());
    shuffle(vec.begin(), vec.end(),g);
    string computerchoice = vec.front();g



}