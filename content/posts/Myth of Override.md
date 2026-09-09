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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WRGMEM%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T065053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF%2BFNHucxZUnenSjblubbC4bKP4M4f3Eci7edQxqJjVwIgXEimtX41fVNLNAevL%2FXsZI7WttoQFBat4BWD7sR0PKkq%2FwMIZxAAGgw2Mzc0MjMxODM4MDUiDOeV1A6%2FSGE5b9fTPCrcAxfg1koE5ebcZ9qI%2B3xGghUQ7TXHM3uc1Frf%2B2IeVzzh3gQjnt3xo0XzWa3DNzcri8Sf4ctPPfqhTAe7Rs0L7RwcYupV4oi4mVT3Pqzt6fhshzhmG3BxYA0KU4l5xANN3OMvpqIUqTsMrBy4H%2BdsFWpsO2HTD2ZL%2FksS4C3tB%2FdEOtXji3Q1Lr%2FZaS%2BxKc9YWj5WFCgVUPNpBrN8Sij6gUsc5o8NTebpp7m47%2Bcce4YtTcahADeDko7fqNsHBt5uWpE%2BpRB%2FlkiSXyogaQHGmod3v8k6tYGZKjDwg25TDcBjP6DGVc1QnnCsemvL19zVuVyerr4kEIp6bUg8k5hYCfLlyGfcl8%2F3yCvwCSekWXwy1DAjvodCtgOJ1CyaPdbEeYPhxdrVSqqC7%2B99vrm%2BRd548tVQTUgCw5Aky5Uia0q7kQ1v036SwQIS4eqfp%2BLSdqaMWl4rk46CsxSFVyUB7VPWXvxXyyd9SQYSkZ0eFnnGeTNzMVAOKizjbt%2BqKWXdT4ERlUV6b6m%2FSbxeq%2B9DLVDJcG5ucN054FjLLmIgMfMth%2FIsK8OH9sUMFYg8OV7m%2B%2F2JO30Mawb%2BZuh5WM6mSxqXOiIYidFlf5DijtJwejy%2F975FM6JwJ6oTkyolMP%2Fug9UGOqUBocc%2FKfp%2FlMJobvCDGhphBY6brHj89kp8qWzRjHaaBI04tj%2FqvFT8xdhDtDUooXhTEL%2BT04TAGBjrmmmsZOwxsx57Iq1FUhEf1ObSnBNwC2fwHHTXe568if3zbpng7MhiqgHdGEfwNjy3CX%2Fx3ypf5een0wzkyo%2FtoyU7f8ioiAFp5j5k22VQ6mfbH%2BcrGA6Xh1sDtM9DsMjxTMJ%2FnhoMGmHh4r87&X-Amz-Signature=4ebee6bee5025b864cf3022f328a1681979ee518c2d274d72ebe5d55a726e0ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WRGMEM%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T065053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF%2BFNHucxZUnenSjblubbC4bKP4M4f3Eci7edQxqJjVwIgXEimtX41fVNLNAevL%2FXsZI7WttoQFBat4BWD7sR0PKkq%2FwMIZxAAGgw2Mzc0MjMxODM4MDUiDOeV1A6%2FSGE5b9fTPCrcAxfg1koE5ebcZ9qI%2B3xGghUQ7TXHM3uc1Frf%2B2IeVzzh3gQjnt3xo0XzWa3DNzcri8Sf4ctPPfqhTAe7Rs0L7RwcYupV4oi4mVT3Pqzt6fhshzhmG3BxYA0KU4l5xANN3OMvpqIUqTsMrBy4H%2BdsFWpsO2HTD2ZL%2FksS4C3tB%2FdEOtXji3Q1Lr%2FZaS%2BxKc9YWj5WFCgVUPNpBrN8Sij6gUsc5o8NTebpp7m47%2Bcce4YtTcahADeDko7fqNsHBt5uWpE%2BpRB%2FlkiSXyogaQHGmod3v8k6tYGZKjDwg25TDcBjP6DGVc1QnnCsemvL19zVuVyerr4kEIp6bUg8k5hYCfLlyGfcl8%2F3yCvwCSekWXwy1DAjvodCtgOJ1CyaPdbEeYPhxdrVSqqC7%2B99vrm%2BRd548tVQTUgCw5Aky5Uia0q7kQ1v036SwQIS4eqfp%2BLSdqaMWl4rk46CsxSFVyUB7VPWXvxXyyd9SQYSkZ0eFnnGeTNzMVAOKizjbt%2BqKWXdT4ERlUV6b6m%2FSbxeq%2B9DLVDJcG5ucN054FjLLmIgMfMth%2FIsK8OH9sUMFYg8OV7m%2B%2F2JO30Mawb%2BZuh5WM6mSxqXOiIYidFlf5DijtJwejy%2F975FM6JwJ6oTkyolMP%2Fug9UGOqUBocc%2FKfp%2FlMJobvCDGhphBY6brHj89kp8qWzRjHaaBI04tj%2FqvFT8xdhDtDUooXhTEL%2BT04TAGBjrmmmsZOwxsx57Iq1FUhEf1ObSnBNwC2fwHHTXe568if3zbpng7MhiqgHdGEfwNjy3CX%2Fx3ypf5een0wzkyo%2FtoyU7f8ioiAFp5j5k22VQ6mfbH%2BcrGA6Xh1sDtM9DsMjxTMJ%2FnhoMGmHh4r87&X-Amz-Signature=75e60e78aed1eb9f720c14d2196aa703aef1aeecbdc61d1007063a9299091994&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
