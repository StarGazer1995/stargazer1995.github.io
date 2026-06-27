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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JZ2VGAP%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T190141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClNQLNlBq2onxVls8iELZN1KJn5S2iTxkjYnnwJ0ts9QIhAO3xvKnugvEWSEULuwWO45fCeAU2C%2Fca%2FGcGH3BBUFN2KogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxkkc0U0q0epbSEcloq3AO5cVc0POHvl4kTn3AuiLlO17rmA9TKo%2BMOXe9eATqTupbGuG%2FzjjCgArOVxkyDyrc%2FG3lNz3nxtlsBhuZxCdqxdGwH%2B3zYDoNmGgkrekoK44MRx8cOQq8YrgMP5%2Bu5PecV5Hu366nVaQsxwOmKSkEAwRrEnyvKeA3R7uduZkcXYmRbSCbWiw9U7EEu0rWy4Yjbd1HBzxB6Zrl6i4NAgbtOrWKcI5sGqdeCrM9ikc0tTzfelpJrQfbV%2Ftk0DrIrZ%2BpTIREr2AgI8WSVsGPjSDSQl0zANz3135%2F1EY%2FRjDwaHZIkZn1kS9xsmsJJxFMCy4tu78g6QqYwvGNspS1rFnwTtxt94LP7ydMBEu%2FNc3jCcgnF9AmjQCiWR9WgzHCd3nwmkGd45PRMoBiqYXca5S015ae%2FLSHOz17PbNys1Ukz01AXcnn9pQq6oA9ugr36U3TUx8KtDYGC8BpjCwD1xIucXwJ5uztPaIu3Ui10TBLsZp5MoGt7rJx4yHx2JPQlSKCmGyg5hatpgMcvohRNv%2F86Bv8rzA8ddOjbdFeWBwc5dA8Lr1IBu6oMXf%2B3q321HsGypaROhq6XMBxid8yf237r6qn8SYrk6RQ5lyRcE6%2BCwvMAbH%2Bf%2BhDq21ZHKTCdnIDSBjqkAV0n%2FSJ%2F4tZXCuw5juIIWiNK%2FSbeavz4C%2BGG%2FMg%2B%2BOQ663ld9LmcqKRyAnnEtJ0AP5yIrO47LbXSet%2FFjf%2Ff20KQ5FhYofexA2qNcDHUIvdN6KTML8dbKXueeeHTXN4yY4AvOnWUjVtBV0iGn6KCmQsJ%2Fp8UkBpWLmZ0lDU4OZMyw2PvY%2BsEgpe%2B78epVf%2FDw79Eim4vMYxg2rncvfmLO%2FfY9e3k&X-Amz-Signature=1ab35598bcf68973a862042d93178a70a97a0b46e5a9aff3e17d10de02270265&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JZ2VGAP%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T190141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClNQLNlBq2onxVls8iELZN1KJn5S2iTxkjYnnwJ0ts9QIhAO3xvKnugvEWSEULuwWO45fCeAU2C%2Fca%2FGcGH3BBUFN2KogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxkkc0U0q0epbSEcloq3AO5cVc0POHvl4kTn3AuiLlO17rmA9TKo%2BMOXe9eATqTupbGuG%2FzjjCgArOVxkyDyrc%2FG3lNz3nxtlsBhuZxCdqxdGwH%2B3zYDoNmGgkrekoK44MRx8cOQq8YrgMP5%2Bu5PecV5Hu366nVaQsxwOmKSkEAwRrEnyvKeA3R7uduZkcXYmRbSCbWiw9U7EEu0rWy4Yjbd1HBzxB6Zrl6i4NAgbtOrWKcI5sGqdeCrM9ikc0tTzfelpJrQfbV%2Ftk0DrIrZ%2BpTIREr2AgI8WSVsGPjSDSQl0zANz3135%2F1EY%2FRjDwaHZIkZn1kS9xsmsJJxFMCy4tu78g6QqYwvGNspS1rFnwTtxt94LP7ydMBEu%2FNc3jCcgnF9AmjQCiWR9WgzHCd3nwmkGd45PRMoBiqYXca5S015ae%2FLSHOz17PbNys1Ukz01AXcnn9pQq6oA9ugr36U3TUx8KtDYGC8BpjCwD1xIucXwJ5uztPaIu3Ui10TBLsZp5MoGt7rJx4yHx2JPQlSKCmGyg5hatpgMcvohRNv%2F86Bv8rzA8ddOjbdFeWBwc5dA8Lr1IBu6oMXf%2B3q321HsGypaROhq6XMBxid8yf237r6qn8SYrk6RQ5lyRcE6%2BCwvMAbH%2Bf%2BhDq21ZHKTCdnIDSBjqkAV0n%2FSJ%2F4tZXCuw5juIIWiNK%2FSbeavz4C%2BGG%2FMg%2B%2BOQ663ld9LmcqKRyAnnEtJ0AP5yIrO47LbXSet%2FFjf%2Ff20KQ5FhYofexA2qNcDHUIvdN6KTML8dbKXueeeHTXN4yY4AvOnWUjVtBV0iGn6KCmQsJ%2Fp8UkBpWLmZ0lDU4OZMyw2PvY%2BsEgpe%2B78epVf%2FDw79Eim4vMYxg2rncvfmLO%2FfY9e3k&X-Amz-Signature=5906eaed2c9d7b17c0b1bdd92886e48f0db4ed1af97a47774adc34664e533fa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
