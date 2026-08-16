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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWSYZ233%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T062018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIHneW4Lotn91JC2yVJLC9ugMepYMkJmCiyb3za2VrN3YAiA%2FWX9rx%2BVbvF1xiBfRDeth1TPodr9o%2Bmz2gjEsxBoeJir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMqxQq4TXDcKOuKavSKtwDnrOQRd4qB6Y4oETRgwD2mdTx%2FE70RaZql4CpdId3c9AAuzJo%2Bklz5T9OScXiSdD15FYZSQft7J9XPqD4nchWPJF1DVLn1ooY%2BtuYUL5womREh3pW7Altwg4a5T%2F4z%2FSHkzf5FrBOersY6CnWpl0TqIDZKatWn5fYsGPPtXI92On7Uyxp3HU9QBdrUfnoYY6zc9uMa477LBwc3soo7DKAN8hURQ1YJ7WsaGrTotWKvHc9oDjcg8ffw3qe9NwzoykjoPHNEdri9yeik2rvRLZCuwXT6Zqc5ETasBXKTG7HoccpyCrxMrZhMpAWMdm2Cen1FSGCN5kuz0x2ITo4sIIhotDLLBcUSif%2BuK2GiieHEkItrhYhemg%2F4Ha%2B1un5r1gHwTPEkuaDpUfWA1cEKQIqFmo161iso73Mgbe39KuEqkQsERH98joeSyw%2BJzi7zb%2FXNQApSRJaKSleLiI8myDneAnOBbO%2FV4FIBDd6x%2Fr6BPA2x1BcIpm91Qg6EuxO6fdVZ6Usuk8erNZ8VRJQUdXeFqmXBXOjcD7VmPXhxQFnNvtjGH4a4CvyLLVTAbzpcAlqM0%2FqJuolii7taqkSWYJFFvdLrgvtK5i5qCyk%2BIMmezYLiWJvvE5yzegV2Bcw34KF1AY6pgEcUm6SvtahjUlCjndnB%2BzFwx4mYH03iZQJKrgL9Pe3Xbfk%2BQeBh6k%2Fu0GNlwjc9Sb62rt5LrcCRkjYHfO%2F2gns%2F3XUqerDBaHvQBgWdScKEX%2FIEFkxaZ7g9daEVL5eMR%2FXRSXHUr5Y5BSl3btshuhCvF9W5xNRVX%2BHZujSsD5qi4b6aDeE4wb4fQXDyPe%2F9y4%2BbP92u%2Fk3aN5Mkctl979xHecrcyxU&X-Amz-Signature=031bcefbffd77bcaec2b9f5da789d06a13d8cb9f77c8c6ca05e60aa5e772047c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWSYZ233%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T062018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIHneW4Lotn91JC2yVJLC9ugMepYMkJmCiyb3za2VrN3YAiA%2FWX9rx%2BVbvF1xiBfRDeth1TPodr9o%2Bmz2gjEsxBoeJir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMqxQq4TXDcKOuKavSKtwDnrOQRd4qB6Y4oETRgwD2mdTx%2FE70RaZql4CpdId3c9AAuzJo%2Bklz5T9OScXiSdD15FYZSQft7J9XPqD4nchWPJF1DVLn1ooY%2BtuYUL5womREh3pW7Altwg4a5T%2F4z%2FSHkzf5FrBOersY6CnWpl0TqIDZKatWn5fYsGPPtXI92On7Uyxp3HU9QBdrUfnoYY6zc9uMa477LBwc3soo7DKAN8hURQ1YJ7WsaGrTotWKvHc9oDjcg8ffw3qe9NwzoykjoPHNEdri9yeik2rvRLZCuwXT6Zqc5ETasBXKTG7HoccpyCrxMrZhMpAWMdm2Cen1FSGCN5kuz0x2ITo4sIIhotDLLBcUSif%2BuK2GiieHEkItrhYhemg%2F4Ha%2B1un5r1gHwTPEkuaDpUfWA1cEKQIqFmo161iso73Mgbe39KuEqkQsERH98joeSyw%2BJzi7zb%2FXNQApSRJaKSleLiI8myDneAnOBbO%2FV4FIBDd6x%2Fr6BPA2x1BcIpm91Qg6EuxO6fdVZ6Usuk8erNZ8VRJQUdXeFqmXBXOjcD7VmPXhxQFnNvtjGH4a4CvyLLVTAbzpcAlqM0%2FqJuolii7taqkSWYJFFvdLrgvtK5i5qCyk%2BIMmezYLiWJvvE5yzegV2Bcw34KF1AY6pgEcUm6SvtahjUlCjndnB%2BzFwx4mYH03iZQJKrgL9Pe3Xbfk%2BQeBh6k%2Fu0GNlwjc9Sb62rt5LrcCRkjYHfO%2F2gns%2F3XUqerDBaHvQBgWdScKEX%2FIEFkxaZ7g9daEVL5eMR%2FXRSXHUr5Y5BSl3btshuhCvF9W5xNRVX%2BHZujSsD5qi4b6aDeE4wb4fQXDyPe%2F9y4%2BbP92u%2Fk3aN5Mkctl979xHecrcyxU&X-Amz-Signature=3970117c1b4674307e978603b21fbd83a3ab0877c98f6be3b4ac40a03e1fa32f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
