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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AZW43EY%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T111854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4dmFecCc%2Br9uMZPEyFwGgayjjzldgWw9%2F25nkDwZ2VgIgSh2RGNXMA7ML7H9Z0q7MOZT6IRP17M3eXEt1kmyWxo4qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLnAiL%2FAvQyFMEU8cCrcAyHXBbi3%2F8wo2zXvaQsSoNabzN%2FYM2Y%2FDU9h8w5Rx1ShX3QQNEZ5J4L59C81Dr5QhL0NU5yc%2Fd3MsMT%2FoxLDSyT%2FaRYHQaWhq6VOxzX%2B4S3h4SvzMFFp1QMm93%2BPQqkg0i8K5QJ43y4SmjZlEbMozLUZePX48Dt1CXTNA13y%2BguAuLoVutXXYuVFgQ55kgOIuQrXSVsTPRpW%2F3R%2FROQdolYNzfp9cJ%2FxVFKhUmEfhTQeo5T%2Fy288HK3im2XG8779uZu2rWgBL4uMEJdJz7DBzxwY0LsRTZdnDYl2Lyc95SXFOTy8YXZK2LKmv7UvSzWeJY5YvVkpUui192anzuBLU6thFQBIK7vV26hLxPz94KXzWkjScl715yi30%2FQM%2BUmi2kbcDW3q6Rwt59qxg%2BjOFhuwHhn6hxFKy2AtXjLEH8Bh7M%2Bv7kMe1rAFpCfC2nd2CFZVKxobW%2FuZejrbqLU9wLVgAwQxRxSLGjg%2FqCiM0%2FqQsl2abDuMT0c6YhNigjPsjbRG7LKVnDPEC4sWNYWmFOcOEF7vjtQcYtpqn0UxAqNL0DmDgjKZPVrdQjWMG1DxkETLz0R%2BUMBWFIE0kEE8Tk3sL7FLFCkbrALSlOrU2y35KNfjagCt9Cl%2FR8IyMLXf5dAGOqUBVa0h%2FLSfzmhC4D6ZcMs%2FMoCaZpgImB7ISXKsebDNF3%2FSHJPQz%2B6U%2F9ckNDLgMgx0fHxkkDbDdj2MQFDS24vh6du7ev039a0KBk09jCZubHA7sxVyA83Dr6u%2BZxEQhlxpkbCpNS3iL0Xe6qP4DSi70VtDBMmlc5YITYvnqUy%2FzY6dIyEJ0d3Ka4jyPDEfMnQMZBFlXzzPLDaqZhCPSzXBYEl27Tgh&X-Amz-Signature=92f254f1fa5f6c79b73107f02f2c3adc593234e0f63e664e6017a5987e7c6bf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AZW43EY%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T111854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4dmFecCc%2Br9uMZPEyFwGgayjjzldgWw9%2F25nkDwZ2VgIgSh2RGNXMA7ML7H9Z0q7MOZT6IRP17M3eXEt1kmyWxo4qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLnAiL%2FAvQyFMEU8cCrcAyHXBbi3%2F8wo2zXvaQsSoNabzN%2FYM2Y%2FDU9h8w5Rx1ShX3QQNEZ5J4L59C81Dr5QhL0NU5yc%2Fd3MsMT%2FoxLDSyT%2FaRYHQaWhq6VOxzX%2B4S3h4SvzMFFp1QMm93%2BPQqkg0i8K5QJ43y4SmjZlEbMozLUZePX48Dt1CXTNA13y%2BguAuLoVutXXYuVFgQ55kgOIuQrXSVsTPRpW%2F3R%2FROQdolYNzfp9cJ%2FxVFKhUmEfhTQeo5T%2Fy288HK3im2XG8779uZu2rWgBL4uMEJdJz7DBzxwY0LsRTZdnDYl2Lyc95SXFOTy8YXZK2LKmv7UvSzWeJY5YvVkpUui192anzuBLU6thFQBIK7vV26hLxPz94KXzWkjScl715yi30%2FQM%2BUmi2kbcDW3q6Rwt59qxg%2BjOFhuwHhn6hxFKy2AtXjLEH8Bh7M%2Bv7kMe1rAFpCfC2nd2CFZVKxobW%2FuZejrbqLU9wLVgAwQxRxSLGjg%2FqCiM0%2FqQsl2abDuMT0c6YhNigjPsjbRG7LKVnDPEC4sWNYWmFOcOEF7vjtQcYtpqn0UxAqNL0DmDgjKZPVrdQjWMG1DxkETLz0R%2BUMBWFIE0kEE8Tk3sL7FLFCkbrALSlOrU2y35KNfjagCt9Cl%2FR8IyMLXf5dAGOqUBVa0h%2FLSfzmhC4D6ZcMs%2FMoCaZpgImB7ISXKsebDNF3%2FSHJPQz%2B6U%2F9ckNDLgMgx0fHxkkDbDdj2MQFDS24vh6du7ev039a0KBk09jCZubHA7sxVyA83Dr6u%2BZxEQhlxpkbCpNS3iL0Xe6qP4DSi70VtDBMmlc5YITYvnqUy%2FzY6dIyEJ0d3Ka4jyPDEfMnQMZBFlXzzPLDaqZhCPSzXBYEl27Tgh&X-Amz-Signature=13ec96aee3c0ca9499b1b059492c0f6f07b3614fb5bf139db6422e1eecb1b4d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
