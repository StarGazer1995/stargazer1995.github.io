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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQFJAVA%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T185910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICnlVuEjJ48uMVx0NmQQEBCATI%2BAdXd5l931B6zaAW2qAiEAx%2Fkra%2BzltLC9QXkDreXTvtO6sXcXS3k%2Fv0qD6EOzyGMq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDBYHBgNf2uN44lo%2FtyrcA5zPMzFi0u2p476OWkzpVjEUopPg9SyqBGSGvWouo7m%2FHfvPyGLY0PWakoDvdnvsUjwttuM3esjo2GBFrUK%2BGhDL6uWKl%2B8cYK3lNAOsCaHYf0%2BHNoiBnV8FPYumDCBmwgFGgFlYK50DVWY2yIai910dJaqD9yyJ%2BU5BzbqIk4apqexXJyUJpXeJozvEPbk%2BNaQA4axuKQercltsW%2FeLBW96ZbQiEz01fFRujFaoCBNWXl6cn0rbtX9Qgm20vdDhU%2BNrqPeWP3chP0%2FS31NNctZWb4u05LbaAL3D3BHIhzmt5VWOuZbR9Bhb4D2JAVkzkus%2Bdh0n0vcuVx%2BRJq0JacEVdDMHTSyJJhGHdRKeBxi0ccfVXMU3e7%2FwbpgfoDR1oRtD36G9r1JtAIsKW8JATA3HOf4%2FKeA91CUwXd1m%2F%2F07ZaOFzI7lv2UBByOhMx68nYu7EtZe9QvIbbDlOpLn1U9hShx79J0iCrzTD2snYYFZjuTW5UODRi9Xmg9qwP5sI6JKJhqiZffNYPI%2F%2BTT6cUQ0NCXODv9hOpHul%2BRHXSX9URNyWjFzKUv1kqGSfxnkN%2F3n3Qfputys9aTbbxG4d0un3PsB3CvuYrs8hThOg6IsnHRNAaYHNJpYuKYmMMmHzdAGOqUBp5ENl0N8R6qRA42dqY4uZaVPRwvB7%2FYyH24ydUPo05gbHa38fmlDAwvkdTblb8pH0weVKmD0bDGLjn%2FAIsBVY6KSliTUXPS4JMTsgHa5hAyWPD8hjbGVkTmtyXonShAA8ZGSu784edjk9wHtVF6INaDtXfJc6BzLb%2FXnrsVhRSGZa53suAsUgeUxKC7gDd66kueQH9nAG3j9TJCK%2BoioeDTDAnSM&X-Amz-Signature=c3ddff1ed50c4a937893a68bca8c1228e47ce18cd42b66c45f20eb0b3cf30073&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQFJAVA%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T185910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICnlVuEjJ48uMVx0NmQQEBCATI%2BAdXd5l931B6zaAW2qAiEAx%2Fkra%2BzltLC9QXkDreXTvtO6sXcXS3k%2Fv0qD6EOzyGMq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDBYHBgNf2uN44lo%2FtyrcA5zPMzFi0u2p476OWkzpVjEUopPg9SyqBGSGvWouo7m%2FHfvPyGLY0PWakoDvdnvsUjwttuM3esjo2GBFrUK%2BGhDL6uWKl%2B8cYK3lNAOsCaHYf0%2BHNoiBnV8FPYumDCBmwgFGgFlYK50DVWY2yIai910dJaqD9yyJ%2BU5BzbqIk4apqexXJyUJpXeJozvEPbk%2BNaQA4axuKQercltsW%2FeLBW96ZbQiEz01fFRujFaoCBNWXl6cn0rbtX9Qgm20vdDhU%2BNrqPeWP3chP0%2FS31NNctZWb4u05LbaAL3D3BHIhzmt5VWOuZbR9Bhb4D2JAVkzkus%2Bdh0n0vcuVx%2BRJq0JacEVdDMHTSyJJhGHdRKeBxi0ccfVXMU3e7%2FwbpgfoDR1oRtD36G9r1JtAIsKW8JATA3HOf4%2FKeA91CUwXd1m%2F%2F07ZaOFzI7lv2UBByOhMx68nYu7EtZe9QvIbbDlOpLn1U9hShx79J0iCrzTD2snYYFZjuTW5UODRi9Xmg9qwP5sI6JKJhqiZffNYPI%2F%2BTT6cUQ0NCXODv9hOpHul%2BRHXSX9URNyWjFzKUv1kqGSfxnkN%2F3n3Qfputys9aTbbxG4d0un3PsB3CvuYrs8hThOg6IsnHRNAaYHNJpYuKYmMMmHzdAGOqUBp5ENl0N8R6qRA42dqY4uZaVPRwvB7%2FYyH24ydUPo05gbHa38fmlDAwvkdTblb8pH0weVKmD0bDGLjn%2FAIsBVY6KSliTUXPS4JMTsgHa5hAyWPD8hjbGVkTmtyXonShAA8ZGSu784edjk9wHtVF6INaDtXfJc6BzLb%2FXnrsVhRSGZa53suAsUgeUxKC7gDd66kueQH9nAG3j9TJCK%2BoioeDTDAnSM&X-Amz-Signature=234d3fc587ef3c4c0b59a89dbeb1ff305ff2ac18f84df5c6a9d8d89f1854cce8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
