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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVSUSHB%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T082117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIBep5NGpC60HSUwn4DB0EVvmukg%2BePCYWevIPgLnFYGRAiBeFnYoarPEQfZ9PYI6eROwmJWXJRfI8WcEIF9aiEhaLiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPgP0AkdxRYXO3XBXKtwDTyQgFE4ENTwrsW3SfyMkNYUuqGpNrIHCndSAUPnC2iKsO21xuRtzMF65eSWyGI6XY28QOz%2FHKIBfgw%2Fh2%2F53WrNMuHu7Ni8Iri4TMTdMQINUW%2FxdvJXQtnaA5NJqW1f%2FFBYnip4Yhvq7HIlp0Jnx0mfYeroHVDWOclFEYQll%2BUIMQo9XlNHWdIcy3oP3MRleuLaAkNEBTA%2FpOPZTrmXtZvlpp01AYIkWNZjxtOLL9nDXU2aFEzWnsE%2F5Ma9aXzINESl%2FG8uk%2BL7lJabBPbHXBlIgkSs0nhDh8iXYQtOQ2SzglPVVtWZB2juXt2Wi%2BE35YbciXBxsYtV6fdt%2FDIWje5f2svU5kAeOC9o5ot4k4nXlIWL5OHJEqUJqxlC7o%2BPeHaK4lnBw1jxFddpL0qQ3CI7e8uPkI3dk%2BTZifYiG8ObjA8rW45lu5JXwVRvVycr3dDQqONz2uCYTQOpih1M%2Fi4kGt%2B313ZQUwHfdi1voo5pt%2Fq03EyYOSNC8UkIctCJnp5CGyyX%2FvOLUlOM%2FZcFmyQPuSGHnq%2B4KJPeu1tzjOh1TtYxkt7PHOsaHXShGfQGB6IskJeDmlABPDf52RZOx7s1DUpQEguy9Fh%2FXozHraEJFAt%2FRm2NSD%2FxEsfMwtoDe0QY6pgGLUivR332BTKIKOvJ7TZKGwL82Spu1iFXGukyCVoDKDnN14zRM%2BOyen%2FKWUAQ6gD4bDApiAbuh6OAh4DBBxvnrv4I0TPq1upByg%2FcF4JTRIzBe18nIVkcLys7QSlAxlmf6u3XqrszGGDVl%2FJHJ%2FZIj1glHvZFaLjOv3tX8E3Bmarccny7pmOV%2FuuwtlKUvcqX0dt%2Bnl%2BDQ3Mi6Cg14hGPpN4HGhAdQ&X-Amz-Signature=4549e1cb4cfadb0752c8a033b25f4310aca03b5fb796c6cf4dd62cfc16d970d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVSUSHB%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T082117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIBep5NGpC60HSUwn4DB0EVvmukg%2BePCYWevIPgLnFYGRAiBeFnYoarPEQfZ9PYI6eROwmJWXJRfI8WcEIF9aiEhaLiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPgP0AkdxRYXO3XBXKtwDTyQgFE4ENTwrsW3SfyMkNYUuqGpNrIHCndSAUPnC2iKsO21xuRtzMF65eSWyGI6XY28QOz%2FHKIBfgw%2Fh2%2F53WrNMuHu7Ni8Iri4TMTdMQINUW%2FxdvJXQtnaA5NJqW1f%2FFBYnip4Yhvq7HIlp0Jnx0mfYeroHVDWOclFEYQll%2BUIMQo9XlNHWdIcy3oP3MRleuLaAkNEBTA%2FpOPZTrmXtZvlpp01AYIkWNZjxtOLL9nDXU2aFEzWnsE%2F5Ma9aXzINESl%2FG8uk%2BL7lJabBPbHXBlIgkSs0nhDh8iXYQtOQ2SzglPVVtWZB2juXt2Wi%2BE35YbciXBxsYtV6fdt%2FDIWje5f2svU5kAeOC9o5ot4k4nXlIWL5OHJEqUJqxlC7o%2BPeHaK4lnBw1jxFddpL0qQ3CI7e8uPkI3dk%2BTZifYiG8ObjA8rW45lu5JXwVRvVycr3dDQqONz2uCYTQOpih1M%2Fi4kGt%2B313ZQUwHfdi1voo5pt%2Fq03EyYOSNC8UkIctCJnp5CGyyX%2FvOLUlOM%2FZcFmyQPuSGHnq%2B4KJPeu1tzjOh1TtYxkt7PHOsaHXShGfQGB6IskJeDmlABPDf52RZOx7s1DUpQEguy9Fh%2FXozHraEJFAt%2FRm2NSD%2FxEsfMwtoDe0QY6pgGLUivR332BTKIKOvJ7TZKGwL82Spu1iFXGukyCVoDKDnN14zRM%2BOyen%2FKWUAQ6gD4bDApiAbuh6OAh4DBBxvnrv4I0TPq1upByg%2FcF4JTRIzBe18nIVkcLys7QSlAxlmf6u3XqrszGGDVl%2FJHJ%2FZIj1glHvZFaLjOv3tX8E3Bmarccny7pmOV%2FuuwtlKUvcqX0dt%2Bnl%2BDQ3Mi6Cg14hGPpN4HGhAdQ&X-Amz-Signature=f31710c4f10e91b56422b028afe35eb61ac750d90736f2efaab6940d6c7a6138&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
