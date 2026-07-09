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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X36RFTDE%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T191914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJzyj31CaIpkHo25iFCozDBU5GeCEpx7aND3CmVFl8iwIhAPG9oOKqgf%2BuvDHNx2%2FsQZQYbUX3h6YZjNkj589eenlwKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwlueycwwRRZn5Ks3Iq3ANuEs4F3YGe42%2BZGeBHOykOW8WoBzAvpun9qEQwBbNUe897rfxhiJ6C7qT5pzneLRzb55r3tOMDVxhqMjVSyvH%2BPzkyf%2B88e4JbsXfwRpWNAyfT5Ehi9L%2FimhIMnsJdyXbDrsRGWJH0%2FOBlE7DD9SSRytlI5ifKK%2BXyVWlStlwRYw0n4B%2FyynvvKRjV%2FTCnrIET9jVnklcIHl5yISVC7zK1RRWNP177ndwJhJZMbxJk5R4AYoxllotVztrL%2Bk0Dl6A%2FBhAWEX8cRPazEzDGJcLrg265xUocjUR47D20chnvxUfDQepPHL%2F42hOP7l1SVkS2n2RGdvJw4rzmahP1cbqK3MOLXvaK4bau9S3IprnM9hjkW5yFQaHHuweRP0pjSWm0Mm9%2F4JQf1aF3SDE5u6uVaA9cAYz7tzSljk7pHmVvHoAs%2BslrkvoTxSKkVuBmsyUM8wO9EfCjH75%2FNsfhJVopwNlXfFIJgoFd4g4sIxqT4WOvdVph%2BRzMrR3aj0Y3YNIzxqW%2FalT5uOCjM31KGiGxWNFI1A8sC22kkm2aVzc7F4Kolm5j5mjP4dQdGKL723nWi6gIF1UUFKx%2BKip%2BRvv0JE4kkHR7aZZXUT6odX4Pji50rjZlFzC52K3vrzCI17%2FSBjqkAWCqDqKGiRNHLKaRz9zk5NJ%2FTKp%2FTXyqP4C71xvurwbJtk%2F301B9SXFh37zKmjQJS7CyXg9Q2h0mdvkjHj8N%2BXKkwtP7qfsIuiOev2Tp3O10vDMCCo9sIp3ikbuHiNS7sH%2BCtjSvTWjWLUCBdygL6pjb0C8fxpu7esPATes%2FGpW0fKiVN5FymwPKRryea0lCQy4PY4A0e0gBEH1WYHdElgmd3Lls&X-Amz-Signature=a26154b08b76b44c477ba0c304567349c14dd00cafabec9a44637dbe1f36068c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X36RFTDE%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T191914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJzyj31CaIpkHo25iFCozDBU5GeCEpx7aND3CmVFl8iwIhAPG9oOKqgf%2BuvDHNx2%2FsQZQYbUX3h6YZjNkj589eenlwKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwlueycwwRRZn5Ks3Iq3ANuEs4F3YGe42%2BZGeBHOykOW8WoBzAvpun9qEQwBbNUe897rfxhiJ6C7qT5pzneLRzb55r3tOMDVxhqMjVSyvH%2BPzkyf%2B88e4JbsXfwRpWNAyfT5Ehi9L%2FimhIMnsJdyXbDrsRGWJH0%2FOBlE7DD9SSRytlI5ifKK%2BXyVWlStlwRYw0n4B%2FyynvvKRjV%2FTCnrIET9jVnklcIHl5yISVC7zK1RRWNP177ndwJhJZMbxJk5R4AYoxllotVztrL%2Bk0Dl6A%2FBhAWEX8cRPazEzDGJcLrg265xUocjUR47D20chnvxUfDQepPHL%2F42hOP7l1SVkS2n2RGdvJw4rzmahP1cbqK3MOLXvaK4bau9S3IprnM9hjkW5yFQaHHuweRP0pjSWm0Mm9%2F4JQf1aF3SDE5u6uVaA9cAYz7tzSljk7pHmVvHoAs%2BslrkvoTxSKkVuBmsyUM8wO9EfCjH75%2FNsfhJVopwNlXfFIJgoFd4g4sIxqT4WOvdVph%2BRzMrR3aj0Y3YNIzxqW%2FalT5uOCjM31KGiGxWNFI1A8sC22kkm2aVzc7F4Kolm5j5mjP4dQdGKL723nWi6gIF1UUFKx%2BKip%2BRvv0JE4kkHR7aZZXUT6odX4Pji50rjZlFzC52K3vrzCI17%2FSBjqkAWCqDqKGiRNHLKaRz9zk5NJ%2FTKp%2FTXyqP4C71xvurwbJtk%2F301B9SXFh37zKmjQJS7CyXg9Q2h0mdvkjHj8N%2BXKkwtP7qfsIuiOev2Tp3O10vDMCCo9sIp3ikbuHiNS7sH%2BCtjSvTWjWLUCBdygL6pjb0C8fxpu7esPATes%2FGpW0fKiVN5FymwPKRryea0lCQy4PY4A0e0gBEH1WYHdElgmd3Lls&X-Amz-Signature=22f0d0747cd5151603f073da11fda9fbbae15b0be3660eacf19f597c41d6aee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
