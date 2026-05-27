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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F7BUWAF%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T214434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqb13KANTbCKqtekHv2BEb5lXpnjs8DTQCxXBx5P1fawIhAN8c2PrYzlhheYoEkgwsfzE%2FY%2BNZhHCUkUzBF3T2sqxNKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwtHnoTpxAL5dvyFIEq3APUwBgODoXTUR1iP%2BLdoxowkSwHLYOwaNUvDdMYaOB%2FLysa3YNjKlR9XEPjA8q1vus%2FTfA6PsTlpDan4P%2FPu9NtyE7p2%2Bp2cHlHoEpMeNJ%2BCK4gRv3HGbT4pj%2FbOkOLunCqst5E7Sm%2FXHBAYpFfI01wKa3ZaqnAa2x%2FgKQSkqeAgQsW4jWKT4IH3C0WOKeEPl9gFyKaK6315dUveJ4DYDlkMuQdlD3nT13vnK7aFT7WoXwk08IjGXwrkDPmrWVMKkJguWEg8Cuj6FlefDWEoeCoDkDWd1SyT9jKLWXtFgBxjWBHTy2o1bKP0U1VC6IeU7veKHv3lE%2B3AqieiG5l2Fc47wr4B07rVcHY708K%2BGq6BjN31GWTwO8xm1MZ5zHAfMPsPfM8%2FgRijq1680%2Bq%2FSIaTAQ8c9Ew%2FgZYyLsDB%2FSHoe%2Bp6zIoNed0MvHOP5KLpj6u0Q2L%2BJeSI0LD48mNvKV7uT7TH1c1wvoE88qaQ0cyV80Er3OWW%2BlmyRjPx6ayiUIBtQjsqgG5s6cqcTfVYw4OsucB%2FEppih5JAmNJgdqk7QFu7nXIlW59%2BJ0m%2FPcACN1Y2xc12ZTqLy5V3UMbU2vIg5a%2FRleKZ3OJ9fIjt83JMbkdkQA3ugNXBp3g%2BTDQ%2BdzQBjqkAXHujmKmCwS1a9kM3jk3dkBi3bQHLLvyYYx84IEE2rDfrs9JpwHWGz0jb4d0hqQmN7PSj%2BzLNCtDMWcX4arh9kmQ8O7ombkiHJjMirWm7DPEsnKkrKJDQ6hTviUCaDmxAwTBn2a%2F4GJjdwsDj%2Blrkev%2FOTSTOFXHhvbFYJEtys7ftjNh7Pd53A2wFWM90qdAaXKB6sTaZ0HojNmf5rgO1gEpZduL&X-Amz-Signature=373ab485919350ba9291533aa1cba72a03aada51540751195e0a2badb3d6821f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F7BUWAF%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T214434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqb13KANTbCKqtekHv2BEb5lXpnjs8DTQCxXBx5P1fawIhAN8c2PrYzlhheYoEkgwsfzE%2FY%2BNZhHCUkUzBF3T2sqxNKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwtHnoTpxAL5dvyFIEq3APUwBgODoXTUR1iP%2BLdoxowkSwHLYOwaNUvDdMYaOB%2FLysa3YNjKlR9XEPjA8q1vus%2FTfA6PsTlpDan4P%2FPu9NtyE7p2%2Bp2cHlHoEpMeNJ%2BCK4gRv3HGbT4pj%2FbOkOLunCqst5E7Sm%2FXHBAYpFfI01wKa3ZaqnAa2x%2FgKQSkqeAgQsW4jWKT4IH3C0WOKeEPl9gFyKaK6315dUveJ4DYDlkMuQdlD3nT13vnK7aFT7WoXwk08IjGXwrkDPmrWVMKkJguWEg8Cuj6FlefDWEoeCoDkDWd1SyT9jKLWXtFgBxjWBHTy2o1bKP0U1VC6IeU7veKHv3lE%2B3AqieiG5l2Fc47wr4B07rVcHY708K%2BGq6BjN31GWTwO8xm1MZ5zHAfMPsPfM8%2FgRijq1680%2Bq%2FSIaTAQ8c9Ew%2FgZYyLsDB%2FSHoe%2Bp6zIoNed0MvHOP5KLpj6u0Q2L%2BJeSI0LD48mNvKV7uT7TH1c1wvoE88qaQ0cyV80Er3OWW%2BlmyRjPx6ayiUIBtQjsqgG5s6cqcTfVYw4OsucB%2FEppih5JAmNJgdqk7QFu7nXIlW59%2BJ0m%2FPcACN1Y2xc12ZTqLy5V3UMbU2vIg5a%2FRleKZ3OJ9fIjt83JMbkdkQA3ugNXBp3g%2BTDQ%2BdzQBjqkAXHujmKmCwS1a9kM3jk3dkBi3bQHLLvyYYx84IEE2rDfrs9JpwHWGz0jb4d0hqQmN7PSj%2BzLNCtDMWcX4arh9kmQ8O7ombkiHJjMirWm7DPEsnKkrKJDQ6hTviUCaDmxAwTBn2a%2F4GJjdwsDj%2Blrkev%2FOTSTOFXHhvbFYJEtys7ftjNh7Pd53A2wFWM90qdAaXKB6sTaZ0HojNmf5rgO1gEpZduL&X-Amz-Signature=91cf0defbced489d004b6daac5db0d006d7d51cc079eff5350f4567d9cfd2c4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
