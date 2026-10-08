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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKP7YTJJ%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T223542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIBjikRiPdIi4ADNshnpRJd8L4vPuiMWL5Mtfsjv2q2JbAiEA87j5VKocj253Z6z5z46jGWLjwWfokW43LlxkLCoUMMMq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDDA2v3r10omr70DDhircAy3QZoIpMrqlSrRD39UJRuey%2Fzrb4dhAWlt8LvToYT7b7NXaAIAX4BjtS923Rq4g2GjthNixTd2v7TpqErIWtXqgfWs4RDf1qQc2U1gjPxxu6Bg%2ByNCsAxZc%2BFZ2N0dbMNU%2Bh81rkD8Hu0r81%2Bi0hhfEXfH%2F3IcVW%2F2YRYXIo%2F%2FOg5xpvzcHLMV5jY3%2FOd0r8EykAgDmRBnBlquobAde04uFp6Qq8C2BbA0E8msS6ZOPJVRAegCKXYWzDSYC678EBDK84TyfzevOIe3KKvKzvd9nHl9DaM4O3VoXbkvxLfQ%2F02qH4eMeNv0z%2Br9l7vTe0OCYrKsja59ZO%2BA%2F3F9P0n1ssetUpUNOVqzhrE%2BzGzlnklZav1qggvDYxjFuuaLNpWqeuwL4mLQXsEmmfCoBqCET40700kkaiLiiQwYIGOqKHb1WPAOwYxU%2FsD0eP1tQlV8znw4sQS%2BKaMLWWNvYwHcDtVZ%2BeiskiJygtiZnErqszPHn4M3BZ9MRwQiRikgRSU9JLT%2BNMgJSiW1NeWH9ZVmGSH%2F%2F6kXCZJ%2FynKp6N0CJX5iz96HMdemji9hBHvadzhRrALJXoAAU%2FwRjuA%2F5bHawx1IV%2Bl%2BrEwfPFm%2Fg4VhA3yMzP%2FI6FIJsaXRPMPb%2Bn9YGOqUBgsdbQj3FidNKnrMMcl%2BgSF8C%2B9ZYi%2ByK9T4rJduLRlzTLKn42wqKLHJFBJZgRuP4zut4v79BmlXXsdsleGMpchOgBCnIDCei%2B0mkehpq58hEZCTGGBVCnrCuuiYe4Y8LdcSYv6Y7MEz3M4sDOkoS5jlm%2BZ21ufdexo9l0fIm%2FQmpYXdqIIOW070lehB7LfpxfV7D%2BpW3Yr1sDZ3iD%2Fngt9W9o9dV&X-Amz-Signature=5ae5677a6c47e765a7bf1876e93c62f52bc53f73ff1ef3bbb027548585423afa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKP7YTJJ%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T223542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIBjikRiPdIi4ADNshnpRJd8L4vPuiMWL5Mtfsjv2q2JbAiEA87j5VKocj253Z6z5z46jGWLjwWfokW43LlxkLCoUMMMq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDDA2v3r10omr70DDhircAy3QZoIpMrqlSrRD39UJRuey%2Fzrb4dhAWlt8LvToYT7b7NXaAIAX4BjtS923Rq4g2GjthNixTd2v7TpqErIWtXqgfWs4RDf1qQc2U1gjPxxu6Bg%2ByNCsAxZc%2BFZ2N0dbMNU%2Bh81rkD8Hu0r81%2Bi0hhfEXfH%2F3IcVW%2F2YRYXIo%2F%2FOg5xpvzcHLMV5jY3%2FOd0r8EykAgDmRBnBlquobAde04uFp6Qq8C2BbA0E8msS6ZOPJVRAegCKXYWzDSYC678EBDK84TyfzevOIe3KKvKzvd9nHl9DaM4O3VoXbkvxLfQ%2F02qH4eMeNv0z%2Br9l7vTe0OCYrKsja59ZO%2BA%2F3F9P0n1ssetUpUNOVqzhrE%2BzGzlnklZav1qggvDYxjFuuaLNpWqeuwL4mLQXsEmmfCoBqCET40700kkaiLiiQwYIGOqKHb1WPAOwYxU%2FsD0eP1tQlV8znw4sQS%2BKaMLWWNvYwHcDtVZ%2BeiskiJygtiZnErqszPHn4M3BZ9MRwQiRikgRSU9JLT%2BNMgJSiW1NeWH9ZVmGSH%2F%2F6kXCZJ%2FynKp6N0CJX5iz96HMdemji9hBHvadzhRrALJXoAAU%2FwRjuA%2F5bHawx1IV%2Bl%2BrEwfPFm%2Fg4VhA3yMzP%2FI6FIJsaXRPMPb%2Bn9YGOqUBgsdbQj3FidNKnrMMcl%2BgSF8C%2B9ZYi%2ByK9T4rJduLRlzTLKn42wqKLHJFBJZgRuP4zut4v79BmlXXsdsleGMpchOgBCnIDCei%2B0mkehpq58hEZCTGGBVCnrCuuiYe4Y8LdcSYv6Y7MEz3M4sDOkoS5jlm%2BZ21ufdexo9l0fIm%2FQmpYXdqIIOW070lehB7LfpxfV7D%2BpW3Yr1sDZ3iD%2Fngt9W9o9dV&X-Amz-Signature=3160c0e8fbb020799cc9e807531b1b1a0971b35bb77af05c2119bfe119fced3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
