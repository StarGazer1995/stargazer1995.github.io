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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFVJK55W%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T133300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFxjOsCFn3PUEZPcL5KgmnRzg7SSFpcamX%2FHdVcFMWBgAiBx%2BOyCJWSzYW0FJXTib3vqW30tE7leBaZLc1T9cxGt2SqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBxr2LlbHwc6mwk0sKtwDcIfcGF1XSAvAQQ3SBHjaN1i646xiLg%2BSwlKOB3n5PND4nj1zwL5LzDdHgMTF6Q6FVC8JrFfZqm9D0KPHdHY%2BY1Gjr4Zua1z2QJNd2UbVDbILEPZPVqrDDmNP9PByb0uz%2F0i3G6l4%2FeZdO8ryxdx88lMAWydN5dbhA7HMVsvsbRicWxbA0iV0vU0gkDyHTcHBL3y58EHOBWoUnjXmv%2BFf1SP4Yjvwj4b2udBkVyOPOJYBLsURyA8RFY95%2BkGC8wsXN5M8dRJBqIMib8QY5Ba%2FKsQ0BTsXFXMstUvjeRKMNz7HQgNbCNwE9Eznj7vavQjwQnE%2FMt5U1UrJiP02Huh5rXvKJFmbRuMNNzRkRrhipRIdZAhOo%2B2aY16i4AZUIjDRlKRqjcG%2BHQrHkuKKmXaShxrShVU1Z0EivBcq7VNcwJ6Dvys8x3kaQr6plYvmG9XBaviiEINvuus2cWaSPmNIz7vjBUEcmc%2FHNbL7Ueeweex9AhoJ%2BjQq0jG%2FllTBsjTQK7trjSEBfKDd4arCMiDSRBh2D1CGTXLNWP6HPGbm43NbAseb9jWTJ0rvjRDfjlQcHJJeE0G47tbOLlcpgDdCwMS9vURDFMnVg797Se%2BTIYO94ewUEtpJi8XxK1cws5aI1gY6pgGzO6vGRE4eOx1TtymIIGTeS4XTLpMvTQAPn2%2FYu3FG9jFFsx4AUIMd9iXEtVQ3XmyvVbI00uI2FOsd05dkMn210sy3YDmZ85%2BEBNnUbEyVb%2BYjbg%2BHFyCSAN%2FhEyEm54HvaslQ15kmRp58%2F6b9HOMtq%2F2PTYtvAGNnT4gF3VQwd5CNLT%2BfhEFIBnOR97OpaSGEv%2BcVfpyy3StqZwWLMmwD%2Bw5LVOgU&X-Amz-Signature=e80f9313d30b9b0765de6f69c85139244837137ac80a855de2356c5df0228757&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFVJK55W%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T133300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFxjOsCFn3PUEZPcL5KgmnRzg7SSFpcamX%2FHdVcFMWBgAiBx%2BOyCJWSzYW0FJXTib3vqW30tE7leBaZLc1T9cxGt2SqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBxr2LlbHwc6mwk0sKtwDcIfcGF1XSAvAQQ3SBHjaN1i646xiLg%2BSwlKOB3n5PND4nj1zwL5LzDdHgMTF6Q6FVC8JrFfZqm9D0KPHdHY%2BY1Gjr4Zua1z2QJNd2UbVDbILEPZPVqrDDmNP9PByb0uz%2F0i3G6l4%2FeZdO8ryxdx88lMAWydN5dbhA7HMVsvsbRicWxbA0iV0vU0gkDyHTcHBL3y58EHOBWoUnjXmv%2BFf1SP4Yjvwj4b2udBkVyOPOJYBLsURyA8RFY95%2BkGC8wsXN5M8dRJBqIMib8QY5Ba%2FKsQ0BTsXFXMstUvjeRKMNz7HQgNbCNwE9Eznj7vavQjwQnE%2FMt5U1UrJiP02Huh5rXvKJFmbRuMNNzRkRrhipRIdZAhOo%2B2aY16i4AZUIjDRlKRqjcG%2BHQrHkuKKmXaShxrShVU1Z0EivBcq7VNcwJ6Dvys8x3kaQr6plYvmG9XBaviiEINvuus2cWaSPmNIz7vjBUEcmc%2FHNbL7Ueeweex9AhoJ%2BjQq0jG%2FllTBsjTQK7trjSEBfKDd4arCMiDSRBh2D1CGTXLNWP6HPGbm43NbAseb9jWTJ0rvjRDfjlQcHJJeE0G47tbOLlcpgDdCwMS9vURDFMnVg797Se%2BTIYO94ewUEtpJi8XxK1cws5aI1gY6pgGzO6vGRE4eOx1TtymIIGTeS4XTLpMvTQAPn2%2FYu3FG9jFFsx4AUIMd9iXEtVQ3XmyvVbI00uI2FOsd05dkMn210sy3YDmZ85%2BEBNnUbEyVb%2BYjbg%2BHFyCSAN%2FhEyEm54HvaslQ15kmRp58%2F6b9HOMtq%2F2PTYtvAGNnT4gF3VQwd5CNLT%2BfhEFIBnOR97OpaSGEv%2BcVfpyy3StqZwWLMmwD%2Bw5LVOgU&X-Amz-Signature=5eecda7cc09254824eccdf6aeb66bb4bab204d63bee0eca76e9f90cb637abdc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
