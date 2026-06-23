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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDFC6GYZ%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T141804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIBwruzhjWvrXce%2FmvMG17TAVq4LNov7MGLRRwXEJrwTFAiEAqSEu8HqBYuQ5lTeRr%2FCBYeMm7Tt%2FhhYwyzVN%2BNj79ngq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDIFiyNOaz38qy6SOISrcAwjUWI3JIY5PZ3HHNSCAKFCoqhyTrVjweldUq6CK7XQzvYl2Sa6cuiRbVK%2BnFAgnaURZ91KIDKI3R3ijwYvMszOwbtj9xYtUEJMUNfcYMr7Z1zG%2FBGFxqW4lWPfWigGa3BKSNM%2BrRyUGA%2FJVs3XXDCmPajm21mG97wf76FMXbX9yw%2B069iHNTeomCaE2cDaghBElq3WF4EAnBgo%2FyZi5ObnC4K97qIpAUpuOkDW881XLsjpT1c6cJTDkDZRWFPS5dNFIZeAKpVoF5wYfMBOu0tTwugPh6mINnLvpi3LqPvYLzuvUkgXEt7UDr2r%2B6O%2BsyzrznGfA%2F4mWqLtH1eaFA%2Fr9M%2F%2BBv%2BFtc3aK6ZylsMUH6R1Ulb%2BQpH8XL0iPy9j5htDjYusYijUiL6R8SXD%2Fh7Nu2qB78UurhDzNUT%2FmyiZI3UpNk6XwK6tFhXH%2FhkDzmqoZNz951WKwlzBbbtdkveFporbGuYOjK5ns8DY4SihiKL4ay8Ce9fK9D4qcdn%2BzoVYH%2FPejIGu1DboB1zVOCRuyJEeyQpYNWlhBqyyUNBDjLak8ZUyJnxtLGTDkzRNIsbjreRQJ1mZWdR3sEromwOfgquRZeIDGOXfWiZC39TdgoQgJWcaWpV7IhBCUMNCI6tEGOqUB7WWPCYie1yxA8TrtxvsuWbiA%2FjxPF6RuHrS%2FwppQgUX3t%2FmWIE89rvYLOMj%2FjPDBl9CiZ8ULPWv%2BoXrmO45KQ2O3VoiMyRVEAN48PnB5Fo9yEeEMrs4niUfDi%2BGOf28Dvz%2BE%2FWmPlDdnuBdvvJVo8D3F39BayVYEoVgvHpwSju75wTT2NgugpHvOTXBJrvgCvF6QsNNbLKDqn2zDT%2BIuRODwayxN&X-Amz-Signature=a929b820f1356316bbe96203497b812f7df9a273775a0a86a8e6dbca60a1ecf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDFC6GYZ%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T141804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIBwruzhjWvrXce%2FmvMG17TAVq4LNov7MGLRRwXEJrwTFAiEAqSEu8HqBYuQ5lTeRr%2FCBYeMm7Tt%2FhhYwyzVN%2BNj79ngq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDIFiyNOaz38qy6SOISrcAwjUWI3JIY5PZ3HHNSCAKFCoqhyTrVjweldUq6CK7XQzvYl2Sa6cuiRbVK%2BnFAgnaURZ91KIDKI3R3ijwYvMszOwbtj9xYtUEJMUNfcYMr7Z1zG%2FBGFxqW4lWPfWigGa3BKSNM%2BrRyUGA%2FJVs3XXDCmPajm21mG97wf76FMXbX9yw%2B069iHNTeomCaE2cDaghBElq3WF4EAnBgo%2FyZi5ObnC4K97qIpAUpuOkDW881XLsjpT1c6cJTDkDZRWFPS5dNFIZeAKpVoF5wYfMBOu0tTwugPh6mINnLvpi3LqPvYLzuvUkgXEt7UDr2r%2B6O%2BsyzrznGfA%2F4mWqLtH1eaFA%2Fr9M%2F%2BBv%2BFtc3aK6ZylsMUH6R1Ulb%2BQpH8XL0iPy9j5htDjYusYijUiL6R8SXD%2Fh7Nu2qB78UurhDzNUT%2FmyiZI3UpNk6XwK6tFhXH%2FhkDzmqoZNz951WKwlzBbbtdkveFporbGuYOjK5ns8DY4SihiKL4ay8Ce9fK9D4qcdn%2BzoVYH%2FPejIGu1DboB1zVOCRuyJEeyQpYNWlhBqyyUNBDjLak8ZUyJnxtLGTDkzRNIsbjreRQJ1mZWdR3sEromwOfgquRZeIDGOXfWiZC39TdgoQgJWcaWpV7IhBCUMNCI6tEGOqUB7WWPCYie1yxA8TrtxvsuWbiA%2FjxPF6RuHrS%2FwppQgUX3t%2FmWIE89rvYLOMj%2FjPDBl9CiZ8ULPWv%2BoXrmO45KQ2O3VoiMyRVEAN48PnB5Fo9yEeEMrs4niUfDi%2BGOf28Dvz%2BE%2FWmPlDdnuBdvvJVo8D3F39BayVYEoVgvHpwSju75wTT2NgugpHvOTXBJrvgCvF6QsNNbLKDqn2zDT%2BIuRODwayxN&X-Amz-Signature=9d25c05eecdcf8c841103cf2f777dd698027bad1b37e3a20be558cc17549e2a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
