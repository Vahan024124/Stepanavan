#include <iostream>
using namespace std;


int main(){
    int can = 0;
    int tiv; 
    int baj=2;
    cout << " ";
    cin >> tiv;
    while (baj<tiv){
       if(tiv%baj == 0){

        can++;
           cout<<can; 
        }
           
          baj++;
     }
       if(can == 0){
            cout <<" zer tivy parz tiv e";
        }

      else{
        cout<<"zer tivy parz che";
      }



}
