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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R26LB277%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T224258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTAMk2M%2FjIHwzklWmzhZzfT6%2FEub4ovsW9nbE%2BlKq2iwIhAMcV4ELcwo4fqGxdt2y5LIFpZyR1k2rRBTEbILQhBXArKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw182ygqCf2iG1YLwUq3AMOMkL5yxGBjWG59xqgsYhWiZ4me%2BT4zQ2x45KbVhT1D52cFHhMO3JlDOFjtXUpKqbUE6tGpmk62fLXqvOFxALHGC0B4MCRvfjUU24JjJbW8Y09%2Fm64mppAbJCBwVPwv1j7yak0P5%2FoOIGHqKnSXwNBeHVbnYzn91H%2BROLW2WbjnbjRYyTa6bjrGCq3xvcoGz0OlM9dSOOpPW1Sf4cpXCx%2BNciLvB8i2FnP9OOOG4hLyz07%2BuY0TjTe4%2Bq3kn1oMs9oeRLTN%2FODDMlPzDLolfSf3yZ0qqE1ohAKu2Y3jTmoTbObuvepv%2FRFj95TrBgOBiaY4jFyvjG5L5zSMpbvyu%2BGXZYMA3yjKhXI3cz3N8GdCq3vU7KgdaZEEy%2BO4tH8SyJPieUDMffaSPNh9hgRss8P2zf6ZGWaJ34bymz8U0UnIr60PwccDN9lEy8ULzZj%2FeuzBrDdaK%2FD%2BSO7qw%2FBNKynaIFi2SRKxs1mN4ABhH7OZrf3lCrzmgsyN9lZRWW52bNdWDyL0lE%2Fjz4r9SQ%2FGfw%2B0hykCi5m92whmcX6xqE%2F6QfkDE1WZ2a0%2BuR%2FvXF5dYihpajAyjfuGL45tvpks8yqTIOuxQMsKUVdw8rn%2F%2B%2BBOb7aN7z1tzayCu6tpzDO7ajQBjqkAWIaJd9y30rhFGduujtm5P%2FHDMUatpdYP9FF6ulfitLTfAlmNtd3%2BpZ8bbNcQy7YgO5h02Uo8lxqh3YiiuUPeID3Lng8Mzhl7aQt8Soez6xhA0LjfnxNbA3JER61r3H83RZ5z2YCqYBVgSMweHMDmA3Arp1mqAvt7TMbZMd%2B0SEbnTGLLZ%2FJ9VmZ0FMHhprv6dY12IanwdQHN764o%2BCfsFqOmX9F&X-Amz-Signature=813bb159bf87055d2e4521c46e4575a696c11f19f4604f8613a792e2b619a6ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R26LB277%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T224258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTAMk2M%2FjIHwzklWmzhZzfT6%2FEub4ovsW9nbE%2BlKq2iwIhAMcV4ELcwo4fqGxdt2y5LIFpZyR1k2rRBTEbILQhBXArKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw182ygqCf2iG1YLwUq3AMOMkL5yxGBjWG59xqgsYhWiZ4me%2BT4zQ2x45KbVhT1D52cFHhMO3JlDOFjtXUpKqbUE6tGpmk62fLXqvOFxALHGC0B4MCRvfjUU24JjJbW8Y09%2Fm64mppAbJCBwVPwv1j7yak0P5%2FoOIGHqKnSXwNBeHVbnYzn91H%2BROLW2WbjnbjRYyTa6bjrGCq3xvcoGz0OlM9dSOOpPW1Sf4cpXCx%2BNciLvB8i2FnP9OOOG4hLyz07%2BuY0TjTe4%2Bq3kn1oMs9oeRLTN%2FODDMlPzDLolfSf3yZ0qqE1ohAKu2Y3jTmoTbObuvepv%2FRFj95TrBgOBiaY4jFyvjG5L5zSMpbvyu%2BGXZYMA3yjKhXI3cz3N8GdCq3vU7KgdaZEEy%2BO4tH8SyJPieUDMffaSPNh9hgRss8P2zf6ZGWaJ34bymz8U0UnIr60PwccDN9lEy8ULzZj%2FeuzBrDdaK%2FD%2BSO7qw%2FBNKynaIFi2SRKxs1mN4ABhH7OZrf3lCrzmgsyN9lZRWW52bNdWDyL0lE%2Fjz4r9SQ%2FGfw%2B0hykCi5m92whmcX6xqE%2F6QfkDE1WZ2a0%2BuR%2FvXF5dYihpajAyjfuGL45tvpks8yqTIOuxQMsKUVdw8rn%2F%2B%2BBOb7aN7z1tzayCu6tpzDO7ajQBjqkAWIaJd9y30rhFGduujtm5P%2FHDMUatpdYP9FF6ulfitLTfAlmNtd3%2BpZ8bbNcQy7YgO5h02Uo8lxqh3YiiuUPeID3Lng8Mzhl7aQt8Soez6xhA0LjfnxNbA3JER61r3H83RZ5z2YCqYBVgSMweHMDmA3Arp1mqAvt7TMbZMd%2B0SEbnTGLLZ%2FJ9VmZ0FMHhprv6dY12IanwdQHN764o%2BCfsFqOmX9F&X-Amz-Signature=b1e348edbc2fe9c8652f09909986c2ff40aeae7d82710cd1117965ecc6497568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
