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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7AE24YB%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T130616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIGGoctHtYixfVVXL2Lx3Xbb9kaQYe3mIsrm7dq07rK6mAiEAn3AoScQTrj2IADjyqtdLwAJt0ewkr7KO3mhvIaGRrc0q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDJoZzYudWaNgBqf68ircAx4I58JNSaqhPKs%2B%2Fo1thQi6TvqBXOWibX6vJnizRL%2BSmJ74oUIr%2F0eOq5aU9S3LcHdB8%2FfNmdFrS9Kl3oJeWan7zt1ixRi7xe7hRlWKfnzNI7gR9ZgCEmbfd5HL4kjO421CqTqnVcWLuISmCQ2SzcqDOA9LJVXCOdNlB6FoU8ER4cRwlAO3o7MCZ8X9P8z1pvxMPor2fojjUZ4g%2FENW93r96QNlx7ZYY1gujnxdJBq1X3j9UmmNM5SFD9aReKbJOl1uShnIN8FhX2lVL8upIBeDRg%2F%2BLl7zYEuUXjs70m%2B%2F20o3yewXseb6KQQCKOTLxeSlg5F99beA0lwLIkcDgfjktWTPPv44ogm8Q9gK1RJ97vDRp9%2FG7YCfGgl0IE7hrZjQWMqF06oUyN74OwtwXb%2FaGzY%2FCEWcQFxAe9P7R8jG0FsbGxhdzkKT9H5c3ODO83iHxbVcg15VsL86s0rF0OZtKnTz%2Bg7X3LsdTcCgkKminRdxWwmX0s8uy0OzHWUCGU3dFppdXph9KkqCm%2BUOrk4rkQ1mO30iwYs5tflku0RrTKRFWuH1ZhM7FH9Gc2RuhbfFcVls3TlooLyGNefntI3mJt%2BWu%2FtoIYpR76GEX9TsgGxqNkyAvhincHIyMNLy3dIGOqUBo3z2Wu%2BTvqV7NlG61XoI8Z%2BWh6PbkGdN%2FnxPQZTGUk7snRR1K%2BmSMvYow8BA0RvAyEUi1fpvyGFEEdQS5MbRoA1%2BsO%2FplVpb7jsElMh7k25cxV5WcCHFeY0D5ffqfasHrauylfDNG2B1nZROyaOBRIQU%2Fswx2EJ5GJyt2ahhsRrz13g5T4NesHIlwFMizJe1obw6mubd8kii5z683qhK9VfJoEFe&X-Amz-Signature=fe13e300ca77392df11c40ac2e2ce097dc93e1a981f0c7755a73e40b14308672&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7AE24YB%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T130616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIGGoctHtYixfVVXL2Lx3Xbb9kaQYe3mIsrm7dq07rK6mAiEAn3AoScQTrj2IADjyqtdLwAJt0ewkr7KO3mhvIaGRrc0q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDJoZzYudWaNgBqf68ircAx4I58JNSaqhPKs%2B%2Fo1thQi6TvqBXOWibX6vJnizRL%2BSmJ74oUIr%2F0eOq5aU9S3LcHdB8%2FfNmdFrS9Kl3oJeWan7zt1ixRi7xe7hRlWKfnzNI7gR9ZgCEmbfd5HL4kjO421CqTqnVcWLuISmCQ2SzcqDOA9LJVXCOdNlB6FoU8ER4cRwlAO3o7MCZ8X9P8z1pvxMPor2fojjUZ4g%2FENW93r96QNlx7ZYY1gujnxdJBq1X3j9UmmNM5SFD9aReKbJOl1uShnIN8FhX2lVL8upIBeDRg%2F%2BLl7zYEuUXjs70m%2B%2F20o3yewXseb6KQQCKOTLxeSlg5F99beA0lwLIkcDgfjktWTPPv44ogm8Q9gK1RJ97vDRp9%2FG7YCfGgl0IE7hrZjQWMqF06oUyN74OwtwXb%2FaGzY%2FCEWcQFxAe9P7R8jG0FsbGxhdzkKT9H5c3ODO83iHxbVcg15VsL86s0rF0OZtKnTz%2Bg7X3LsdTcCgkKminRdxWwmX0s8uy0OzHWUCGU3dFppdXph9KkqCm%2BUOrk4rkQ1mO30iwYs5tflku0RrTKRFWuH1ZhM7FH9Gc2RuhbfFcVls3TlooLyGNefntI3mJt%2BWu%2FtoIYpR76GEX9TsgGxqNkyAvhincHIyMNLy3dIGOqUBo3z2Wu%2BTvqV7NlG61XoI8Z%2BWh6PbkGdN%2FnxPQZTGUk7snRR1K%2BmSMvYow8BA0RvAyEUi1fpvyGFEEdQS5MbRoA1%2BsO%2FplVpb7jsElMh7k25cxV5WcCHFeY0D5ffqfasHrauylfDNG2B1nZROyaOBRIQU%2Fswx2EJ5GJyt2ahhsRrz13g5T4NesHIlwFMizJe1obw6mubd8kii5z683qhK9VfJoEFe&X-Amz-Signature=9bd16a533762b91c74a34271bf112dab4ee7fc2c1adbe744936df0a5689c6ba4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
