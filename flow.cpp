#include <iostream>
#include <functional>
#include <list>
using namespace std;


namespace{string t="\n\t";}

template <typename T>
class Flow{
    public:
        T data;
        list<function<void(T)>> tunnel;
        
        Flow(T fT) : data(fT){}
        
        void update(function<T(T)> uF){
            this->data = uF(this->data);
            for(auto &tls : this->tunnel){
                tls(this->data);
            }
        }
        
        void collect(function<void(T)> cF){
            cF(this->data);
            this->tunnel.push_back(cF);
        }
};
        
int main(){
   Flow<int> flow(10);
    //void (*live)(int)
    function<void(int)> live=[](int y){
        cout<<t<<"Activetl Data: "<<y;
    };
    
    function<void(int)> mod = [&flow](int y){
        function<int(int)> mody=[y](int x){
            return y;   
        };
        flow.update(mody);
    };
    
    flow.collect(live);
    mod(20);
    mod(30);
    cout<<endl;
    return 0;
}
