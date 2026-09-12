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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEYO7ZV5%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T063843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDe4kq9A8PAfSF%2F1Efj6llTDx8TLY7B3YC6pn80lwNelgIhAIhi35uHNHhAOQoT0hSxuT9hQOav0pBq13aK4%2FleJyXDKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyJpz8%2B0wMnvV77Gsq3AP6nk7S7zgahsDSwwalvCi2w%2FwlslGNsZIr9Q6X%2Bp4dUbnG3ijqjiqpjKW8%2BsRyaTgdhsPFrWLllyB4yXeGa7ZN74oF84%2FsQ7z0MDrPdJUJoeokAvcAjbALm0JaCDpRXbIaLw5IYNYyhVg5moLHo1%2FCL3zJl8qpBfkKI5hGK5xfsXPn4mIIZIA7oV6pm9TlXMfp7Z5hgUfzpYIeJJ6nR0hV93gWxk5ftUQUYbT6PgyoCLhe%2BbjV2VgS53PP%2BgEZPqXQ9elB8bbRnVVT7aXlvDr3G1swpIVxuYmS%2B6%2BHYwM%2FXGHe8t6hGCYC27wnti3Q9gFojU8tM7muBvDhlSEBsiU6G%2BbFxSexcx%2BajuMChVN3qBsg0KM7YJJdfcWZzhGtxXcy20vVYbP1Q2TtgCM3Z0SgIzqg4iotR9th8olcxWKVg1grmj6wxrQo00Pe66Vulp3SsbjAL%2BEmkr66nkvO1upSjRRWLVTyzxxhpAEMy75wOrgaM7%2Be4CHD5EpyDt2cP%2FWwxiqcauQCwHu17zQ21j9BGXJvHJyxz%2BCzrKqQjt32%2FUYkw%2Br%2BVSic7DTFtfOWABm7hiRDuQEd1gbXFcIlFoi6N%2BHlRnli2mL5PrIsi1hul4hGpYC0tZ1l3DLQojCjtJPVBjqkAVkECCE0LAnD8qKMB4EtUzfW7l3m6j6OMgVp3%2BiQME27U1GzocA3r3YTay0XteXtwzauOJl3ndR0zEDsZUeRQc91a3n210Jsl0z8GMDq6JHE%2BcqFy3RRvd2CGP901lvt63AqZMyTrAP9KAmpw3sNCm%2FWsVC64CB4gSJ0LGrtnMsYmVgSQglAcOutRsvfzIBMmnKeKsxKJ25IKIUrrkkf8O13wMwr&X-Amz-Signature=8788c634b4e342bb0881ac4d899e114afe4eed4025037af91aa8f18c57b23324&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEYO7ZV5%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T063843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDe4kq9A8PAfSF%2F1Efj6llTDx8TLY7B3YC6pn80lwNelgIhAIhi35uHNHhAOQoT0hSxuT9hQOav0pBq13aK4%2FleJyXDKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyJpz8%2B0wMnvV77Gsq3AP6nk7S7zgahsDSwwalvCi2w%2FwlslGNsZIr9Q6X%2Bp4dUbnG3ijqjiqpjKW8%2BsRyaTgdhsPFrWLllyB4yXeGa7ZN74oF84%2FsQ7z0MDrPdJUJoeokAvcAjbALm0JaCDpRXbIaLw5IYNYyhVg5moLHo1%2FCL3zJl8qpBfkKI5hGK5xfsXPn4mIIZIA7oV6pm9TlXMfp7Z5hgUfzpYIeJJ6nR0hV93gWxk5ftUQUYbT6PgyoCLhe%2BbjV2VgS53PP%2BgEZPqXQ9elB8bbRnVVT7aXlvDr3G1swpIVxuYmS%2B6%2BHYwM%2FXGHe8t6hGCYC27wnti3Q9gFojU8tM7muBvDhlSEBsiU6G%2BbFxSexcx%2BajuMChVN3qBsg0KM7YJJdfcWZzhGtxXcy20vVYbP1Q2TtgCM3Z0SgIzqg4iotR9th8olcxWKVg1grmj6wxrQo00Pe66Vulp3SsbjAL%2BEmkr66nkvO1upSjRRWLVTyzxxhpAEMy75wOrgaM7%2Be4CHD5EpyDt2cP%2FWwxiqcauQCwHu17zQ21j9BGXJvHJyxz%2BCzrKqQjt32%2FUYkw%2Br%2BVSic7DTFtfOWABm7hiRDuQEd1gbXFcIlFoi6N%2BHlRnli2mL5PrIsi1hul4hGpYC0tZ1l3DLQojCjtJPVBjqkAVkECCE0LAnD8qKMB4EtUzfW7l3m6j6OMgVp3%2BiQME27U1GzocA3r3YTay0XteXtwzauOJl3ndR0zEDsZUeRQc91a3n210Jsl0z8GMDq6JHE%2BcqFy3RRvd2CGP901lvt63AqZMyTrAP9KAmpw3sNCm%2FWsVC64CB4gSJ0LGrtnMsYmVgSQglAcOutRsvfzIBMmnKeKsxKJ25IKIUrrkkf8O13wMwr&X-Amz-Signature=790dd4453eef2e1b38e2395a9669916901fa795aeade553b58171eb829e25523&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
