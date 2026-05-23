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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIEFAAAY%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T203922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGc%2FQ6xVHxxizegmv2PayEZ92g7TkQSGyUEHbvdiaZzXAiAd0Hi1f3A9kgBghqI7tzQS7ZAemCJSMZuk47dD%2FTMguir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMeuEVW%2FbxpsTdDlZJKtwD8SFttbLGd8uHyXMu6I0fgi5rmxKt8zNqAVtiUMZYRg5YnMKmH0yxpOyH6RYi%2BQ0nfbKOrCEMP%2BTmNeAlm7Q6s5Ag7S3miOVYcXZQsDkqgVIPkBwYQzBT5YWOue%2B1BkyHqWuwWwHtSaUP%2B9DmidiNSXIgX26XhuNGFlyHPsv7YfGpRLWvpwn%2BRB3bcRW72CfGW25yG3iRXnB96qnfcJ1LsXkFLiO9cyA4G%2BtkDXvq6FPRbc1sC5umHVB7d5216EMgUi3WHB7fdi1O75fICGeJLq%2B6wRpig3A6SGNiQXObINcx0amQVGYhE1l%2FbKzy7SSy%2BJHuDSDswZSZhnSC8S1mtj8Z2QTLJ7TNhNINUuSg6W5FwYxkZpILiGy03B6AhAr%2FmaWIVVTqRe1Nm6xJce778ubrbtnjTWbQkvE726sNHdc2MX79z5UYwh6krOgOUpbHM9%2FBPnUho9jjrC1scC%2Fm4g7SrglrNKX%2FWYFn1wagZ9ietWEVILi54E3uQRrrsEE624sWx9NHh87heSE7%2Ff7IQgiyzi66CnE05ficEOnq89cUU8NhdylGyUxXI9X%2BEjtSug1yoX1mrwiu%2BMHE%2BQToEDhqGi994kURlY%2FzskcYwz1wjRHvQntWX4Q0DH8w2Z3H0AY6pgHvs0iEOU5tYbM4EUz7Lj%2FoCYy6HIEzl2IFIPcdcPHXoOLW8gq%2BWNOCdJS98%2FpmdIF8Clp9CSBUQ2iPWCH7sLnT0sy5JLcY%2BdGbyTWlCMkhtgpD12GHcPdnQ9EHU%2B3Jl1SUbyjIL5RZejNGTnB%2FYNjP59gNGUPLwVwc5z6FD0nMeTnzGvTq%2BJB9T5Jybo0gZwz78oI5Go%2FtUjHM9IN2MT%2FOSrPJOo%2BK&X-Amz-Signature=eb341b06c1c76fd9a7073d1d22d3c78cb8271f7ec416cbf24604973acca00e0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIEFAAAY%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T203922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGc%2FQ6xVHxxizegmv2PayEZ92g7TkQSGyUEHbvdiaZzXAiAd0Hi1f3A9kgBghqI7tzQS7ZAemCJSMZuk47dD%2FTMguir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMeuEVW%2FbxpsTdDlZJKtwD8SFttbLGd8uHyXMu6I0fgi5rmxKt8zNqAVtiUMZYRg5YnMKmH0yxpOyH6RYi%2BQ0nfbKOrCEMP%2BTmNeAlm7Q6s5Ag7S3miOVYcXZQsDkqgVIPkBwYQzBT5YWOue%2B1BkyHqWuwWwHtSaUP%2B9DmidiNSXIgX26XhuNGFlyHPsv7YfGpRLWvpwn%2BRB3bcRW72CfGW25yG3iRXnB96qnfcJ1LsXkFLiO9cyA4G%2BtkDXvq6FPRbc1sC5umHVB7d5216EMgUi3WHB7fdi1O75fICGeJLq%2B6wRpig3A6SGNiQXObINcx0amQVGYhE1l%2FbKzy7SSy%2BJHuDSDswZSZhnSC8S1mtj8Z2QTLJ7TNhNINUuSg6W5FwYxkZpILiGy03B6AhAr%2FmaWIVVTqRe1Nm6xJce778ubrbtnjTWbQkvE726sNHdc2MX79z5UYwh6krOgOUpbHM9%2FBPnUho9jjrC1scC%2Fm4g7SrglrNKX%2FWYFn1wagZ9ietWEVILi54E3uQRrrsEE624sWx9NHh87heSE7%2Ff7IQgiyzi66CnE05ficEOnq89cUU8NhdylGyUxXI9X%2BEjtSug1yoX1mrwiu%2BMHE%2BQToEDhqGi994kURlY%2FzskcYwz1wjRHvQntWX4Q0DH8w2Z3H0AY6pgHvs0iEOU5tYbM4EUz7Lj%2FoCYy6HIEzl2IFIPcdcPHXoOLW8gq%2BWNOCdJS98%2FpmdIF8Clp9CSBUQ2iPWCH7sLnT0sy5JLcY%2BdGbyTWlCMkhtgpD12GHcPdnQ9EHU%2B3Jl1SUbyjIL5RZejNGTnB%2FYNjP59gNGUPLwVwc5z6FD0nMeTnzGvTq%2BJB9T5Jybo0gZwz78oI5Go%2FtUjHM9IN2MT%2FOSrPJOo%2BK&X-Amz-Signature=6163845096a2945522f8afe6c43a9e0579690aee736a4b642fefb4c8868c39e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
