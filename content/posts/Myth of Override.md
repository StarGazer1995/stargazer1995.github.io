---
created: 2024-07-04T01:57:00+00:00
categories:
  - Blog
tags:
  - Problems
  - Blog
updated: 2024-07-04T02:13:00+00:00
date: 2024-07-04T01:57:00+00:00
title: Myth of Override
cover: https://app.notion.com/images/page-cover/webb1.jpg
id: 6e79f44c-5df9-46d3-bbec-45dc2f724d70
---

# Introduction:

Recently, while acquainting myself with the new company, I encountered a piece of unusual code.

It seems quite straightforward. We start by declaring a base class with a private virtual function, which is then called by a public member function. Next, we derive a class from the base class and override the virtual function. This pattern is known as the Template Pattern. It defines the skeleton of an algorithm but allows subclasses to override specific steps without altering its structure. The code appears sound until we scrutinize the derived class.

```c++
#include<iostream>
#include<memory>

class base {
public:
    base() = default;
    void callPrivateFunction(){
        privateFunction();
    }
private:
    virtual void privateFunction(){
        std::cout<<"The call comes from a private function"<<std::endl;
    }
};

class derived : public base {
public:
    void privateFunction() override {
        std::cout<<"The cal comes from the overrided function"<<std::endl;
    }
};

int main(){
    base *ptr = new derived();
    ptr->callPrivateFunction();

    derived *ptr_derived = new derived();
    ptr_derived->privateFunction();
    return 0;
}
```

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">github.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp</div></div></div></a></div></div>

My initial thought was, 'How can we override a private virtual function? It wouldn't pass the compilation test.' However, I was surprised by the real compiler's response: PASS.

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQZBXS2V%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T020103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPEIBwL1%2F4a73WY5VW2qLuIf%2Fe%2BASPlmzRs9CNqW1%2BEQIgQEj7iS0Pqk9ZNbn2EYGIXpPsR%2BB7ItSYWMAuIIObwY0q%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDJAOQ8QN3njMO5uUFircA04QDRattSqgpsm8A6DsP%2FAmMZ9%2Fy5VCArK2NUtShg4C2S6d5bXz0Is2JrlHBuPtYSm4tuiilCqqrzTX%2B9cF3kk8olO5xKOvJhl6ZhNbdV2Y0zByYuFYr6l0W1c8mIcnwyu7Zumtp4EPoOj150KHWJhXtM3%2FCEg2IDtW0Fa48XLMJ3xOruqe73HXNmWK1yjI90hatcZ%2B28znaQBCWiroxnis%2FJqnVTV0TrIKWWSyik7evHjJ9J3BeQw8lgBn949CDqKtz1yogtGnymGk64H7MNangtes%2BBb5fcGFTidYshln7tUST7TfCFKykL7FCeT50ZIEOL9L28QlYcW2F1flifyoiKRjzMxdAF8%2FXpe4dnqH%2FWBnhI%2BPI9%2BefXtYsgLWB4Hrm5GEtdrNhX6h%2BPzTZXjqbHPaVftjBnXtEaZNC0owRP2FfAYO1P9W7hBacIA%2F6zPPXYZIcm8TJxEb69yK5PTO4BoTw5Aumxa5%2FFXRVDHHRoFmmZ7C40aGqIFIRTELb7vmoAV%2FMNRoivxew0X%2B9CYN3UKnEB1qxIetXdeYVnXKjKbWh7k0JnwVn9Wy9AgcCp1RcyFvL5kwUP1D6qoe8koo4HzVM4FThY6d75v5txRc3gSwa1PrlhiuKgkoMOPRvNUGOqUBX1g3WKH9ZuomDVTH3%2Bhj61quWPviYa80GpXw6y3t1%2F6f9NQCGcDJIG2WhhZdKemLDnt74qSjSYK79wvDKAPZk5ZjfJJWeVsmB7kykdlEOSsH1GlQdXspVv1dDxoLa9pUdKaYSMk2k20Qo38TWQ%2F2oMPj%2Fgbop0WeVuxobTCqQt4I88xrM8yccL4j6HV8cO8sh8qmXov52ljpA7gKCB7%2Br9R28lhI&X-Amz-Signature=de0e7ff350120f161858e00d2d893290119a21794a2038e5baa9b73a6fbf59af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQZBXS2V%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T020103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPEIBwL1%2F4a73WY5VW2qLuIf%2Fe%2BASPlmzRs9CNqW1%2BEQIgQEj7iS0Pqk9ZNbn2EYGIXpPsR%2BB7ItSYWMAuIIObwY0q%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDJAOQ8QN3njMO5uUFircA04QDRattSqgpsm8A6DsP%2FAmMZ9%2Fy5VCArK2NUtShg4C2S6d5bXz0Is2JrlHBuPtYSm4tuiilCqqrzTX%2B9cF3kk8olO5xKOvJhl6ZhNbdV2Y0zByYuFYr6l0W1c8mIcnwyu7Zumtp4EPoOj150KHWJhXtM3%2FCEg2IDtW0Fa48XLMJ3xOruqe73HXNmWK1yjI90hatcZ%2B28znaQBCWiroxnis%2FJqnVTV0TrIKWWSyik7evHjJ9J3BeQw8lgBn949CDqKtz1yogtGnymGk64H7MNangtes%2BBb5fcGFTidYshln7tUST7TfCFKykL7FCeT50ZIEOL9L28QlYcW2F1flifyoiKRjzMxdAF8%2FXpe4dnqH%2FWBnhI%2BPI9%2BefXtYsgLWB4Hrm5GEtdrNhX6h%2BPzTZXjqbHPaVftjBnXtEaZNC0owRP2FfAYO1P9W7hBacIA%2F6zPPXYZIcm8TJxEb69yK5PTO4BoTw5Aumxa5%2FFXRVDHHRoFmmZ7C40aGqIFIRTELb7vmoAV%2FMNRoivxew0X%2B9CYN3UKnEB1qxIetXdeYVnXKjKbWh7k0JnwVn9Wy9AgcCp1RcyFvL5kwUP1D6qoe8koo4HzVM4FThY6d75v5txRc3gSwa1PrlhiuKgkoMOPRvNUGOqUBX1g3WKH9ZuomDVTH3%2Bhj61quWPviYa80GpXw6y3t1%2F6f9NQCGcDJIG2WhhZdKemLDnt74qSjSYK79wvDKAPZk5ZjfJJWeVsmB7kykdlEOSsH1GlQdXspVv1dDxoLa9pUdKaYSMk2k20Qo38TWQ%2F2oMPj%2Fgbop0WeVuxobTCqQt4I88xrM8yccL4j6HV8cO8sh8qmXov52ljpA7gKCB7%2Br9R28lhI&X-Amz-Signature=ceebe36119aef2c54fb3ed37e9d5a6df04c9557841f963f11ca180aa95c26125&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
