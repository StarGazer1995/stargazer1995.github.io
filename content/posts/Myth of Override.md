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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUABDN3%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T183739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVnnkYb6ySWZuTZr8qJnANo4DPmVjS%2FRCg2Q3bA5YYaAiEA2D1oT4U%2B1XpP4OJ2PaLHAKgSleZ5nXcdnrOAifhBKXwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGoscYVJobhSnw%2FLCircA4CWpTYFFusq7l%2FbCuxpYIgOhUUH7BfR5daYZyD%2F6SsV7KUlBxUmckjduUyVlzzNwZemSsB%2Ftop%2FDNVY5kb79PuChrN%2BG6xLQej3OJ6zxwSy9SetYylSE8RGwZm1zFNqsdQPgOgoNju9CBoV8gnA7%2F8pnDzBiB5MYfznx7Mf6vlvBAHQUWQZFGl1Q62JBEM3PX%2BzG9gFlnG%2Bn3GShWzGUkXgOLEr2hhGPvx7b%2Btrzr%2BV%2FI44CTWMG1PtuJNfNLxhgwkddaAyVd5Tc2lXri%2BU1hl3A9N8boctEFKkKJDDMfuKQa5%2FqxiNU3ZJYGivoPfymkbeBTOfNkV0J45hzc6APZHpr%2FP7D7dvOJdBCFsh8u03tnZ4GsSNhv5laVgdqjWuJ8LkxQb5NaeTWn5vI5Ivkfg0qmfZV7k%2B0YN7UeY%2BG%2Fq5%2FwT96X2npZM7%2Fpb7oAD1TCHf%2FYHkGHWigCLCVgFkJBkHyoGYkt9KZMRvJFZ3vY%2BTFKNf3uoMO8WWiWj%2BvQRdPL3q6nx4JaQo2byYCJol%2FQ%2BSJ%2BGDTKEyc8LcUAnfIWDba6viRSVwqBhAATxRfV8cn9THHTOFxNs3MWptOjIzutIel%2F8%2BhYEcNwoJ4B%2By5EMjqRHcAVm7MI1%2FSvZfMLCW2NMGOqUB5OfpN27qmm9T80aIcwWfZ2IXdirD8rZFwnqyCR9eCWWagg3cX3qWFh6CZ66gBrvo3ZVzSI7Pv7WV3FAowGmq29i9zdlUJRNHKhp%2FQ3bm%2BPJhtWN5Fw5ilr2OTlQKych%2BuCziiX3xKLC%2BH2AvKYiNoIzh5hOKjdhLeH6TIe%2BIDrUMu6k1PHlk%2FS5DznoSiJtHg92XmvQbgzKujrjsabg4VxTVxyCD&X-Amz-Signature=b790c3dd73e49ee3d9cb0f9b9355614fc7a945ca4c67fab7f38b86d632d192bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUABDN3%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T183739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVnnkYb6ySWZuTZr8qJnANo4DPmVjS%2FRCg2Q3bA5YYaAiEA2D1oT4U%2B1XpP4OJ2PaLHAKgSleZ5nXcdnrOAifhBKXwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGoscYVJobhSnw%2FLCircA4CWpTYFFusq7l%2FbCuxpYIgOhUUH7BfR5daYZyD%2F6SsV7KUlBxUmckjduUyVlzzNwZemSsB%2Ftop%2FDNVY5kb79PuChrN%2BG6xLQej3OJ6zxwSy9SetYylSE8RGwZm1zFNqsdQPgOgoNju9CBoV8gnA7%2F8pnDzBiB5MYfznx7Mf6vlvBAHQUWQZFGl1Q62JBEM3PX%2BzG9gFlnG%2Bn3GShWzGUkXgOLEr2hhGPvx7b%2Btrzr%2BV%2FI44CTWMG1PtuJNfNLxhgwkddaAyVd5Tc2lXri%2BU1hl3A9N8boctEFKkKJDDMfuKQa5%2FqxiNU3ZJYGivoPfymkbeBTOfNkV0J45hzc6APZHpr%2FP7D7dvOJdBCFsh8u03tnZ4GsSNhv5laVgdqjWuJ8LkxQb5NaeTWn5vI5Ivkfg0qmfZV7k%2B0YN7UeY%2BG%2Fq5%2FwT96X2npZM7%2Fpb7oAD1TCHf%2FYHkGHWigCLCVgFkJBkHyoGYkt9KZMRvJFZ3vY%2BTFKNf3uoMO8WWiWj%2BvQRdPL3q6nx4JaQo2byYCJol%2FQ%2BSJ%2BGDTKEyc8LcUAnfIWDba6viRSVwqBhAATxRfV8cn9THHTOFxNs3MWptOjIzutIel%2F8%2BhYEcNwoJ4B%2By5EMjqRHcAVm7MI1%2FSvZfMLCW2NMGOqUB5OfpN27qmm9T80aIcwWfZ2IXdirD8rZFwnqyCR9eCWWagg3cX3qWFh6CZ66gBrvo3ZVzSI7Pv7WV3FAowGmq29i9zdlUJRNHKhp%2FQ3bm%2BPJhtWN5Fw5ilr2OTlQKych%2BuCziiX3xKLC%2BH2AvKYiNoIzh5hOKjdhLeH6TIe%2BIDrUMu6k1PHlk%2FS5DznoSiJtHg92XmvQbgzKujrjsabg4VxTVxyCD&X-Amz-Signature=9814c66469eda04e198bceab7cc7115004b1f4cd004b974cb9cadd2378d2b1f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
