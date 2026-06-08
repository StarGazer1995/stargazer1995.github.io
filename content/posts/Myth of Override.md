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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VO4VAD64%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T135845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH1jADsWFj23SkYMivH9QGkHqxRY%2BECwPVdWkI4zNCRmAiAgmkg6JV4BMSoJogA62KXLifCsSwVa105lcAa1%2BshI7yqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhunxYl4i%2FHWECDxHKtwD%2F9qpAyOagvuccDRlKRnEZreRikxGWPVHZT%2BEEmu6J3a84bVpq6Mlt2izLUZpZfmflPA3UrOt4VT1BxpiUA0wQpucNa98%2B9%2BwgE1rtlpwgYeQKgW2sshylT90sqTMaCMhJEAR2OHOrAlYIBWA9XgelBwAzgcv%2FmNLhShIP%2FksR2Hxo09t48Uux5Z2%2BZdEQAX%2BXVleB97nZuYVk5br8PmXUmjgmHQM29sUHfgVJ3Ol9rU%2BWG0Ye1jMP6CHuDqsalSrsq338%2BG0JF08zpJJxo6%2Fqc7McJVwjOJ%2BY71IxQmHXIXdRRHFhN4S3laIp%2BePAVaTjF3%2BsTq4v5jCJDwc2iBl9BhgHn6FC5Fy9VJuZQvC7bcPOrvZvOL4QrAxF5Wpb1A2lM3Je1g%2BOgyfhNeCszn6DcwtI7CvMgDrVUl3C5nWZ6P507EOGc6kjubfiHhB7pcDzxoxAmy8Jm25O46xYv%2FikmKjg79SvSVOIpeWp9QAPb5Oz0KebNm8G%2FZmURoZaEE1R%2FlPiq038St7mhR5fJxgHYtNwr6QG61lbjtGp3xNqrNhjyFOPVmme3jkHwUIDsGe2RKfZO4IKk3YL0N9KjiOXbRknbHkUlRua2onQ9sFEeQACYnPGib7JcVW4gUwkdea0QY6pgHaGJoenvZhQCRgZG6FPM%2F8dFj5rVNWNWS6ZfH9JZ4Va0rmj%2B1J02bS7vywtDQ8A46mGN0hQJbEs%2F8f22BZhabOCaLN0yiIJIwlqJOJM3dovOe4d6WUMWCThKerPnAor1rC9vN7jWyAe1RL4%2FzzkX7xxlXX0IlXAFiZF4oZ17M88Aq5HuVY9%2F5T220b%2Fz1eA%2FnheRmq7SKJuMMHZAvfmGiWGGn1tTuu&X-Amz-Signature=de46fee38f33d849959c7ea6ac7b17bf7458e44d8d3f5f5ffec59bab4cca14eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VO4VAD64%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T135845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH1jADsWFj23SkYMivH9QGkHqxRY%2BECwPVdWkI4zNCRmAiAgmkg6JV4BMSoJogA62KXLifCsSwVa105lcAa1%2BshI7yqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhunxYl4i%2FHWECDxHKtwD%2F9qpAyOagvuccDRlKRnEZreRikxGWPVHZT%2BEEmu6J3a84bVpq6Mlt2izLUZpZfmflPA3UrOt4VT1BxpiUA0wQpucNa98%2B9%2BwgE1rtlpwgYeQKgW2sshylT90sqTMaCMhJEAR2OHOrAlYIBWA9XgelBwAzgcv%2FmNLhShIP%2FksR2Hxo09t48Uux5Z2%2BZdEQAX%2BXVleB97nZuYVk5br8PmXUmjgmHQM29sUHfgVJ3Ol9rU%2BWG0Ye1jMP6CHuDqsalSrsq338%2BG0JF08zpJJxo6%2Fqc7McJVwjOJ%2BY71IxQmHXIXdRRHFhN4S3laIp%2BePAVaTjF3%2BsTq4v5jCJDwc2iBl9BhgHn6FC5Fy9VJuZQvC7bcPOrvZvOL4QrAxF5Wpb1A2lM3Je1g%2BOgyfhNeCszn6DcwtI7CvMgDrVUl3C5nWZ6P507EOGc6kjubfiHhB7pcDzxoxAmy8Jm25O46xYv%2FikmKjg79SvSVOIpeWp9QAPb5Oz0KebNm8G%2FZmURoZaEE1R%2FlPiq038St7mhR5fJxgHYtNwr6QG61lbjtGp3xNqrNhjyFOPVmme3jkHwUIDsGe2RKfZO4IKk3YL0N9KjiOXbRknbHkUlRua2onQ9sFEeQACYnPGib7JcVW4gUwkdea0QY6pgHaGJoenvZhQCRgZG6FPM%2F8dFj5rVNWNWS6ZfH9JZ4Va0rmj%2B1J02bS7vywtDQ8A46mGN0hQJbEs%2F8f22BZhabOCaLN0yiIJIwlqJOJM3dovOe4d6WUMWCThKerPnAor1rC9vN7jWyAe1RL4%2FzzkX7xxlXX0IlXAFiZF4oZ17M88Aq5HuVY9%2F5T220b%2Fz1eA%2FnheRmq7SKJuMMHZAvfmGiWGGn1tTuu&X-Amz-Signature=5567bc955c07b399d248112823a971c3649aa3911f15f53fd5cc0f6efbd197fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
