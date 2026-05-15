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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BGEI6VR%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T224407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJ3%2Bv7VARNSRRbymF10eIAnpd1vZrC%2FxpGEzqG7Pd4TAiAlBH38WTqXkrPiJqGxzOGfOdRISu7f9upJz6DCrYUrSiqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxwunsa%2BXnQBCCrK8KtwD3x%2FXvJKAlYkW1B3VYHUOZDe9RQNnn3bQqnPB9feiiy9VwiSPDtIDldJD2DElGRXrQ052ChAZXROqo%2FCXXt07y0lu7V8Rg%2FMLE0FQObQUVa7O0gGCfyADaDp7lgZQoJbf6uvfWnG3S58grxVUVv%2BizBkV9X7z19hboVTkEP7Xl3MP4I8EfA1h2DhMi4AKpxroyi9OjJ6H5wKz2Quw%2B1m2IpQowOddB8lvmzbltJ1%2FDWOTXPVujyDnqJ5YynMcQ%2Bv4XT7bhmiaL%2FATxuqMqB4z0zxawpwgQN6FBmavsE%2FtQeX4MAgKKmOiWPtxzY19Y%2Bn5XK1sVUXLKDDPhYw1BfYJEs0NDCx%2BOdM4XXLhzb5E%2FTKkEZEuROWws7D%2FmK1DYqtYejEZKw36xi3DLGJ24N1R0DVm5XGAlkLZSPd%2FHC2q6cLzDNTC69affmm1R%2FZFUkvfDxSd2kE45e0B%2FdpWdSf6mn5az%2FrwTD2FJUYZzJaOMvibzjXjOXBmkBo64FktvM63izbdB7%2BfFl2kJtdCCm6tSqfgp%2FsW4Cv7Z1px0vyhGezRYzqsOvePRR6OxZ7pvskJJvWwLs5thvm9VTMo2usJr55BO8R7NHEilUHuaBAiktqWr%2FNXo7t9NLCB1YowqMGe0AY6pgHna2zWCC53xBx%2BaAAkM15F1O7UyTdMEtzVlKcOXrsA0kC1ZrWifNL8H%2Bwu00L4BaQOUe%2FP9%2F9l045r0Co9aBSmJIenLWuLTo18SJmVt9a1Yp1MqbJClwg%2Fyn0TKXa7gdX07TSESYsjKliEcIuzzcrsa8TCJs5uRBMk5vYHx0HtVN%2FJJjXUY3MbSxEIvYY%2FC3uKMaY1M66M8RFvTULnkq4P8MBh%2BfaT&X-Amz-Signature=03bb3f6c04fa368bbbfbbba1bab1ca62bca53d897c9cb9cf697f2af5c02f6e44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BGEI6VR%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T224407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJ3%2Bv7VARNSRRbymF10eIAnpd1vZrC%2FxpGEzqG7Pd4TAiAlBH38WTqXkrPiJqGxzOGfOdRISu7f9upJz6DCrYUrSiqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxwunsa%2BXnQBCCrK8KtwD3x%2FXvJKAlYkW1B3VYHUOZDe9RQNnn3bQqnPB9feiiy9VwiSPDtIDldJD2DElGRXrQ052ChAZXROqo%2FCXXt07y0lu7V8Rg%2FMLE0FQObQUVa7O0gGCfyADaDp7lgZQoJbf6uvfWnG3S58grxVUVv%2BizBkV9X7z19hboVTkEP7Xl3MP4I8EfA1h2DhMi4AKpxroyi9OjJ6H5wKz2Quw%2B1m2IpQowOddB8lvmzbltJ1%2FDWOTXPVujyDnqJ5YynMcQ%2Bv4XT7bhmiaL%2FATxuqMqB4z0zxawpwgQN6FBmavsE%2FtQeX4MAgKKmOiWPtxzY19Y%2Bn5XK1sVUXLKDDPhYw1BfYJEs0NDCx%2BOdM4XXLhzb5E%2FTKkEZEuROWws7D%2FmK1DYqtYejEZKw36xi3DLGJ24N1R0DVm5XGAlkLZSPd%2FHC2q6cLzDNTC69affmm1R%2FZFUkvfDxSd2kE45e0B%2FdpWdSf6mn5az%2FrwTD2FJUYZzJaOMvibzjXjOXBmkBo64FktvM63izbdB7%2BfFl2kJtdCCm6tSqfgp%2FsW4Cv7Z1px0vyhGezRYzqsOvePRR6OxZ7pvskJJvWwLs5thvm9VTMo2usJr55BO8R7NHEilUHuaBAiktqWr%2FNXo7t9NLCB1YowqMGe0AY6pgHna2zWCC53xBx%2BaAAkM15F1O7UyTdMEtzVlKcOXrsA0kC1ZrWifNL8H%2Bwu00L4BaQOUe%2FP9%2F9l045r0Co9aBSmJIenLWuLTo18SJmVt9a1Yp1MqbJClwg%2Fyn0TKXa7gdX07TSESYsjKliEcIuzzcrsa8TCJs5uRBMk5vYHx0HtVN%2FJJjXUY3MbSxEIvYY%2FC3uKMaY1M66M8RFvTULnkq4P8MBh%2BfaT&X-Amz-Signature=fb1bbca6a7eea0e737f158e311caee7cf132cb72bc0a94ba2902d72f420e0540&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
