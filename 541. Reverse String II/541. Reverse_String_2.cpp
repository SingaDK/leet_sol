#include <iostream>     // std::cout
#include <algorithm>    // std::reverse
#include <vector>
#include <string>
using namespace std;


 string reverseStr(string s, int k){
        int i=0;
        while(i+k<=s.size()){
                cout<< (s) << "First try";
                cout<<"\n";
                reverse(begin(s)+i,begin(s)+i+k);
                cout<< (s) <<  i << "try" ;
                cout<<"\n";
                i+=2*k;
        }
    cout << (s) << "before final reversal";
    cout<<"\n";
    reverse(begin(s)+i,end(s));
    return s;
    };


 int main()
 {
   string s = "abcdefg";
   string result;
   int k = 2;
   result = reverseStr(s, k);

   cout<< result;
 }

