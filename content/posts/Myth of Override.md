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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642UK4TX6%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T225751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEzZyAjJYSd1PXrp0qgI4Lcb7CO6Mj2r5t%2FX7SkZ0V0PAiB6ORz6MxBhamFtaLgmkyiClup5sDjcRd%2BNGODEZo6M5iqIBAjg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfAyrNHEOywaRJN5nKtwDOb%2FDJA8T%2Fzxnt4k268WnyELMmDb0x220zJ6kqydljPr17s0v2p1Cn3pVoxZ8Pl0sB4Iqz%2Fdr7rrX4GfOIet2srWRfypx4dKp1R7FGiXmgWNicNeZDiI6lI1WvUZtI5TedSolUrLY8yv%2Foz103B7kuB7CCvTMEcAkwl8PLXz8r5bUTdj6wQSAVEkm4PJ5M6vLuP9t4evz4qAheBlnIbGigF1zSn%2FnwykcFsmuUqAq5O519otxtfiv%2BGUqz3dr1bqbvWuOLKelcFZ9sdKAqHGMA1sHUrLWa6laazUt54Hcp1%2BtlrzVYNtx5fQSK%2FZgKK26WYVsY5AEKFCdlL9YxcH4QkoPHsUGH7%2FLHALEUKYPhHeJNoRniyFy9VYW%2F7FiIhVplxQkMXdLjn9nVOonbTxk21Ur2IOUo7JAj5i4qR97V%2B14LILrM4qeHojIh0ZBufjznCTXOOUvQbxHmLr12sHTfIBWjMNSCgHYtQqnAVYf27m4XeyuSwIDrbpOWJZptGAF8mPmzfaJuJiLs84wIjPs58tL37rEATDYDfIxN9xzTA1yLQ%2FuRiLqqkoU%2FJsmcOXeOeSX3HSB4K7fJcJ%2BFx1hKhBJyHPS7tvua6DRqEbMxJmDdEJJXSNBZyT23vAw57Hc0QY6pgEFoDvJSQhUmnqRhEfeaMWRIzxOaC2RJ7qdg1oe3NAyGaROBcPmiWepnTg7Ph2zFk39dEa8UmwE7bwh1j3ypm373ndC%2FzUOyDU7QeS88NFAPiaK%2FytRpgg6tfvfSzholZegAUNGlxVP6l8XiUOixPEOu0vuf6G1DVQv%2FGjByDbNUlrLF1dByKoJa5ss3ccDFrQmVa1tOwK7fn%2F1hEvdeWTsix6Kl2AZ&X-Amz-Signature=d092bbdebe68e60154ee80b037518394aab6b5b76c97ce1cea74dfc3e259912e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642UK4TX6%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T225751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEzZyAjJYSd1PXrp0qgI4Lcb7CO6Mj2r5t%2FX7SkZ0V0PAiB6ORz6MxBhamFtaLgmkyiClup5sDjcRd%2BNGODEZo6M5iqIBAjg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfAyrNHEOywaRJN5nKtwDOb%2FDJA8T%2Fzxnt4k268WnyELMmDb0x220zJ6kqydljPr17s0v2p1Cn3pVoxZ8Pl0sB4Iqz%2Fdr7rrX4GfOIet2srWRfypx4dKp1R7FGiXmgWNicNeZDiI6lI1WvUZtI5TedSolUrLY8yv%2Foz103B7kuB7CCvTMEcAkwl8PLXz8r5bUTdj6wQSAVEkm4PJ5M6vLuP9t4evz4qAheBlnIbGigF1zSn%2FnwykcFsmuUqAq5O519otxtfiv%2BGUqz3dr1bqbvWuOLKelcFZ9sdKAqHGMA1sHUrLWa6laazUt54Hcp1%2BtlrzVYNtx5fQSK%2FZgKK26WYVsY5AEKFCdlL9YxcH4QkoPHsUGH7%2FLHALEUKYPhHeJNoRniyFy9VYW%2F7FiIhVplxQkMXdLjn9nVOonbTxk21Ur2IOUo7JAj5i4qR97V%2B14LILrM4qeHojIh0ZBufjznCTXOOUvQbxHmLr12sHTfIBWjMNSCgHYtQqnAVYf27m4XeyuSwIDrbpOWJZptGAF8mPmzfaJuJiLs84wIjPs58tL37rEATDYDfIxN9xzTA1yLQ%2FuRiLqqkoU%2FJsmcOXeOeSX3HSB4K7fJcJ%2BFx1hKhBJyHPS7tvua6DRqEbMxJmDdEJJXSNBZyT23vAw57Hc0QY6pgEFoDvJSQhUmnqRhEfeaMWRIzxOaC2RJ7qdg1oe3NAyGaROBcPmiWepnTg7Ph2zFk39dEa8UmwE7bwh1j3ypm373ndC%2FzUOyDU7QeS88NFAPiaK%2FytRpgg6tfvfSzholZegAUNGlxVP6l8XiUOixPEOu0vuf6G1DVQv%2FGjByDbNUlrLF1dByKoJa5ss3ccDFrQmVa1tOwK7fn%2F1hEvdeWTsix6Kl2AZ&X-Amz-Signature=88cb8f5784d15a55136d2a966aa31cf049b82c0be2a8cb747ad213074f985f01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
