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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W42TWSKW%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T225920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQCkuL99EWAWKHg90MMcNYrQ%2BNBUSIx6esZUUGuK9po4vwIhALxAzhOSWMsrTQQz%2FaYPfFNmUNhkg24x7Wo7%2BvTRiiCEKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0MtIBHnmNgPM9L70q3APpu6aSE1TOMgXZ4jEtflMvkWfd80ImepLZSFFNG5CKVBdFt9Agw%2FCLGDPlBtrtNpHM1NWWeVL5er0qprHYalLj82sdnGJZZujy3kU7JvJhAZEM1zFy2Lm8VsIMPK%2BA0vNLONuVmYVvYWIIGDywMxLOn5vMZbImV%2BSPpLEexJIMs31pMtoxvHYlHEnY0ruob1GuGT4NDoiJxkRZT4Wz5nUfi1pRUbZGVQEbhY9Rr4CuVt2F%2BL6fhNHf7nOyW%2B96htYselEysX%2FEs08H0PF2%2BYDG8xscGPtswgyQqQM8sDhlV16uOA1hfjQqnSiw7DW%2BiPM%2FebsLsj4kTV5sIvD%2FA92TpbEeg740EjCcNzeXLt%2FUTr8bIdnSBd%2BKobvTkYc9zvvb8%2FEejaJH0pEeGSVUXX6rcA%2Fu63OBqR5rvZX4Zk6rUXDcYiOOHstVpw36ks9E%2FUv%2FcEHDo2mke1n40HUqPfl5iIIa7Z56jYdOTQ9Ne3XK7gPOKxwf8JKM5KdDrU67Y2ydJnDhZgHiAadkloWwZK6US9vBSyv34cgjgevLyTUNoVZjnKmq6bYZ7s1oM%2FufEwFmlSOT9eKCW%2F10Hi0QL4BiTIsA9I%2BQHPOzrfIOTFsg1BrHgLy9l4wFi28Q3zCDhOHRBjqkAceejIBU5J5qQQANLvmLPjAR7zwMwXpagX%2BfvYLbIqUCtomxhhtvC7NaCrG575stn0UQh8M%2BgzB5OdQqBui1S7AFluBegJEcpYWqBCXucGdyoGf6c7TrvJbivKCalaePetdG32neC1t6VZ5B5AQDPJpNJLslcOK7P6Vk77zh2yxEGtCrJYWAASTzMogo%2FaE0dBOUd%2FTh8CwaPwE5G%2F36UOWcjzhw&X-Amz-Signature=e1b4c8009890569f909e3fbe7bd9360a7eefb6f304efe62e3f2c7a55b4ee07cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W42TWSKW%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T225920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQCkuL99EWAWKHg90MMcNYrQ%2BNBUSIx6esZUUGuK9po4vwIhALxAzhOSWMsrTQQz%2FaYPfFNmUNhkg24x7Wo7%2BvTRiiCEKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0MtIBHnmNgPM9L70q3APpu6aSE1TOMgXZ4jEtflMvkWfd80ImepLZSFFNG5CKVBdFt9Agw%2FCLGDPlBtrtNpHM1NWWeVL5er0qprHYalLj82sdnGJZZujy3kU7JvJhAZEM1zFy2Lm8VsIMPK%2BA0vNLONuVmYVvYWIIGDywMxLOn5vMZbImV%2BSPpLEexJIMs31pMtoxvHYlHEnY0ruob1GuGT4NDoiJxkRZT4Wz5nUfi1pRUbZGVQEbhY9Rr4CuVt2F%2BL6fhNHf7nOyW%2B96htYselEysX%2FEs08H0PF2%2BYDG8xscGPtswgyQqQM8sDhlV16uOA1hfjQqnSiw7DW%2BiPM%2FebsLsj4kTV5sIvD%2FA92TpbEeg740EjCcNzeXLt%2FUTr8bIdnSBd%2BKobvTkYc9zvvb8%2FEejaJH0pEeGSVUXX6rcA%2Fu63OBqR5rvZX4Zk6rUXDcYiOOHstVpw36ks9E%2FUv%2FcEHDo2mke1n40HUqPfl5iIIa7Z56jYdOTQ9Ne3XK7gPOKxwf8JKM5KdDrU67Y2ydJnDhZgHiAadkloWwZK6US9vBSyv34cgjgevLyTUNoVZjnKmq6bYZ7s1oM%2FufEwFmlSOT9eKCW%2F10Hi0QL4BiTIsA9I%2BQHPOzrfIOTFsg1BrHgLy9l4wFi28Q3zCDhOHRBjqkAceejIBU5J5qQQANLvmLPjAR7zwMwXpagX%2BfvYLbIqUCtomxhhtvC7NaCrG575stn0UQh8M%2BgzB5OdQqBui1S7AFluBegJEcpYWqBCXucGdyoGf6c7TrvJbivKCalaePetdG32neC1t6VZ5B5AQDPJpNJLslcOK7P6Vk77zh2yxEGtCrJYWAASTzMogo%2FaE0dBOUd%2FTh8CwaPwE5G%2F36UOWcjzhw&X-Amz-Signature=ecd5950f3c58ad1f31f5d32434c940a11ffc090108d82eba1d69054b7885a5df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
