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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SRZLECJ%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T140010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBWlJCmd8KP58qSBtAJ8rnLI5dDFZrbCqkDMcVlDwzTIAiEAzOaXSEn%2F7mW%2FjLSIfOE00UrhWS8pcbwQHIAho2mIr9cq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDKu%2BAXmoxm7GmbGPtSrcA2UNpB%2B2LbIvsyxE4mav6QGErbTD4BIkqWMGS5hcKMNE3tB5vHF8Sx%2FeY8rx9oW1r86tq0LzioRuqFLW3PRCRyJaxcYoA0QRLzHEODBy0jlhIelsocNvrHyrykbavRAdxP7Q%2Be6JAkVnSmUiplBM6GRkzZ5lZC3CKuU6gjFsil0lGjIXvK9FXSQIz7BPygrSEMMc8%2B99tUAND0c%2FKZX444kG9DFbjtEicl0I3DmoK%2FxHYWbmY8OQb%2Fsjzn3cUVmi1PzMMjPlh6Ztc%2FjvBVJS%2FFWS%2Bxoo%2BQnuUM9Ec3UJJNrRScNOjXqTpu1BEZtIlTDzVH2cmgjls1OvXAd8YbQZih%2FJ6dWMQdDXi3Bk7g79jBjJNXwm7weLyo9qjtTUUdesXBHDLT1QSQqrg3IbyEb6CgTDMvCd8MINonVzUg2kmwZzTS9l7e%2BxGp7LxtBaewTuFbyDsxvuHIyM3ntvIdbvNXNZTfhYFyHt5atCMZ81XTnG5cgwXvDSbmts%2FxWjWn3%2BvGTBVBPpXfKN4G7c2gipHVreewXiZNMuo2VStyAEPHNbOYNbkhj6yN5cw7hImfAy2ekzwh%2By5sI1Nl2JH%2BODPXpCd%2B7NgBIPPG%2B88MJIs9bx9O1ue42Kfiv96Ci5MLnb9NEGOqUBdzDSWhr6T2Y64bU0Bq62Iwg%2FxLZY3m1OkEFPejPJprSIYQhZFT7d138Jr5NW3kzLvJI0aHXuvlNQocQgZv4%2Fbbkq09rL5%2Fcb%2FPCWa7WBWIzTE7m53Kh5BPEahKgddUuteYUhiaXWQho%2FD0zwX5WP66DLEsVDsfo9H5bySDWokbRuKdmGnTWsdY%2B1AQgmkF1CCItLrntYBoMejlCsgwJ6ZjBGwez9&X-Amz-Signature=25fd3471f2d348a52a06662650ee2d81ecb6cdc5c6937b3d68017e1287c9b768&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SRZLECJ%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T140010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBWlJCmd8KP58qSBtAJ8rnLI5dDFZrbCqkDMcVlDwzTIAiEAzOaXSEn%2F7mW%2FjLSIfOE00UrhWS8pcbwQHIAho2mIr9cq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDKu%2BAXmoxm7GmbGPtSrcA2UNpB%2B2LbIvsyxE4mav6QGErbTD4BIkqWMGS5hcKMNE3tB5vHF8Sx%2FeY8rx9oW1r86tq0LzioRuqFLW3PRCRyJaxcYoA0QRLzHEODBy0jlhIelsocNvrHyrykbavRAdxP7Q%2Be6JAkVnSmUiplBM6GRkzZ5lZC3CKuU6gjFsil0lGjIXvK9FXSQIz7BPygrSEMMc8%2B99tUAND0c%2FKZX444kG9DFbjtEicl0I3DmoK%2FxHYWbmY8OQb%2Fsjzn3cUVmi1PzMMjPlh6Ztc%2FjvBVJS%2FFWS%2Bxoo%2BQnuUM9Ec3UJJNrRScNOjXqTpu1BEZtIlTDzVH2cmgjls1OvXAd8YbQZih%2FJ6dWMQdDXi3Bk7g79jBjJNXwm7weLyo9qjtTUUdesXBHDLT1QSQqrg3IbyEb6CgTDMvCd8MINonVzUg2kmwZzTS9l7e%2BxGp7LxtBaewTuFbyDsxvuHIyM3ntvIdbvNXNZTfhYFyHt5atCMZ81XTnG5cgwXvDSbmts%2FxWjWn3%2BvGTBVBPpXfKN4G7c2gipHVreewXiZNMuo2VStyAEPHNbOYNbkhj6yN5cw7hImfAy2ekzwh%2By5sI1Nl2JH%2BODPXpCd%2B7NgBIPPG%2B88MJIs9bx9O1ue42Kfiv96Ci5MLnb9NEGOqUBdzDSWhr6T2Y64bU0Bq62Iwg%2FxLZY3m1OkEFPejPJprSIYQhZFT7d138Jr5NW3kzLvJI0aHXuvlNQocQgZv4%2Fbbkq09rL5%2Fcb%2FPCWa7WBWIzTE7m53Kh5BPEahKgddUuteYUhiaXWQho%2FD0zwX5WP66DLEsVDsfo9H5bySDWokbRuKdmGnTWsdY%2B1AQgmkF1CCItLrntYBoMejlCsgwJ6ZjBGwez9&X-Amz-Signature=9e394d53c8db3fca2041698265b272c478bfd21c5efeefca03a5142782148b88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
