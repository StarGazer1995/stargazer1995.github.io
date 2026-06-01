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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JLLTVDW%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T232223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIG4OY2QwQRu3%2Bzpn%2BUCjRIT1J3kLL2UA1pLqBk4ADuPrAiEAmMrNHm52BKprUlPmgOyI%2BZhmutzSp9PCGP%2BCfT%2BbHZwq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDIV9cZzU8%2F1Ef%2Bs0GircA3Ntw8d69kS%2Fy63uIqkrTZx4jaS0cn6W%2B%2F28kAADFtgbw8wz8ZwrHvWFq3ixhCwBgjk11W58M9iXJF%2FXj6cBLj2Rhu%2B7%2FXqxX1Evp0vrcWVcgsVVjBkoZ%2BJAHzXjPhqaBVxv6lVIuhdCu2vZ0kqh6Vgu8mt0%2BpVRh9L%2FpP1qrA5ruzh2xuAq2tjsulS2kbK1UlMafKbLrHZxJsHka%2FB3j1bMHStAVjY9Y4KLLVmd8pu0Ab8Wqz90PmuDn986Fnec%2Fe5aATn8%2FgFvxCCjgGYTUEWWynI5wOYKd9i8CVOMt37B4gNZX0T8r5AmLQwldOn353%2FCNhlrpNAMSG1Twvmw7cH%2FBJNKGVvVfeU%2FVEww%2BHkCjacuVEz%2F40IPvDdGRqy12rJ2Bsq3TgsRydsLwRc2Y0FqOXzjbMspX76dzRZrpM2WiXVBkp7ApYVVN0NIkrX0qrJ5ucD3nvrBSVESa0WgtgTBBDW8%2BlgnjswEEUSSXb2FK%2FEMsDMtAIHyatPUrVTjtj3NT0%2BEgNE%2BYMJiQKVCG%2BdNt6b0CkYWIB5XvrBjmb%2Bi90qASxmPolj2T1iOWoHh64dpM6i2BbDfXWXvUTN7Rt8yuga66QWna5tHn%2B2ltwj1iHDtBLGTzI3xb5%2BCMOuF%2BNAGOqUB8gfJBe%2BCRGnmO1jnUCrefRwdH86yphGCy33OtbQm1JP4fAaWsSzz84nObe66tbVf3%2BhfJoSIGFSlyPgDp2%2BXUAaJHRLTV8T1s7ReJVQADXE1%2FgVncBxAiH4RrY6u3KqueqjJgxsN5HfXzSuOFMVAEUgEapISKvqbNatrQuecfLkEhadXwBi34z0Qbwctkw4hipOHw5v8jyzNBzfFGFrm%2FCBsx1Tf&X-Amz-Signature=b10124e4943bd4aedc51cd1e923003478b65bab217b180508f5d978de0a01eac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JLLTVDW%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T232223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIG4OY2QwQRu3%2Bzpn%2BUCjRIT1J3kLL2UA1pLqBk4ADuPrAiEAmMrNHm52BKprUlPmgOyI%2BZhmutzSp9PCGP%2BCfT%2BbHZwq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDIV9cZzU8%2F1Ef%2Bs0GircA3Ntw8d69kS%2Fy63uIqkrTZx4jaS0cn6W%2B%2F28kAADFtgbw8wz8ZwrHvWFq3ixhCwBgjk11W58M9iXJF%2FXj6cBLj2Rhu%2B7%2FXqxX1Evp0vrcWVcgsVVjBkoZ%2BJAHzXjPhqaBVxv6lVIuhdCu2vZ0kqh6Vgu8mt0%2BpVRh9L%2FpP1qrA5ruzh2xuAq2tjsulS2kbK1UlMafKbLrHZxJsHka%2FB3j1bMHStAVjY9Y4KLLVmd8pu0Ab8Wqz90PmuDn986Fnec%2Fe5aATn8%2FgFvxCCjgGYTUEWWynI5wOYKd9i8CVOMt37B4gNZX0T8r5AmLQwldOn353%2FCNhlrpNAMSG1Twvmw7cH%2FBJNKGVvVfeU%2FVEww%2BHkCjacuVEz%2F40IPvDdGRqy12rJ2Bsq3TgsRydsLwRc2Y0FqOXzjbMspX76dzRZrpM2WiXVBkp7ApYVVN0NIkrX0qrJ5ucD3nvrBSVESa0WgtgTBBDW8%2BlgnjswEEUSSXb2FK%2FEMsDMtAIHyatPUrVTjtj3NT0%2BEgNE%2BYMJiQKVCG%2BdNt6b0CkYWIB5XvrBjmb%2Bi90qASxmPolj2T1iOWoHh64dpM6i2BbDfXWXvUTN7Rt8yuga66QWna5tHn%2B2ltwj1iHDtBLGTzI3xb5%2BCMOuF%2BNAGOqUB8gfJBe%2BCRGnmO1jnUCrefRwdH86yphGCy33OtbQm1JP4fAaWsSzz84nObe66tbVf3%2BhfJoSIGFSlyPgDp2%2BXUAaJHRLTV8T1s7ReJVQADXE1%2FgVncBxAiH4RrY6u3KqueqjJgxsN5HfXzSuOFMVAEUgEapISKvqbNatrQuecfLkEhadXwBi34z0Qbwctkw4hipOHw5v8jyzNBzfFGFrm%2FCBsx1Tf&X-Amz-Signature=33956b9e0b448bdb2e2a2806ac59d355b67dc0b901c1518dde8049513709536e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
