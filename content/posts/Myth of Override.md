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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Y2CKCFL%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T231421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIEOy4Iy0xE3TAA9lT%2FY8Bi6UmlxTCMAAQU%2Bj%2FupK5ncMAiB8HeoDxXvV8N5EhOeDW5%2Bz%2B6k2%2Fzkn8gy9hayHP6B6JSr%2FAwgHEAAaDDYzNzQyMzE4MzgwNSIMvQZbfZp1dAyBELBuKtwDTbTHKIPMvozwNwxOSXAdNfmBhK%2BrISnFdJPmUNbONgAWd8CFn2cQI1a3Obpg3pPxJK0ST2w4HNtCBFOVyj6hqoNbdM3FYIOC13%2FYDPuLBbbW2v%2FmU7ilhbGyJa1da0KA167ClqxjOnBrzELOvUcGzEXfCBcSeJRpmZekLXo4ZMQiB3jBJB6qh%2FSCm2Y3k91%2BaMk6mouzyNuXnUYkGs2tp3ixBj0p%2BUAK6IN962tLgDqWWjyQrseQuUMFtZaEABJKaR3uID4M9WaU%2B0qiTzhno59pip8Nzla6QQm0zVHtxD2iRPBq%2BgkP9dcGZaNLtO2wm6vtnAzy8h%2FZd83WYz%2B52%2BpBxoePfiDMmvcX9BGd6GSNYBKgSh8HEkiK1UWNNfPsMaACGOeZr50nhfC7n2V0UmX4hGMs0q%2BanUlHOcMbxyI43GdzQgxuF284jN4wO7uTlsym3N%2Bii4RGqULIYOUEq%2BSa7JFFxX5pqckB3DlGIS9EUEW%2FpuvAwvaQPBkvOEVArqbYby890TZMWL%2BiQCIA%2FxYgnmVIVdcxdi7ZMzHMV2zTekUc5VswxlJj0CX6n3e9qb8xT5zfWMgbzoJ5zLaVPDne9zIk%2B%2BfR3pEJ2KBTAiG90QaZfnh3mcqVolgwt9Ks0QY6pgEVY%2BtI%2FtnHRO90mPsJ05qg%2FQgG7yG8Ro%2Fr4ViyhaDInkvfonTaK7p9IwDPBmqFMjBpyQ0lnF8BGid1x58cxdnw%2FXqqq%2BRKLz7gv44Pnuzkd%2FLxGRtt9KGz%2FuoKXhq0gRL0XFTQn7U0TdzEwZ4AasAbi3uiqdzXbnTk2JI3k9rMeJbmZPlSc9LP4MgdKaUZK8tEf%2BGjuTBQEnOmDToputcnqR%2BsfgzH&X-Amz-Signature=74ac22192a04d23a48a01b2e2142fceb6009a7f9c007b2bee914a413937e6f85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Y2CKCFL%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T231421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIEOy4Iy0xE3TAA9lT%2FY8Bi6UmlxTCMAAQU%2Bj%2FupK5ncMAiB8HeoDxXvV8N5EhOeDW5%2Bz%2B6k2%2Fzkn8gy9hayHP6B6JSr%2FAwgHEAAaDDYzNzQyMzE4MzgwNSIMvQZbfZp1dAyBELBuKtwDTbTHKIPMvozwNwxOSXAdNfmBhK%2BrISnFdJPmUNbONgAWd8CFn2cQI1a3Obpg3pPxJK0ST2w4HNtCBFOVyj6hqoNbdM3FYIOC13%2FYDPuLBbbW2v%2FmU7ilhbGyJa1da0KA167ClqxjOnBrzELOvUcGzEXfCBcSeJRpmZekLXo4ZMQiB3jBJB6qh%2FSCm2Y3k91%2BaMk6mouzyNuXnUYkGs2tp3ixBj0p%2BUAK6IN962tLgDqWWjyQrseQuUMFtZaEABJKaR3uID4M9WaU%2B0qiTzhno59pip8Nzla6QQm0zVHtxD2iRPBq%2BgkP9dcGZaNLtO2wm6vtnAzy8h%2FZd83WYz%2B52%2BpBxoePfiDMmvcX9BGd6GSNYBKgSh8HEkiK1UWNNfPsMaACGOeZr50nhfC7n2V0UmX4hGMs0q%2BanUlHOcMbxyI43GdzQgxuF284jN4wO7uTlsym3N%2Bii4RGqULIYOUEq%2BSa7JFFxX5pqckB3DlGIS9EUEW%2FpuvAwvaQPBkvOEVArqbYby890TZMWL%2BiQCIA%2FxYgnmVIVdcxdi7ZMzHMV2zTekUc5VswxlJj0CX6n3e9qb8xT5zfWMgbzoJ5zLaVPDne9zIk%2B%2BfR3pEJ2KBTAiG90QaZfnh3mcqVolgwt9Ks0QY6pgEVY%2BtI%2FtnHRO90mPsJ05qg%2FQgG7yG8Ro%2Fr4ViyhaDInkvfonTaK7p9IwDPBmqFMjBpyQ0lnF8BGid1x58cxdnw%2FXqqq%2BRKLz7gv44Pnuzkd%2FLxGRtt9KGz%2FuoKXhq0gRL0XFTQn7U0TdzEwZ4AasAbi3uiqdzXbnTk2JI3k9rMeJbmZPlSc9LP4MgdKaUZK8tEf%2BGjuTBQEnOmDToputcnqR%2BsfgzH&X-Amz-Signature=1a178f4fc73a475988e56753019c08458aa8e5b574a8e4d6f3fe00fd9862a6e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
