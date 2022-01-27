#include <iostream>
#include <fstream> 
#include <string.h>

int main() {

    int left,right;
    std::string myText;
    std::ifstream MyReadFile("../input.txt");

    while (getline(MyReadFile, myText)) {
        for (int i = 0;  i < myText.length();  i++){
            if( myText[i] == '('){
                left++;
            }
            else{
                right++;
            }
        }
    };

    std::cout << left - right;

    MyReadFile.close(); 
} 