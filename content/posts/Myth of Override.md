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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNJRDBEA%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T055213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDW01ARMMZBlVtzZePIClCjEitoGkNNCi7Ket6qGoxPpQIhALTXAjF7ghs4gusU6z1HHVBzny5CI1ntmQbhgBHDXjwVKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBaK30Olz5k%2Fg9E8q3AO0bCGtJWMp5SI9QLJZmMa%2FRVZALMr9m5yOB6VRfVHufEgBOin%2FxkRK%2FELZxKrvBaZ8nOPHDesoS%2B6CCa5fNkeVeUiAkQhXWZ4RW0YJlpZNn6tWQsrq3Ui1HNOK59pyv8o6V2H%2BecWrdFfPRL%2FK35DtkWNRMh%2FCGk9gYvSkvB7T9A%2FTw0WdVVP5P8MEBNO%2FiiO9QxjZXZj9S1UygJkb4LuoTiESjgh%2FlgFIxIyyM%2FWw03%2FVFHF4nlIRGdkxyV6IHh5rC%2BjLYziwhGKDR%2FWed3lN23f%2BRF9dSwmYLkL%2BFNTwN04PgkH5q%2Bk7pMeUK11pYzjBrgXooQgZPSAPUb%2FdSzhvgm9J%2B3vb8iQz4hj4d8Etvo1pZWJgrY5WaceHNAoawq9VzOdmbADqsFdvle9fgERT13STO0E5Za9ApCIltoV5cdYhSmFny07z%2BVy7xar7l0FLh%2Fe%2BOHHloGg30KY9qNGCweZUbQX2ho7qSO%2BlaQ2wOuCgjAvUFnBSwoJc6YXob7yLAVdvUFqWeWKXIc1mI7CfmLG67Lt%2Bifu11AD4Knhkl%2BdPenpMKTvPiTl2HxuPUQN40jVpzaduAEXwVkiIzzBJqUNxJt8ZMunPeAYjAhtGzDABijNr8wksvJNFMTDx6cHSBjqkAUA2FoHwCAGLnyaHCXp4sP4%2F3LmJfjkkZDIoHNb8g4Y5u1vDrv2P%2BcUyvyFMWH23uzVcVRv%2BaRGe8IFPU8hhx9JcbVxEe8VIr5nivgwcyzHavBNknw%2BWhQqs8qz8O2ND0lemagl7mP2LuNb3W2OKxS4E1z%2BHvne%2Fz5BLL%2BDxdBLcgWgHCteSZ776S7Px6sK%2F%2B6%2BuG%2FZqTtcD2ODS%2FpjK%2BcQ7a5yo&X-Amz-Signature=1a99d2a817d19b6da11f4273f95d170bbc631036acb264f256b0ad9e7996cf68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNJRDBEA%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T055213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDW01ARMMZBlVtzZePIClCjEitoGkNNCi7Ket6qGoxPpQIhALTXAjF7ghs4gusU6z1HHVBzny5CI1ntmQbhgBHDXjwVKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBaK30Olz5k%2Fg9E8q3AO0bCGtJWMp5SI9QLJZmMa%2FRVZALMr9m5yOB6VRfVHufEgBOin%2FxkRK%2FELZxKrvBaZ8nOPHDesoS%2B6CCa5fNkeVeUiAkQhXWZ4RW0YJlpZNn6tWQsrq3Ui1HNOK59pyv8o6V2H%2BecWrdFfPRL%2FK35DtkWNRMh%2FCGk9gYvSkvB7T9A%2FTw0WdVVP5P8MEBNO%2FiiO9QxjZXZj9S1UygJkb4LuoTiESjgh%2FlgFIxIyyM%2FWw03%2FVFHF4nlIRGdkxyV6IHh5rC%2BjLYziwhGKDR%2FWed3lN23f%2BRF9dSwmYLkL%2BFNTwN04PgkH5q%2Bk7pMeUK11pYzjBrgXooQgZPSAPUb%2FdSzhvgm9J%2B3vb8iQz4hj4d8Etvo1pZWJgrY5WaceHNAoawq9VzOdmbADqsFdvle9fgERT13STO0E5Za9ApCIltoV5cdYhSmFny07z%2BVy7xar7l0FLh%2Fe%2BOHHloGg30KY9qNGCweZUbQX2ho7qSO%2BlaQ2wOuCgjAvUFnBSwoJc6YXob7yLAVdvUFqWeWKXIc1mI7CfmLG67Lt%2Bifu11AD4Knhkl%2BdPenpMKTvPiTl2HxuPUQN40jVpzaduAEXwVkiIzzBJqUNxJt8ZMunPeAYjAhtGzDABijNr8wksvJNFMTDx6cHSBjqkAUA2FoHwCAGLnyaHCXp4sP4%2F3LmJfjkkZDIoHNb8g4Y5u1vDrv2P%2BcUyvyFMWH23uzVcVRv%2BaRGe8IFPU8hhx9JcbVxEe8VIr5nivgwcyzHavBNknw%2BWhQqs8qz8O2ND0lemagl7mP2LuNb3W2OKxS4E1z%2BHvne%2Fz5BLL%2BDxdBLcgWgHCteSZ776S7Px6sK%2F%2B6%2BuG%2FZqTtcD2ODS%2FpjK%2BcQ7a5yo&X-Amz-Signature=7f5f2634b5d0a3becf3f8136524091137cbef8e99c13edb12d3cb393c86bc880&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
