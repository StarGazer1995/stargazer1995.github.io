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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVULWB5F%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T205926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQgzJINU4YryOZRmlkyCgRV9elbC%2BR3Nx%2F3y%2BewiFgwQIgeh8j%2BXIvbnRStOSUV%2B65oLmanj2yD%2FpWCAF1GgQjQ64qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH5AKZRNkOA3U714vCrcA8pu%2FLQwEvxryzr%2FqfjziUWpL%2BURWxjlhru8CY3p%2Bvv4KOtOVWosHOaSdGKISadWOfcYdBDgvsYQX1z612LUGLBjouJzU6cPJ4G5PHMW71WcSi7RbFJhAGj4Pv6fGw3GILKc7rObYvx8mFb1JGw1Bf9QJPdpE2gdwX9uFAiu2UjMyJhqsVU9i8ZmQbDK2EVct57mC4csmiq8LApL0jahSiyReF19xUxLSIbY1SuEJ0OrPc%2BCV9xU2ezTnO9U0ovaGz3kMabEr%2F50896ASgb%2FE%2BHEZxE9JxKljqYiVNPweO11xVI3fClvd5xKaZ5gjZAnfGHB0bORaFbVPZVUnAWKlH0pEIAE1jIyAvFf0x2ln6G1SXAysYsKnCZokMlkXGdePUb6jBgfw9baiZD0OC%2B1G7Oal7giDn92PkJ5R3zml5Gd7bBLyVL6kk%2Fhw1DXRlDE5Veutt2wnSaEaATyIXzNgXnSfC0HzbGAyw7ieN%2F8IaBXohoYjVrhiYJXjNGi%2BW6K3pzyHPmnTNZALfs6IWd24ITS2D7cyURxuJolX1Mmb8NtqXvwrDtPoSInEHA1S4zV04aKcu5OYFTUvloh%2BpzSe1lB5EjIAOoNMe0motUr9uY6yOkTbCm91qnbktw2MISO%2BtIGOqUBh1SQ0%2FAzhnA4g59rM3HghT%2FhLW8fgAVzm%2FyQJvnWmnPadzhlwxiC3y488U1ZoNIkJTRyE81ptYZE6XR2rmIrwN9snZ%2BYsodIMcnBsSPtjVCBFb%2FBw0enPfUlNeLI%2Fb96aIhdg5MzkHJtg%2F9MkigyRNSskROaL%2B5jMSwJNoyksgEcyGFt%2Bw0q86ADnFu9QBMDB5C5L%2B68KsJ%2Bb8J%2BCzECVZbeJHrf&X-Amz-Signature=8ef1923626c65a3ed0e2c1af94fc1fda27fc434e84ee473ba20ddaa5ed1cfb4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVULWB5F%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T205926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQgzJINU4YryOZRmlkyCgRV9elbC%2BR3Nx%2F3y%2BewiFgwQIgeh8j%2BXIvbnRStOSUV%2B65oLmanj2yD%2FpWCAF1GgQjQ64qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH5AKZRNkOA3U714vCrcA8pu%2FLQwEvxryzr%2FqfjziUWpL%2BURWxjlhru8CY3p%2Bvv4KOtOVWosHOaSdGKISadWOfcYdBDgvsYQX1z612LUGLBjouJzU6cPJ4G5PHMW71WcSi7RbFJhAGj4Pv6fGw3GILKc7rObYvx8mFb1JGw1Bf9QJPdpE2gdwX9uFAiu2UjMyJhqsVU9i8ZmQbDK2EVct57mC4csmiq8LApL0jahSiyReF19xUxLSIbY1SuEJ0OrPc%2BCV9xU2ezTnO9U0ovaGz3kMabEr%2F50896ASgb%2FE%2BHEZxE9JxKljqYiVNPweO11xVI3fClvd5xKaZ5gjZAnfGHB0bORaFbVPZVUnAWKlH0pEIAE1jIyAvFf0x2ln6G1SXAysYsKnCZokMlkXGdePUb6jBgfw9baiZD0OC%2B1G7Oal7giDn92PkJ5R3zml5Gd7bBLyVL6kk%2Fhw1DXRlDE5Veutt2wnSaEaATyIXzNgXnSfC0HzbGAyw7ieN%2F8IaBXohoYjVrhiYJXjNGi%2BW6K3pzyHPmnTNZALfs6IWd24ITS2D7cyURxuJolX1Mmb8NtqXvwrDtPoSInEHA1S4zV04aKcu5OYFTUvloh%2BpzSe1lB5EjIAOoNMe0motUr9uY6yOkTbCm91qnbktw2MISO%2BtIGOqUBh1SQ0%2FAzhnA4g59rM3HghT%2FhLW8fgAVzm%2FyQJvnWmnPadzhlwxiC3y488U1ZoNIkJTRyE81ptYZE6XR2rmIrwN9snZ%2BYsodIMcnBsSPtjVCBFb%2FBw0enPfUlNeLI%2Fb96aIhdg5MzkHJtg%2F9MkigyRNSskROaL%2B5jMSwJNoyksgEcyGFt%2Bw0q86ADnFu9QBMDB5C5L%2B68KsJ%2Bb8J%2BCzECVZbeJHrf&X-Amz-Signature=0bb0f166fbf8cd29fc5f6e8a9035ee98cbb61ed2802c99c58fa5ecb7b645148c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
