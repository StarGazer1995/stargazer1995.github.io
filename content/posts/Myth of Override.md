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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7U7LMG5%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T003354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDe3sulZZ0EC6Rc035nb7efFQPQscnggEJoHm6znmK9CQIgDdYcq2gpSAxHWUvwuO266R7dV7ZgAJTXH%2BDBRRL4TeUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDbTzkuEAdAR6KiUWCrcA0U9ikhb5iLj9n0WXsTQbqfat6sqoMN25Nt88SGSexXsSeJ%2BkS2dsGV9F%2FbFOw9%2BqSnh3qidM%2FUun5%2FO87S%2FhES69yUo6SIctldmbMTK61iuiMrHkk3KtuIhLlUsYBQJdD1JtgBTumWZbCJiWCKzsSBHT6S8fTPsgac7DO56jmaAk1EOIMMt8Uv3mjTsN4U4oVrOc0rupRvwMedhLujZeyHNQ3ykMSc5jtnD9kQ4zoKjDty5ktf2B34nSJF9UUfRB2kRyFBZoku2K3PFmV0%2F%2Fcev5M2CZfQHxCPG2ovomhJqsEcsxdJNJkul0mIU1S%2FnNe64TcCqdKr9thwyjovm8b7oXORK2NKUD6pHggdClB4b4H2uBvljj18cHFTeI1nEqGzJYP9Nzcj%2B7rpimf%2BIkmn5qxy9n2Ew8diBBs8oraRYmejctkuHxRAnUOs9cDPzVxhgbAw72HuzWDju2mJKFqZ9NkPa%2FeiH6kSg7ZNPSOtayCoHbvf%2FfvGu9VvR8sStldhgRFra1exQB2x4nesBBH%2B4E5pAsw4OH3jAufUtlONzxcw4235BvtNIRk4A3kiuytQCC%2ByXEiQ%2FzVx0yctfYoX4jRkmV8pqpyBSCBZzV1jGIrmfFKYHoluZN7W1MIrWuNQGOqUBG27MqYN6bdkC7DSVQqz%2BvYVWjlGtEqST%2B3mB%2Bp68DrWsazUHQQ83bXKsJtfc25sICryZS5vhi5JJmVceTtwsYmed7DyvSfph6Z9fhE8%2B8ht5fn2rzBxoQx4xJ3lJhlGnH3hoSK7ot40Kw74SN3Jovt5z8gnJ0u7HYVSd5ZAFZKFru3iLXg99q9Ng%2FjO7Y3erzV4Ly%2FjycPCjin7Z0fKeV8X%2BfKhK&X-Amz-Signature=aaf0cf534479cc0056658178d9f0b9b865dd4f36e87e334ea3eb0c184a481d6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7U7LMG5%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T003354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDe3sulZZ0EC6Rc035nb7efFQPQscnggEJoHm6znmK9CQIgDdYcq2gpSAxHWUvwuO266R7dV7ZgAJTXH%2BDBRRL4TeUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDbTzkuEAdAR6KiUWCrcA0U9ikhb5iLj9n0WXsTQbqfat6sqoMN25Nt88SGSexXsSeJ%2BkS2dsGV9F%2FbFOw9%2BqSnh3qidM%2FUun5%2FO87S%2FhES69yUo6SIctldmbMTK61iuiMrHkk3KtuIhLlUsYBQJdD1JtgBTumWZbCJiWCKzsSBHT6S8fTPsgac7DO56jmaAk1EOIMMt8Uv3mjTsN4U4oVrOc0rupRvwMedhLujZeyHNQ3ykMSc5jtnD9kQ4zoKjDty5ktf2B34nSJF9UUfRB2kRyFBZoku2K3PFmV0%2F%2Fcev5M2CZfQHxCPG2ovomhJqsEcsxdJNJkul0mIU1S%2FnNe64TcCqdKr9thwyjovm8b7oXORK2NKUD6pHggdClB4b4H2uBvljj18cHFTeI1nEqGzJYP9Nzcj%2B7rpimf%2BIkmn5qxy9n2Ew8diBBs8oraRYmejctkuHxRAnUOs9cDPzVxhgbAw72HuzWDju2mJKFqZ9NkPa%2FeiH6kSg7ZNPSOtayCoHbvf%2FfvGu9VvR8sStldhgRFra1exQB2x4nesBBH%2B4E5pAsw4OH3jAufUtlONzxcw4235BvtNIRk4A3kiuytQCC%2ByXEiQ%2FzVx0yctfYoX4jRkmV8pqpyBSCBZzV1jGIrmfFKYHoluZN7W1MIrWuNQGOqUBG27MqYN6bdkC7DSVQqz%2BvYVWjlGtEqST%2B3mB%2Bp68DrWsazUHQQ83bXKsJtfc25sICryZS5vhi5JJmVceTtwsYmed7DyvSfph6Z9fhE8%2B8ht5fn2rzBxoQx4xJ3lJhlGnH3hoSK7ot40Kw74SN3Jovt5z8gnJ0u7HYVSd5ZAFZKFru3iLXg99q9Ng%2FjO7Y3erzV4Ly%2FjycPCjin7Z0fKeV8X%2BfKhK&X-Amz-Signature=71c58cf2c8216c09c15cff41ee650e17986fe6adba1b95e8b952449e3062438e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
