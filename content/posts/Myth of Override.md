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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXW7TFES%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T075449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1qiXlfN4wlxwgIetLNsUcHSR71rKw%2FDVYbsCic6sw5AiEA9qjidA8TpbYZgGXWHpT1YLOkkZ%2FWrR8Twp8c4e0xaxYqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBxtEK0QN%2FNDLdcGSrcA1pGPXho18MphIQQTeNsvKf2LDSAVoYU94xLL16MF6fwFqGH%2FyC0j6lZg%2B%2Ffr%2FSKIA2K0TpAoqvK8usVM41z3gS6nyNFgR7RwbstoLdkIAgxpoyVwvuaElgoMZ4OUAlyVvBN57v2%2BefoxxPouBIYij%2BcuDq15AcabYVsBF9O4o9fB9gwhDK7G0ZoUjGlYVzg9l2ICzpeRXJd6LJ7zYSQUrZVwxMCHrHDKPlNsUkAa3M2WO0tV2kM4WLRYLH4njzVLm4YVRqbCflaRkCAaeeaPYPiEjPDJkwHw6LMzDFfsbLknDMhme7GDXqI9%2FRLzYfzHlCMloF4EjVRJ9uXhLRcvlPuWCoXRlG96ec7DXvsTElh98%2B57Sm3HVBAKZiBBqGqazKV6hQyp22I34%2FX3RnBEeQf6Et84%2Fee81dgOUC4Ys65Oxlro8meb97Tq1sjkkZnKabSUfRJur%2BV3lxqhoseS8i%2FsClxWwHsXllBwb8kC86gzpunCJkAWT%2FtDAN92M7weipXApgy%2Fkbl5rGDF5ebH8L9y6gjVNARkRTuiow5S5LDBBDAE%2BW6h7hcnkONqIEqj%2B0M8kLyZumyOibMG5fWOtOq%2F6R09MiIwxFGeAyjbkpwiAfd8xNccJD3riELMKj5qtAGOqUB%2FCrcK4ldUE7wzpI%2FKuLPyYwgMA7CPrnTYtftpZDgaox2di%2BzDyaW5Pl1sIojrCYNfEtxx7Eokknae8fbbPHXKu3CLsqhAZrXvcuzdTBsD7JZ7%2FAOp%2BhluaHdZR70W3KulK7uFVyzyrSOgQJ83P59e3ybpAkFFfZ2r3zzA%2FBH0%2BNeznpFWHumUrVEGgatLs3%2FcIsqvdtfYjOBpqS%2B05Ris8UNv094&X-Amz-Signature=0ae954fc9bc36e8d0b8121183afd7ffe7d4abe0f7854231786321fbf92afbb20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXW7TFES%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T075448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1qiXlfN4wlxwgIetLNsUcHSR71rKw%2FDVYbsCic6sw5AiEA9qjidA8TpbYZgGXWHpT1YLOkkZ%2FWrR8Twp8c4e0xaxYqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBxtEK0QN%2FNDLdcGSrcA1pGPXho18MphIQQTeNsvKf2LDSAVoYU94xLL16MF6fwFqGH%2FyC0j6lZg%2B%2Ffr%2FSKIA2K0TpAoqvK8usVM41z3gS6nyNFgR7RwbstoLdkIAgxpoyVwvuaElgoMZ4OUAlyVvBN57v2%2BefoxxPouBIYij%2BcuDq15AcabYVsBF9O4o9fB9gwhDK7G0ZoUjGlYVzg9l2ICzpeRXJd6LJ7zYSQUrZVwxMCHrHDKPlNsUkAa3M2WO0tV2kM4WLRYLH4njzVLm4YVRqbCflaRkCAaeeaPYPiEjPDJkwHw6LMzDFfsbLknDMhme7GDXqI9%2FRLzYfzHlCMloF4EjVRJ9uXhLRcvlPuWCoXRlG96ec7DXvsTElh98%2B57Sm3HVBAKZiBBqGqazKV6hQyp22I34%2FX3RnBEeQf6Et84%2Fee81dgOUC4Ys65Oxlro8meb97Tq1sjkkZnKabSUfRJur%2BV3lxqhoseS8i%2FsClxWwHsXllBwb8kC86gzpunCJkAWT%2FtDAN92M7weipXApgy%2Fkbl5rGDF5ebH8L9y6gjVNARkRTuiow5S5LDBBDAE%2BW6h7hcnkONqIEqj%2B0M8kLyZumyOibMG5fWOtOq%2F6R09MiIwxFGeAyjbkpwiAfd8xNccJD3riELMKj5qtAGOqUB%2FCrcK4ldUE7wzpI%2FKuLPyYwgMA7CPrnTYtftpZDgaox2di%2BzDyaW5Pl1sIojrCYNfEtxx7Eokknae8fbbPHXKu3CLsqhAZrXvcuzdTBsD7JZ7%2FAOp%2BhluaHdZR70W3KulK7uFVyzyrSOgQJ83P59e3ybpAkFFfZ2r3zzA%2FBH0%2BNeznpFWHumUrVEGgatLs3%2FcIsqvdtfYjOBpqS%2B05Ris8UNv094&X-Amz-Signature=057de4ec4e1c05353c4ad0a59f975d8e4a066425a3ce7c15392ba8c509ab8050&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
