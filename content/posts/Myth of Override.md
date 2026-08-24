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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TZ7Z6GJ%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T143128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDNqIUdHUTbweKw5zoS9QqOExeBoNRaUF9kEdMXbE1PyQIhALjfKDLNoFzhhO73U7mRhX3XslSRQ4%2BKl7XCeUgU5owaKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQ0UrxDVZoBOnB26Mq3AN2RFwDDRvm2pBYUbG2hcvtrYOEllv63yIChcdCZLnancWLAWxQkgGNr7WRmROZi923D%2BAEFZMwxNXS36WOVtEs4JKwFeNP4oX8m2rixFtTUQw2Jt7MkXxBtg%2Fds6TNKQwTsv0NL7kVbaV4IzE0YwARaw3%2F5cCquTrfiDO6UalG459AEPxscOn99yI20lO8G8%2Fjtx6k%2FfvAhprJcqk64sepwbYxyhRL52%2FNfo5IxcIb3vGSdN1xfx8hlZ46WAkFN9A0EU6ftEfzvryDQakCI5bppMP%2BOQa0HkWA1OKzBKj6erxFdI9WjP%2BIuRa%2Bq8wfqcna%2BNEGVyfXU5r5O%2BcyMy2KftFLCocY3FD5zDgJtt%2F%2BnmSRdj2JO5%2Bo1Y1yt3lp8s92Y3sENtyFCa53C%2BEjDWvhIeGpg6cWIwzWTZPLYMvr8eJKcnqKxU9SOQoiuIpyvzAko05VSWPsBWUVe2JIJwksI5sbClVT1wEzyOmbTXKiP9RDbZlYa4x%2BdUfzv0O7u8VRRsuJph6QyPZrpWc2Mje6WZe9MSCCA4l4fPLRWvn8362%2Bmj%2FLQ4VQZJXB7kqE5QJJoMxPu3zdI3zGzR3yBNKX%2BAvpA2JW8sdlF03ec%2BmYo5mMcu1rTZ4xUvZ9DTCAp7HUBjqkAUxK2D3iw3CL2GPZUB%2BgoL%2F3skTyyRyRRfQdlCahMvaacR8aLva80JHmfKjK%2BFI6xBfDaro4Pt3WFSa8FNiHR7ItvbOumvzHL8iHxaHitoweGhDfQfbsIq0Yru7f4pzZ2cFun5E58PWnU2rmuCq2Yagz6z11tXoJg0arCJO6vO5VVpyiIfIkQLEaUGjo6GDiJtSSGryyGmZGAVHCNKc9zDHVG9vW&X-Amz-Signature=5cd4d8c6908175ce6bf4eb45c412d014bb03b4d0f6eca07791ae91cf7c14ac7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TZ7Z6GJ%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T143128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDNqIUdHUTbweKw5zoS9QqOExeBoNRaUF9kEdMXbE1PyQIhALjfKDLNoFzhhO73U7mRhX3XslSRQ4%2BKl7XCeUgU5owaKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQ0UrxDVZoBOnB26Mq3AN2RFwDDRvm2pBYUbG2hcvtrYOEllv63yIChcdCZLnancWLAWxQkgGNr7WRmROZi923D%2BAEFZMwxNXS36WOVtEs4JKwFeNP4oX8m2rixFtTUQw2Jt7MkXxBtg%2Fds6TNKQwTsv0NL7kVbaV4IzE0YwARaw3%2F5cCquTrfiDO6UalG459AEPxscOn99yI20lO8G8%2Fjtx6k%2FfvAhprJcqk64sepwbYxyhRL52%2FNfo5IxcIb3vGSdN1xfx8hlZ46WAkFN9A0EU6ftEfzvryDQakCI5bppMP%2BOQa0HkWA1OKzBKj6erxFdI9WjP%2BIuRa%2Bq8wfqcna%2BNEGVyfXU5r5O%2BcyMy2KftFLCocY3FD5zDgJtt%2F%2BnmSRdj2JO5%2Bo1Y1yt3lp8s92Y3sENtyFCa53C%2BEjDWvhIeGpg6cWIwzWTZPLYMvr8eJKcnqKxU9SOQoiuIpyvzAko05VSWPsBWUVe2JIJwksI5sbClVT1wEzyOmbTXKiP9RDbZlYa4x%2BdUfzv0O7u8VRRsuJph6QyPZrpWc2Mje6WZe9MSCCA4l4fPLRWvn8362%2Bmj%2FLQ4VQZJXB7kqE5QJJoMxPu3zdI3zGzR3yBNKX%2BAvpA2JW8sdlF03ec%2BmYo5mMcu1rTZ4xUvZ9DTCAp7HUBjqkAUxK2D3iw3CL2GPZUB%2BgoL%2F3skTyyRyRRfQdlCahMvaacR8aLva80JHmfKjK%2BFI6xBfDaro4Pt3WFSa8FNiHR7ItvbOumvzHL8iHxaHitoweGhDfQfbsIq0Yru7f4pzZ2cFun5E58PWnU2rmuCq2Yagz6z11tXoJg0arCJO6vO5VVpyiIfIkQLEaUGjo6GDiJtSSGryyGmZGAVHCNKc9zDHVG9vW&X-Amz-Signature=9ca98277fcb04b3d1c54d6df40f8c16a531aef319522653925a4ddb1247c26ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
