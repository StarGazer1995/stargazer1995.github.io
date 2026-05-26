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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT6C57DH%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T212729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDH%2BNHqxWZXf89t1djbtNK1fbFy6CEGBl0Q0EO8afC6AIgea7s%2Bwqi5JVYWLIbH%2Bb%2BPQfKBnVLCHCum4DWN2y6Ra4qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlTjpxPmFUBx%2FTD%2BCrcA2Y%2BqJNHl8GuIqOyId8gF5rntyUo%2FKba7b%2BcNa8xyDgbpYS%2F9A0mfA62mpAR6bJu2w9PG321N3N6TeFIjGefheEU3xyS%2FGsShZUuOOp6vEVoBIY86b3PuBDRgAuWuxlMdbrsowuF1PPz%2FcoLwAxmFlP%2FkHTjWfUBA618q864OgxrDZFAbNJ3jW%2FIBKxEPV45fRcEbde9FBKB4jVcZB9QuPmv1W0rYmATkGPUtcaE7qu4CJO%2Fnf8wAliUU2EXUoctUX9LKbgSRwIbBBpkO0mf2Rvn25cDPAosyyKmmw11HCbz3d%2BMnczKstoSJBEMmlAr0TlpYPvzw23mA5OCuDb4wTGmZ3AicP3asro40lse5qU7JesgfEYDWKb5gLmtFYbWx3TliVUcP5wE9Qeq73mLa4i2SvZmKjZHlWpR6LDc5F3PvnXC6fHSp8GOpO9MG6xQnwU6LzdlTiRXj%2FTC2eIDE6ZeTE7HG6kqQKozDOqdedUqn1wZ5Ie01trlPiYBQvgBU6jo6mCxTtHs448hiLkXNQDYkHICDi87pOJsqJ7c%2B8e%2BNeKGdhwvbKpz%2FbQWkaVGiQQVQiQFu3NRv1yXFBVO2%2Bpmq9YcBTTxkNV3quNb34ILwUBSsN9hZne7BgoOMMrt19AGOqUBElir4%2BuQ%2BvYjXq8lkWpDTRAE4AaI8E4kRd0FCN2vYlQhsDAvtxZJk57hSIbqCaXwCMTYyVC2D%2FAWyLFDJ9wxGmfvPMuUj7K5lQZmro1BeMxO0cV9aPqanmt734bEuC24Ghb3bzGl14mLWj%2BVeE54pvw%2B0DcDLsdj0dJbqYp%2FOWT%2Fj2v%2BAZMO4Ze7PkiTriDxg%2BrMK3J2MjnMnEUoW2JR5DmElnhm&X-Amz-Signature=d03c890dab55b5132da38dd4409508f495e9aaf84ec748bdd2bc93194c056ca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT6C57DH%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T212729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDH%2BNHqxWZXf89t1djbtNK1fbFy6CEGBl0Q0EO8afC6AIgea7s%2Bwqi5JVYWLIbH%2Bb%2BPQfKBnVLCHCum4DWN2y6Ra4qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlTjpxPmFUBx%2FTD%2BCrcA2Y%2BqJNHl8GuIqOyId8gF5rntyUo%2FKba7b%2BcNa8xyDgbpYS%2F9A0mfA62mpAR6bJu2w9PG321N3N6TeFIjGefheEU3xyS%2FGsShZUuOOp6vEVoBIY86b3PuBDRgAuWuxlMdbrsowuF1PPz%2FcoLwAxmFlP%2FkHTjWfUBA618q864OgxrDZFAbNJ3jW%2FIBKxEPV45fRcEbde9FBKB4jVcZB9QuPmv1W0rYmATkGPUtcaE7qu4CJO%2Fnf8wAliUU2EXUoctUX9LKbgSRwIbBBpkO0mf2Rvn25cDPAosyyKmmw11HCbz3d%2BMnczKstoSJBEMmlAr0TlpYPvzw23mA5OCuDb4wTGmZ3AicP3asro40lse5qU7JesgfEYDWKb5gLmtFYbWx3TliVUcP5wE9Qeq73mLa4i2SvZmKjZHlWpR6LDc5F3PvnXC6fHSp8GOpO9MG6xQnwU6LzdlTiRXj%2FTC2eIDE6ZeTE7HG6kqQKozDOqdedUqn1wZ5Ie01trlPiYBQvgBU6jo6mCxTtHs448hiLkXNQDYkHICDi87pOJsqJ7c%2B8e%2BNeKGdhwvbKpz%2FbQWkaVGiQQVQiQFu3NRv1yXFBVO2%2Bpmq9YcBTTxkNV3quNb34ILwUBSsN9hZne7BgoOMMrt19AGOqUBElir4%2BuQ%2BvYjXq8lkWpDTRAE4AaI8E4kRd0FCN2vYlQhsDAvtxZJk57hSIbqCaXwCMTYyVC2D%2FAWyLFDJ9wxGmfvPMuUj7K5lQZmro1BeMxO0cV9aPqanmt734bEuC24Ghb3bzGl14mLWj%2BVeE54pvw%2B0DcDLsdj0dJbqYp%2FOWT%2Fj2v%2BAZMO4Ze7PkiTriDxg%2BrMK3J2MjnMnEUoW2JR5DmElnhm&X-Amz-Signature=86e599efb5684bc22a3f5589270b36f32005a53fde15c10461d2c6e756718848&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
