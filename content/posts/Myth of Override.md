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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA34LUU7%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T114343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDAk2%2BdYmIVgpVTYjLsVPzL140LwfqA02eF%2FkhujeN2FAiEAj%2FJtE0Yg%2BhKvjN2PJJxZ4WSjffHo%2BUeDTSNJmGez3Dkq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDD0fEYF8d7InqYqf4ircA3ZEBifhnz%2BK79XvOFlZQ46r6s5t%2BC389TwriTTEWBxBgYPSnsa9dOlI08BP4QfplThbc%2FiDP7Ihx229ReZnquR7%2FX5HJvSiAfDPwF0oNoA4oG5e9PPAh6utavFKSlEWUhXw8rk3L1CBt8hk%2F9nksCJHXCxQITf22oKvLHX5S2NDcLmhohDLNXPeFJlhV%2B0bUoON6rw4vHpyluwhAAGK274ShhB8ADakFw8Zq9QcRXhM5YBkJpTv3pZ4xI%2B%2FqWO79ALty4YiKDJdFH3Nx6YqskixKA5%2F2SAKV21P131yt7AzDvlDJrr7gQ4OfVaCA2huWSWiyblIMhlZYf%2FQHjBagLFMja4G%2BaVFsVyjP7sGeNFJIp%2FdapZHIQaM9BmYuG7TubbvxOTsbDNketXD4boMK8AFS9%2FVlmi6F17eb%2BMOvSlf3yg8eMDrbhVHY7qv496mQSI7bedBpYchoUMFnhBZGXB5gubyhDm2L%2FUnaOFHZ8tfsDD9ME7mSbEuvnIB7T1oTByhrxweZLcFeHdqAb%2B3HHJH9QOlxzPwFn7xlTU1AezUjaw7u2CIda6aeVvjXojLYJttgPAgbMXcfXGAKz%2Byyc7CBE9LYcsPOxSfeq4pv2%2B2uK88NTq6WYxehcWfMI3WltAGOqUBJ5Y5v4j1sOKeZ8XSBIwAnEZi740zW9GB0Y7FDBAKehC%2BnXzE4XmkjNcB3BwFZ4VubFP0IMWNIXgKh%2FdgFNRPpf0ikIcSNLSMqjZJaMY9ndNOq%2FcF%2Fp5tdvR23cQVhn%2F6xqcYiCkpZRpgj382cQdSZSh8ZEPiTMfw%2FAWHYq%2FPTBS4rt4sXpCk76C3yhCP3O6jAXKVqRrVn9zSb%2FOJNelJYdlDY8cy&X-Amz-Signature=f1bd2dd211adc41994c0833d7a683573797887506b0d2a2cb0ac3abcc53743ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA34LUU7%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T114343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDAk2%2BdYmIVgpVTYjLsVPzL140LwfqA02eF%2FkhujeN2FAiEAj%2FJtE0Yg%2BhKvjN2PJJxZ4WSjffHo%2BUeDTSNJmGez3Dkq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDD0fEYF8d7InqYqf4ircA3ZEBifhnz%2BK79XvOFlZQ46r6s5t%2BC389TwriTTEWBxBgYPSnsa9dOlI08BP4QfplThbc%2FiDP7Ihx229ReZnquR7%2FX5HJvSiAfDPwF0oNoA4oG5e9PPAh6utavFKSlEWUhXw8rk3L1CBt8hk%2F9nksCJHXCxQITf22oKvLHX5S2NDcLmhohDLNXPeFJlhV%2B0bUoON6rw4vHpyluwhAAGK274ShhB8ADakFw8Zq9QcRXhM5YBkJpTv3pZ4xI%2B%2FqWO79ALty4YiKDJdFH3Nx6YqskixKA5%2F2SAKV21P131yt7AzDvlDJrr7gQ4OfVaCA2huWSWiyblIMhlZYf%2FQHjBagLFMja4G%2BaVFsVyjP7sGeNFJIp%2FdapZHIQaM9BmYuG7TubbvxOTsbDNketXD4boMK8AFS9%2FVlmi6F17eb%2BMOvSlf3yg8eMDrbhVHY7qv496mQSI7bedBpYchoUMFnhBZGXB5gubyhDm2L%2FUnaOFHZ8tfsDD9ME7mSbEuvnIB7T1oTByhrxweZLcFeHdqAb%2B3HHJH9QOlxzPwFn7xlTU1AezUjaw7u2CIda6aeVvjXojLYJttgPAgbMXcfXGAKz%2Byyc7CBE9LYcsPOxSfeq4pv2%2B2uK88NTq6WYxehcWfMI3WltAGOqUBJ5Y5v4j1sOKeZ8XSBIwAnEZi740zW9GB0Y7FDBAKehC%2BnXzE4XmkjNcB3BwFZ4VubFP0IMWNIXgKh%2FdgFNRPpf0ikIcSNLSMqjZJaMY9ndNOq%2FcF%2Fp5tdvR23cQVhn%2F6xqcYiCkpZRpgj382cQdSZSh8ZEPiTMfw%2FAWHYq%2FPTBS4rt4sXpCk76C3yhCP3O6jAXKVqRrVn9zSb%2FOJNelJYdlDY8cy&X-Amz-Signature=c8f552677fa425b80f92b4b7f7ef217da91121968231055c6c7065cf23a4524f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
