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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUG5AGPC%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T092940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICNd7ByAXmFDZQNmMSwQ2FpvfeIL8fx87e%2BAGYkC048AAiEAzFeON1KWEJVF%2Fs5p6ezUTPZyz61toQQJYIprHO%2BR7vAq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDCg7MChTnjvaq4lr%2FSrcA66%2BQWHOd9UH1FexV02zreOJh%2BoVnsBEvZtUR5bFaDwwnEXPjRg%2BorVPxo42kG6u65rntAJIAGlYmyqNIqhZLUsvgraki5PmNuDfdKD7UsVs8KrYHy9b7AJec%2Buim0Rn4Vz5i42Dewg7kaAOJprItULN1rSFRULInVDkPTS2MBbv8O4%2B2HG6Rjsyhggc0b0iJ6l%2BsF73KtUm2G2nwdj9DPa%2B5B5RlXmw0yg%2FNHqzGbVllZjN6WC%2B8%2FPyuuBdTw7jf3s1jQWzuCH3TOBVaot2Xlfo1Drf8J53SiZhnLTWLAj9xJ5EdDNO6bJLopc2KYICa%2BjzKE7RrRXfYQIDQeJVXXS%2B2nIyhTHwgbY8KRT8omPWCoQhwAVtGLYpUjD%2FUrzv1rstgVIxQhjUSwt2j%2BnOhsa4G0%2BHRwUBLu7SOUqVYym91UP%2BCsmZyaan6tzJC%2FHwomWxE%2BZ9TZ%2BedZBnTKkETrX8s1%2BGhByvVHkC44D%2F%2Fd0n3gkJZ%2BD22KDm8KzdaXiB%2FfZ%2FvCEjBTBuUKCEENndfR0xz4S9O7roDB6of1C%2FLWB1BqWwFyWhG3RxEB6lhF3a8HxXY5T4dGT4c4JaSD%2FB3LEWO3OsRC9dgNjbqezvu6cOSA6oZWFbSdg%2B2xk8MMmIs9IGOqUBledaXT3Er0KFMhF177yePkAlJGANMQr7h3LqICtQE67c4eKYARyO7%2BRN%2BbNm9FSTTGTT%2BzGDNxJFO7JmDMvyMugxBvjhpczvSQ439B774chqsaXY3kqBcJpBzoKq2N89GO%2Bwv%2BfczX6Tuksd4XVuPGSqwOZDDe4trmuVjyUiqUjg%2FP43klvGAxZ5Ck9uj6bSiiYp0%2FtMm9wLFTbFlMHlYQCdu9u3&X-Amz-Signature=d2d56909b7a9dac38698ca71f3c3eba6d3fca4a1ef18eabd39fadc6ccb47c936&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUG5AGPC%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T092940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICNd7ByAXmFDZQNmMSwQ2FpvfeIL8fx87e%2BAGYkC048AAiEAzFeON1KWEJVF%2Fs5p6ezUTPZyz61toQQJYIprHO%2BR7vAq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDCg7MChTnjvaq4lr%2FSrcA66%2BQWHOd9UH1FexV02zreOJh%2BoVnsBEvZtUR5bFaDwwnEXPjRg%2BorVPxo42kG6u65rntAJIAGlYmyqNIqhZLUsvgraki5PmNuDfdKD7UsVs8KrYHy9b7AJec%2Buim0Rn4Vz5i42Dewg7kaAOJprItULN1rSFRULInVDkPTS2MBbv8O4%2B2HG6Rjsyhggc0b0iJ6l%2BsF73KtUm2G2nwdj9DPa%2B5B5RlXmw0yg%2FNHqzGbVllZjN6WC%2B8%2FPyuuBdTw7jf3s1jQWzuCH3TOBVaot2Xlfo1Drf8J53SiZhnLTWLAj9xJ5EdDNO6bJLopc2KYICa%2BjzKE7RrRXfYQIDQeJVXXS%2B2nIyhTHwgbY8KRT8omPWCoQhwAVtGLYpUjD%2FUrzv1rstgVIxQhjUSwt2j%2BnOhsa4G0%2BHRwUBLu7SOUqVYym91UP%2BCsmZyaan6tzJC%2FHwomWxE%2BZ9TZ%2BedZBnTKkETrX8s1%2BGhByvVHkC44D%2F%2Fd0n3gkJZ%2BD22KDm8KzdaXiB%2FfZ%2FvCEjBTBuUKCEENndfR0xz4S9O7roDB6of1C%2FLWB1BqWwFyWhG3RxEB6lhF3a8HxXY5T4dGT4c4JaSD%2FB3LEWO3OsRC9dgNjbqezvu6cOSA6oZWFbSdg%2B2xk8MMmIs9IGOqUBledaXT3Er0KFMhF177yePkAlJGANMQr7h3LqICtQE67c4eKYARyO7%2BRN%2BbNm9FSTTGTT%2BzGDNxJFO7JmDMvyMugxBvjhpczvSQ439B774chqsaXY3kqBcJpBzoKq2N89GO%2Bwv%2BfczX6Tuksd4XVuPGSqwOZDDe4trmuVjyUiqUjg%2FP43klvGAxZ5Ck9uj6bSiiYp0%2FtMm9wLFTbFlMHlYQCdu9u3&X-Amz-Signature=163c9d4fbf888aecf738106216ae68dd8f6fe641f7847feb6f6e4b8e41bd3110&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
