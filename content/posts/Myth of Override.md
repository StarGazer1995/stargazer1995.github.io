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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633W6TWR7%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T095913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIGhJ4JKgSpsRobuj4rgBWyrTJnS3u1seQN17QkfvLpdVAiBlcxvvTGxkY75mgPkL2dx2FIu06mnSLA5VGRP%2BobaJTCqIBAjZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr6M%2FFejuWemLpdk3KtwD6mvbBO4vOM4Iq%2FuJXuL0RVEB6lAQGX7%2F9hCY8IZN%2Bp4aB%2FbeDagDC0tml%2F7CsRvoICM7s0G7b6xEdqttD4b6pRTZ7%2BHCu2FktHg0z3id%2BqF0cqb3LN9KduHB%2FckMW%2BUq033iUD%2FKNlj626vNq01BpjXJV8hp9PDPDNu9gjWRAJQKBNitTCIO9WFy9FXOLvJuaenOy0hlKgrbBAj9MnXsuG7pJM7Jj1px8SVU7BppoMJsurV1Mw1KvLL0wQeUkRBfQx2QyYpVlwPYGHVfPD7Y8AdD00NmLmJWL7LxpbJ4a9pBtcoaIXmQo9mFoaQqrDMAS3M12KUwjJBoq8rU3bf3%2FAVmltQCixojkZLb3t5mdy%2FIuD20OPNr%2Bja4%2FDojw5KvlG6AwrHy1qc0SfJI1CPMbofS%2Bv9Sh1%2FbW8W2DS70Au6zWzIwUaweYbvTkNNSlXZ%2BAN8JoJyNxP%2F42KSB5IM1RZEO0SPhlHOxpCPtjfbxzwNZ40rCHleLu5wlXO%2BE6KYhiJOx4uDpgBFa%2BR%2BRfYGTni6dDNxFWox324Zkk4ftNlEN5mBG6A%2FRb1m3EBW1%2Fl%2FHAcQfy%2BlowqfHkmkp6RROy8XcWHNJMD1nMywgRrGiu0LZaxqCTyma%2Fuv3XzgwjvG70wY6pgFS2NJbHXljLdVB6dY%2Fqn2TkXhpVByyGYsR8VUHg%2BPIwx1z3o%2FnBJf5YGiqQucY5hGvv3v%2BCk0DLY37k2xklUwX1wdBTSLqmWkqVkeeRP069Nri6OjS19aBNlwwx9uXUeN9VzzvD7wUb6hVO4qNZCYsGoXMfcx5K7DLrH5YuCDNXDxzyR%2BNbxUGQFITed9eqLeVyO9Nl0If3eYmF%2BYDCI%2BrwIhrgK%2Bf&X-Amz-Signature=9a814efc39d9e0c6564ecf3d19492e8f8949c73bc7e24468cc7b821ac64a9e7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633W6TWR7%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T095913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIGhJ4JKgSpsRobuj4rgBWyrTJnS3u1seQN17QkfvLpdVAiBlcxvvTGxkY75mgPkL2dx2FIu06mnSLA5VGRP%2BobaJTCqIBAjZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr6M%2FFejuWemLpdk3KtwD6mvbBO4vOM4Iq%2FuJXuL0RVEB6lAQGX7%2F9hCY8IZN%2Bp4aB%2FbeDagDC0tml%2F7CsRvoICM7s0G7b6xEdqttD4b6pRTZ7%2BHCu2FktHg0z3id%2BqF0cqb3LN9KduHB%2FckMW%2BUq033iUD%2FKNlj626vNq01BpjXJV8hp9PDPDNu9gjWRAJQKBNitTCIO9WFy9FXOLvJuaenOy0hlKgrbBAj9MnXsuG7pJM7Jj1px8SVU7BppoMJsurV1Mw1KvLL0wQeUkRBfQx2QyYpVlwPYGHVfPD7Y8AdD00NmLmJWL7LxpbJ4a9pBtcoaIXmQo9mFoaQqrDMAS3M12KUwjJBoq8rU3bf3%2FAVmltQCixojkZLb3t5mdy%2FIuD20OPNr%2Bja4%2FDojw5KvlG6AwrHy1qc0SfJI1CPMbofS%2Bv9Sh1%2FbW8W2DS70Au6zWzIwUaweYbvTkNNSlXZ%2BAN8JoJyNxP%2F42KSB5IM1RZEO0SPhlHOxpCPtjfbxzwNZ40rCHleLu5wlXO%2BE6KYhiJOx4uDpgBFa%2BR%2BRfYGTni6dDNxFWox324Zkk4ftNlEN5mBG6A%2FRb1m3EBW1%2Fl%2FHAcQfy%2BlowqfHkmkp6RROy8XcWHNJMD1nMywgRrGiu0LZaxqCTyma%2Fuv3XzgwjvG70wY6pgFS2NJbHXljLdVB6dY%2Fqn2TkXhpVByyGYsR8VUHg%2BPIwx1z3o%2FnBJf5YGiqQucY5hGvv3v%2BCk0DLY37k2xklUwX1wdBTSLqmWkqVkeeRP069Nri6OjS19aBNlwwx9uXUeN9VzzvD7wUb6hVO4qNZCYsGoXMfcx5K7DLrH5YuCDNXDxzyR%2BNbxUGQFITed9eqLeVyO9Nl0If3eYmF%2BYDCI%2BrwIhrgK%2Bf&X-Amz-Signature=8d31c313dea67df66d4fc1161fcdb0cbdc00eaf7078ec5147521dc82d6c49c2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
