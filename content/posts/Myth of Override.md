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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646MG3QZF%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T211114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGfTp3ZDfv7IenGraChLaRdJDLSkwKxfa7OCjl02B%2FKoAiADWwDfWGUktAIoHEpdi8ANq312BnFV1ehulceNuvwzwiqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAR1%2B6gzFNreif6fVKtwDUE4aWqhWKWi97GGvUqqtzJVeG836uozafPaZpkbOvRNQb7pF%2ByISq5PTkHE1fJwKv1wnKzidcBhUkakVyg3Td5v9vL9h0rIPgK%2BWmqZd5pPN6miGbQEcMef%2BVJZBpIoFtLWlLy3bFXTGHZTZKhXTIVJPZzMAVNA14QG57hosISZPhIWnFR12ZQ5YQbTwMdy7JYQ%2BTg54J%2Bgd0pJCYCKqhvODrePJjW%2BKgFiv4YKO02LttpWfxdnWSW2FNEWMZpl3gu5Ah%2BVnyNKmJmqO2J0JWuCkPF9VaJOkrROPNBiZ%2BerYf%2BzIn84yRGMU3VE%2BDS8tHfia%2BRl1Rf6N2A%2BENKSSI9XfS1WHCKN8TbydGDVL6YT3xHTitn4nX5ZBdn6ZH4u9Xfp%2FqTL5kJWgKc8Z6mDNO8wGpOSozpVg0wM6Vpt%2B5eQkMfJtpe8m4QPZps3LJlZ9RaSY1dRC4MRznrJmGHcGXpbfFX3j6omfeLR9r0XG4GjNWkmpJBO6f8NuNcNQT3W06ZjZ3yo6VWruc5qPSMgVsO1duoPyXXpwuqS%2FNMFdMc9mveV7%2Bk3mvlQcsSmB3a8wvbyYoRCn4PokxsI%2BJzjx9INzUbJI9gztogP5TO%2BAj7MEZIZhF6V2c%2BeWALMw1pCz0AY6pgEHBhEV42LPS59Ya%2BxTAoCixC65DTy%2FMkLnZ6tzooxHqsMaEbWCdd2fC7I4cQgG8D6jmhhOq588wU6pOmQgUugAJqSIEUTb%2BxntsYTNhaHUB7wJxRgVLeSE039tXQvJYl14lz%2Be8%2BW8oQx6t2x5iy2KOPvf5uBnTI9JGo2rA1H8XE9bOohHCbKPPE5GFWtZ0HBSAgNSYaDL3Q8qwteRquJqiVxxhQTV&X-Amz-Signature=a58096590c259b444b4b10cf2e3a291ab8dcdf0ffd53390e900c45a7f4018f8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646MG3QZF%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T211114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGfTp3ZDfv7IenGraChLaRdJDLSkwKxfa7OCjl02B%2FKoAiADWwDfWGUktAIoHEpdi8ANq312BnFV1ehulceNuvwzwiqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAR1%2B6gzFNreif6fVKtwDUE4aWqhWKWi97GGvUqqtzJVeG836uozafPaZpkbOvRNQb7pF%2ByISq5PTkHE1fJwKv1wnKzidcBhUkakVyg3Td5v9vL9h0rIPgK%2BWmqZd5pPN6miGbQEcMef%2BVJZBpIoFtLWlLy3bFXTGHZTZKhXTIVJPZzMAVNA14QG57hosISZPhIWnFR12ZQ5YQbTwMdy7JYQ%2BTg54J%2Bgd0pJCYCKqhvODrePJjW%2BKgFiv4YKO02LttpWfxdnWSW2FNEWMZpl3gu5Ah%2BVnyNKmJmqO2J0JWuCkPF9VaJOkrROPNBiZ%2BerYf%2BzIn84yRGMU3VE%2BDS8tHfia%2BRl1Rf6N2A%2BENKSSI9XfS1WHCKN8TbydGDVL6YT3xHTitn4nX5ZBdn6ZH4u9Xfp%2FqTL5kJWgKc8Z6mDNO8wGpOSozpVg0wM6Vpt%2B5eQkMfJtpe8m4QPZps3LJlZ9RaSY1dRC4MRznrJmGHcGXpbfFX3j6omfeLR9r0XG4GjNWkmpJBO6f8NuNcNQT3W06ZjZ3yo6VWruc5qPSMgVsO1duoPyXXpwuqS%2FNMFdMc9mveV7%2Bk3mvlQcsSmB3a8wvbyYoRCn4PokxsI%2BJzjx9INzUbJI9gztogP5TO%2BAj7MEZIZhF6V2c%2BeWALMw1pCz0AY6pgEHBhEV42LPS59Ya%2BxTAoCixC65DTy%2FMkLnZ6tzooxHqsMaEbWCdd2fC7I4cQgG8D6jmhhOq588wU6pOmQgUugAJqSIEUTb%2BxntsYTNhaHUB7wJxRgVLeSE039tXQvJYl14lz%2Be8%2BW8oQx6t2x5iy2KOPvf5uBnTI9JGo2rA1H8XE9bOohHCbKPPE5GFWtZ0HBSAgNSYaDL3Q8qwteRquJqiVxxhQTV&X-Amz-Signature=ff2f053dea28b34ff2b66702b7e0cf07c04ccbe7c999bf0a654d295a4ff06ee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
