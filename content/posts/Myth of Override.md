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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TGTJFXY%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7xA6njl9MR2vUOJHwZO8gaeB2susjdF6vpDRRi1H8swIhANlIAlIikp4Yq%2FimtJNGwonNmaw%2BdpOA1Y%2BLtBpV8tn3Kv8DCGYQABoMNjM3NDIzMTgzODA1IgzY%2BNMkrvRhdJjfEzEq3AO8843nViBNMQgEbR0T16BxZSdjVKAZRyOwvDSZJG9IpbeRsIjYBJBS94nRG2Uz%2BvaB4A3xLjVx4VbI%2B%2BhWW8D%2FO6yrV0xp0cGOTwR1r29o2AHMR9agpSID9CnD9mUJ4X2LSwXf%2BIDwerMipjDPhh5%2BXY%2BG6tNLJktG3iEf9Y5SN3tQ%2BAYutUu0CsX9GkGNgujE69UyAVwz0iyHo3Mc4uYPDm8ApU2FIKiZK0y3FJ4vOwwENu%2Bx1ba9RwmZij3Df%2B9DuRCEX5o%2FFBstPlb6SK3FnSnzyHiiy0W6g2WcrJfHKohcGkA7ly9BgvD4LDFBj4iNZmbMXLtcctXguo8ob8jWOuIGoyjPut7i7KGP83Mx%2BZa2f7EHGQyWaPBuKrSq%2B7pFi5BTL6sYyFTMm4p0qRypKn5IefaReQZd7HQxNN8fqb009pI1068eToZUqmRXnWdpPsFI875xJYTzupNXKYWujFZc50cMVqlnAvPZNJBeECpsxaoWwHq8xKwSQhzS9i61FZfFKE6RjXYgGZmhb8PfarrSGUxJQevOwXCXAi3EFnjJoNhgYkHXb7SZsxG5ocBNtDMrx0Jw1tz%2BczxJdzwof2P3WlON02lxIzp%2FBCatoW3%2FAs8KVWZVC6FSnTDe0aLTBjqkAX9oEclO4e6KNRDD52Xy2AK5n3MZXYeqeaMyCCDbgYqTkXzSus4WjlaFVeYXme9QzvNBptP8qyVZc0DBgHZoEEOhM6C%2FBF3HpCSyRX0hGsZHVwVnP3bbPyVU04foovMW1lpl1LaczXaX2I0%2F%2BvWIXuHab8YxYu0tDIPMuNZpwsMha7ml68KUM%2FBEXOSe9SwwK8ANvu9Z6lMitMOsaZYbkjd7TH6f&X-Amz-Signature=cc5c62c8dfe669b2b5352cc9eb0af5364dfdbeea7c99055c9a36c12f08f9456a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TGTJFXY%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7xA6njl9MR2vUOJHwZO8gaeB2susjdF6vpDRRi1H8swIhANlIAlIikp4Yq%2FimtJNGwonNmaw%2BdpOA1Y%2BLtBpV8tn3Kv8DCGYQABoMNjM3NDIzMTgzODA1IgzY%2BNMkrvRhdJjfEzEq3AO8843nViBNMQgEbR0T16BxZSdjVKAZRyOwvDSZJG9IpbeRsIjYBJBS94nRG2Uz%2BvaB4A3xLjVx4VbI%2B%2BhWW8D%2FO6yrV0xp0cGOTwR1r29o2AHMR9agpSID9CnD9mUJ4X2LSwXf%2BIDwerMipjDPhh5%2BXY%2BG6tNLJktG3iEf9Y5SN3tQ%2BAYutUu0CsX9GkGNgujE69UyAVwz0iyHo3Mc4uYPDm8ApU2FIKiZK0y3FJ4vOwwENu%2Bx1ba9RwmZij3Df%2B9DuRCEX5o%2FFBstPlb6SK3FnSnzyHiiy0W6g2WcrJfHKohcGkA7ly9BgvD4LDFBj4iNZmbMXLtcctXguo8ob8jWOuIGoyjPut7i7KGP83Mx%2BZa2f7EHGQyWaPBuKrSq%2B7pFi5BTL6sYyFTMm4p0qRypKn5IefaReQZd7HQxNN8fqb009pI1068eToZUqmRXnWdpPsFI875xJYTzupNXKYWujFZc50cMVqlnAvPZNJBeECpsxaoWwHq8xKwSQhzS9i61FZfFKE6RjXYgGZmhb8PfarrSGUxJQevOwXCXAi3EFnjJoNhgYkHXb7SZsxG5ocBNtDMrx0Jw1tz%2BczxJdzwof2P3WlON02lxIzp%2FBCatoW3%2FAs8KVWZVC6FSnTDe0aLTBjqkAX9oEclO4e6KNRDD52Xy2AK5n3MZXYeqeaMyCCDbgYqTkXzSus4WjlaFVeYXme9QzvNBptP8qyVZc0DBgHZoEEOhM6C%2FBF3HpCSyRX0hGsZHVwVnP3bbPyVU04foovMW1lpl1LaczXaX2I0%2F%2BvWIXuHab8YxYu0tDIPMuNZpwsMha7ml68KUM%2FBEXOSe9SwwK8ANvu9Z6lMitMOsaZYbkjd7TH6f&X-Amz-Signature=78a9a88506669469fd1fd8d7d1434d18a47b986e4c591fad6d945a361fabc799&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
