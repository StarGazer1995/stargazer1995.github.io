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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN7NIWBL%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T054945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDzV%2BUa7PhaLB%2FHMFSfdSxJpkrj1pCtZim7ykUJ0SP7SgIhALANBTuv58bq75sTxW4pqAFaSQmz9f8T1ut9XaQ%2FXRpGKv8DCA8QABoMNjM3NDIzMTgzODA1IgzDyHShEUlQXmwRPNcq3AOD%2FONn6AMNFjPs4LnYHxAO1FJV21nkYpDF0xmt0a4SHfUIkXpBUhuGys3fXghR%2FU3OXoY1FLik0RNSHuLqo35inmuqD7CA6zvUA2DJQ1krLol2N%2FtPoktk124h2JrZ18gAlcBWozI2WpsyTokKlaigqQAGIMMKlHkwyphSA0s9iBeNvZ5B3p94wsI%2FqzMhIJcqonkV4ZDXL5WrwegcsrYzeHOafCEzoHOMAIvtAPcYqPN1490Y%2FsOPxqtKvjFSfY0U%2F3D2DEdWYxwAvEYCp0Zze%2FL0faIzYkLmgefOSo%2FAj7%2FeGrL5vXj85Ws9HIxbpbdT5QiJVYpo9GyhaTi8ZMoMx6VQxrJVrlAbRV%2FWbIapFgnixn%2B%2FYuXdVtFxXNF8%2BP43tU3CLEDdMNg9xIaexYsi0Vzz0o%2BeD4whigQrnjBiUQlpFiwyZVxgKMy6jnXnr%2F%2BfyAZAsz1I3%2BlpR8X9f4vXKAcv48aLp3eziGRlPKUX7rcLNJlK8%2Fve4gHH02g6XMyjUxeseL1OyojKnKn6UfbDa778wSL%2BiWUm9gxOzOqJNwQQqPdIPiUYFPjnEVToBoghmmB2joQsZQZqbl1A3hh47ExWmuDoA%2FyTNGoRRHP%2BauHaWOzGXhOWcCzwjTC92IXQBjqkAWga%2BA04yJGmUqGtH8qM4kQIPGOASvyZnfieA5kMnZBlV0YM6WsUpWtpCrmLi8a6dPm8Gea%2BL8M51vBOSNGkj7PbJLtgHoBCwRc2iB6uUnJP0QU%2Buy24NphT94mgXSa73kaxhMy%2BSoM5fgCBJYNviI96q7RpVWBXtK6aKsaITqLnXPpgD59SKvzjua2V8qpCMqjejD7ndveyr93sx2sAq5%2Fc4%2BFk&X-Amz-Signature=129dee7f73bb976999c18213891badce58a5d9cb9d3f0c6089982b474856af8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN7NIWBL%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T054945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDzV%2BUa7PhaLB%2FHMFSfdSxJpkrj1pCtZim7ykUJ0SP7SgIhALANBTuv58bq75sTxW4pqAFaSQmz9f8T1ut9XaQ%2FXRpGKv8DCA8QABoMNjM3NDIzMTgzODA1IgzDyHShEUlQXmwRPNcq3AOD%2FONn6AMNFjPs4LnYHxAO1FJV21nkYpDF0xmt0a4SHfUIkXpBUhuGys3fXghR%2FU3OXoY1FLik0RNSHuLqo35inmuqD7CA6zvUA2DJQ1krLol2N%2FtPoktk124h2JrZ18gAlcBWozI2WpsyTokKlaigqQAGIMMKlHkwyphSA0s9iBeNvZ5B3p94wsI%2FqzMhIJcqonkV4ZDXL5WrwegcsrYzeHOafCEzoHOMAIvtAPcYqPN1490Y%2FsOPxqtKvjFSfY0U%2F3D2DEdWYxwAvEYCp0Zze%2FL0faIzYkLmgefOSo%2FAj7%2FeGrL5vXj85Ws9HIxbpbdT5QiJVYpo9GyhaTi8ZMoMx6VQxrJVrlAbRV%2FWbIapFgnixn%2B%2FYuXdVtFxXNF8%2BP43tU3CLEDdMNg9xIaexYsi0Vzz0o%2BeD4whigQrnjBiUQlpFiwyZVxgKMy6jnXnr%2F%2BfyAZAsz1I3%2BlpR8X9f4vXKAcv48aLp3eziGRlPKUX7rcLNJlK8%2Fve4gHH02g6XMyjUxeseL1OyojKnKn6UfbDa778wSL%2BiWUm9gxOzOqJNwQQqPdIPiUYFPjnEVToBoghmmB2joQsZQZqbl1A3hh47ExWmuDoA%2FyTNGoRRHP%2BauHaWOzGXhOWcCzwjTC92IXQBjqkAWga%2BA04yJGmUqGtH8qM4kQIPGOASvyZnfieA5kMnZBlV0YM6WsUpWtpCrmLi8a6dPm8Gea%2BL8M51vBOSNGkj7PbJLtgHoBCwRc2iB6uUnJP0QU%2Buy24NphT94mgXSa73kaxhMy%2BSoM5fgCBJYNviI96q7RpVWBXtK6aKsaITqLnXPpgD59SKvzjua2V8qpCMqjejD7ndveyr93sx2sAq5%2Fc4%2BFk&X-Amz-Signature=7d832e8857710028e724a4ad2a4e448577312672cc518dcb0999c2eef2d35c58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
