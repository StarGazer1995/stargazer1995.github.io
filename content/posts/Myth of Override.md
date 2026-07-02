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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RMIO43%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T155936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDotvKm4hQ2gpya3%2F0cGcOcKDq%2FCTGpHQ7krm6XFUWOHwIhANlAZpLgpGnvnw25z4O2IloHpESHYCjAZWeVd92smV0cKogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwe22l4ysQ%2F%2FMqBZWwq3AN3wwm20z7S5uJ4BvwzT7q7o9fDG7tewUgIBlS4uvR6e1EdmnXtFnrMafqbRe5OPPnbClnHitIIhIeSW8MG83Ak90YkQP7NuoFOyKrtfqMUFUY%2BuhT64n%2BcjtmrlRCuzzlM8%2FQrL97BfVBppQaipG0Lu6n4dJuCfIK0WxdOHlGenNkWn2sTkhhiOAfnWS%2FsSVPDCA384hn7M0Kg5txQeftx8G57g19IhEj9rYjBS5Z4pcnCnGgy6imjnDP2WoQwIS%2BmievXQ5DePa%2BWc1%2BJxkJWcfzvQ9p%2FhT1lQe%2BNEyTEpPfJCvVHkx7B7SHz%2BptaoPx51mxgq5zDwP1FJaagqUboOsw8rwVKPaWVdnVbWQ%2FCTl5poovM2kftXADK%2FtXB40HZB%2Bn4T7gH7DBsBorppGlOSWJvlueoQ5u%2Fgsno3eNl3WUnUDYI1u5ICnH55AKy1EVJ%2BQ4gJA7EY%2FA0QJMZs33qxHSADWuSP8EewtvMpgUiZ9TxZXIQBp55gV2BOFqbBb2OaHePmRNdLNB%2F2h85kKiHYo0mCtBx52UkC2Wt4vKlS5oF47MKgchOgPOGXq0D7v3ZuB%2BGzypRzMug0ux3K9lgwWrETDBSYzVVWRLKqzpcpkvnzkxD15gvM3JjGTDq55nSBjqkASvwhTSHJ%2B%2BYg%2B25X%2BZaj87jc6m6I%2ByF%2FUPLThO1BUWJ7mStgiVQiPIXI7BADsByqp5tkGasNj2HbfOL8QBu16GYEgS2q7MrcFA972W9r3%2B%2F9yM3aZxKparwrKPsk8lSgokz83gCzAPRI61EkmfQAF2gmjlc9wsTOTmTb1T6GLQVXbhOiVlNoPaMVV79z5IOPdnFOJgchyBv59%2FQlGKJxBOUq8%2B9&X-Amz-Signature=42d5cb5415c78bde7cd436d0914c206fed52c2d1ec22a64559a74cec6aa68c54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RMIO43%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T155936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDotvKm4hQ2gpya3%2F0cGcOcKDq%2FCTGpHQ7krm6XFUWOHwIhANlAZpLgpGnvnw25z4O2IloHpESHYCjAZWeVd92smV0cKogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwe22l4ysQ%2F%2FMqBZWwq3AN3wwm20z7S5uJ4BvwzT7q7o9fDG7tewUgIBlS4uvR6e1EdmnXtFnrMafqbRe5OPPnbClnHitIIhIeSW8MG83Ak90YkQP7NuoFOyKrtfqMUFUY%2BuhT64n%2BcjtmrlRCuzzlM8%2FQrL97BfVBppQaipG0Lu6n4dJuCfIK0WxdOHlGenNkWn2sTkhhiOAfnWS%2FsSVPDCA384hn7M0Kg5txQeftx8G57g19IhEj9rYjBS5Z4pcnCnGgy6imjnDP2WoQwIS%2BmievXQ5DePa%2BWc1%2BJxkJWcfzvQ9p%2FhT1lQe%2BNEyTEpPfJCvVHkx7B7SHz%2BptaoPx51mxgq5zDwP1FJaagqUboOsw8rwVKPaWVdnVbWQ%2FCTl5poovM2kftXADK%2FtXB40HZB%2Bn4T7gH7DBsBorppGlOSWJvlueoQ5u%2Fgsno3eNl3WUnUDYI1u5ICnH55AKy1EVJ%2BQ4gJA7EY%2FA0QJMZs33qxHSADWuSP8EewtvMpgUiZ9TxZXIQBp55gV2BOFqbBb2OaHePmRNdLNB%2F2h85kKiHYo0mCtBx52UkC2Wt4vKlS5oF47MKgchOgPOGXq0D7v3ZuB%2BGzypRzMug0ux3K9lgwWrETDBSYzVVWRLKqzpcpkvnzkxD15gvM3JjGTDq55nSBjqkASvwhTSHJ%2B%2BYg%2B25X%2BZaj87jc6m6I%2ByF%2FUPLThO1BUWJ7mStgiVQiPIXI7BADsByqp5tkGasNj2HbfOL8QBu16GYEgS2q7MrcFA972W9r3%2B%2F9yM3aZxKparwrKPsk8lSgokz83gCzAPRI61EkmfQAF2gmjlc9wsTOTmTb1T6GLQVXbhOiVlNoPaMVV79z5IOPdnFOJgchyBv59%2FQlGKJxBOUq8%2B9&X-Amz-Signature=676bb230c6471ec809c997e97cd8d851d19064efdb986bf3a6f4c93c540935e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
