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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4CZM4T3%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T205200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyrAT3KMp4jJhcmQlkLrTU6msGAb24yRIYryNmtxpumAIhAKFR3P7JAhF6xSDz5AA5cS44QS%2FsgckMi0jFvyfUogn%2FKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6kBWDceF4r4xkDycq3AM7JO6ovPhTfI6Idxfg%2BgpzMeBonervVTmZLCBC4gjEeI0%2BxCrbzd%2FB%2FpBP%2BSJCEYOyLxyNkCTkxwYw%2FDaCbo%2BO%2FQV6eRokBJZkaRGNQA0zZ6IGyeP51kx8s0qLpZhSCCR4BpKde3HZ0mWCz0MjVmWlYI7%2FpkBimeVrEFS%2BcIdvl%2BSI7UBVsm5YhB%2FE3RLpewARnZ6THkxWJZ%2Fc72KJx3iyu4x066xkzTMiog9Eu64BedEDegDtrAv4R1vUAvfTNltRGiH7FHOjM1sfOdBTDvITd%2FT5bLTRjLDXhyi2q4J3Y%2FUngHvmMRY1KCibCG4GcKmR1v7uRxldWSCQ%2FgSUjWvV0EymJjOUdwMc3UlJY2sGq3jEf8RwyDtt2kQ1SqWVf%2FQGGm0Q5W%2BUPjmmPWE1gGJHT%2FQFm%2BUxUk3st3d0s19b70BckH7pe8R%2BDgnnWadLC2MavJ82donHn1tJjcWuC4rtGHnKIt%2FfEYycYspk9nnrAK47XZmiwq7txb42LJoGfyBLn8J8YEyDYPiM%2Bg7fy3keqtv9veqGUpq1treXglSYHLYQExNIBQo85lydvN82OKjDFqnuXljVXJrZucKvT3RcZrAyS1szbSZin5Pfkdv2T7nasNEDPpTI%2FpFAazCZm7PTBjqkAS454nsWrl7Zf1OTDv%2FFcstzAHEdlQMpuadMqopZuaFOEO%2BHC79n1Ac0YNLTP4Bx5Ri1wK%2FzMwUa8b%2BwkfmY3IGJDwUXj9gvDaESKzmKXHUveD5tiBz23cB9QSuuSzU0NtA055gEsqQgU9SXuRQ%2FgTM16%2FdfMRuZwSEF9xN7WQCSUrGmy7Qcw1PSHt1zAWGq4oCi5BjvGGogKcc3loP5AOas%2B82K&X-Amz-Signature=6516e1881dc1d08c478d3dd467c06baa2f81c0c87c544333eafa5bb1559578da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4CZM4T3%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T205200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyrAT3KMp4jJhcmQlkLrTU6msGAb24yRIYryNmtxpumAIhAKFR3P7JAhF6xSDz5AA5cS44QS%2FsgckMi0jFvyfUogn%2FKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6kBWDceF4r4xkDycq3AM7JO6ovPhTfI6Idxfg%2BgpzMeBonervVTmZLCBC4gjEeI0%2BxCrbzd%2FB%2FpBP%2BSJCEYOyLxyNkCTkxwYw%2FDaCbo%2BO%2FQV6eRokBJZkaRGNQA0zZ6IGyeP51kx8s0qLpZhSCCR4BpKde3HZ0mWCz0MjVmWlYI7%2FpkBimeVrEFS%2BcIdvl%2BSI7UBVsm5YhB%2FE3RLpewARnZ6THkxWJZ%2Fc72KJx3iyu4x066xkzTMiog9Eu64BedEDegDtrAv4R1vUAvfTNltRGiH7FHOjM1sfOdBTDvITd%2FT5bLTRjLDXhyi2q4J3Y%2FUngHvmMRY1KCibCG4GcKmR1v7uRxldWSCQ%2FgSUjWvV0EymJjOUdwMc3UlJY2sGq3jEf8RwyDtt2kQ1SqWVf%2FQGGm0Q5W%2BUPjmmPWE1gGJHT%2FQFm%2BUxUk3st3d0s19b70BckH7pe8R%2BDgnnWadLC2MavJ82donHn1tJjcWuC4rtGHnKIt%2FfEYycYspk9nnrAK47XZmiwq7txb42LJoGfyBLn8J8YEyDYPiM%2Bg7fy3keqtv9veqGUpq1treXglSYHLYQExNIBQo85lydvN82OKjDFqnuXljVXJrZucKvT3RcZrAyS1szbSZin5Pfkdv2T7nasNEDPpTI%2FpFAazCZm7PTBjqkAS454nsWrl7Zf1OTDv%2FFcstzAHEdlQMpuadMqopZuaFOEO%2BHC79n1Ac0YNLTP4Bx5Ri1wK%2FzMwUa8b%2BwkfmY3IGJDwUXj9gvDaESKzmKXHUveD5tiBz23cB9QSuuSzU0NtA055gEsqQgU9SXuRQ%2FgTM16%2FdfMRuZwSEF9xN7WQCSUrGmy7Qcw1PSHt1zAWGq4oCi5BjvGGogKcc3loP5AOas%2B82K&X-Amz-Signature=88ef9388af2f330111ccc4e912f08e36a2f702dbc1c59803d21dd985b414015f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
