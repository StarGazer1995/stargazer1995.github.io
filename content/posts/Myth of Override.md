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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7SRTBM7%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T080452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDclew7TZHkzhQYIQqdMOAX2Av9vi1bGLAzutu3siBKfAIhAOkSgJxIR6ViTkL%2B%2F9IVtR8nHBVOh2ShKsFgKF5S5RloKv8DCAEQABoMNjM3NDIzMTgzODA1IgzWRBl5EUIvCZA0QEAq3AO9aVmmDy%2BGj1ykTub0gb2c0OrLhbT4tt4sLVnU34wQOo4CjO6%2BrJZkNQH%2BnRgnw0S1GwRIUAjb5yY5Q1RY2y%2FmJZ3KVVCX2F1sH6Ae6NFdpXN2fnJsY40JMlOpuAtIffxlXo4icR6qwoDUKJw6CkayetQyBvMPTHbFTSKuCjKcfPo4kpYtLMIkgXoEPCUaPrFv7PDM6spXj5XSpLrYgvfpIZq9ftbYZtFfRuWDBAWRGFsWy0bQB27viIpuwd4194xFNsCp8amPbqGL53roZLyEWJXToOpKAw70L6AHqz74Ao0lxAN38ISflPsR4rRL3DLK7MR7xyh7z9OFO9fd2L7X2MztZ8UwnCRFvJzU%2BaDPe8vkv%2FJK9h1E7ds%2FftbEupF%2BVXUOU4sBqwWcryWsSHKiIaV50H9y5z7qCWKo%2BVlvbGPyFKE1nOPzbLDYJ4WQvTvtVmo%2FsH88lT9JmW%2FjbIgPSaZrHv7oB2ekyX76aghXLKpwvzTbWV8PFyiWb8PzFTIgza1r020O25sN5SZoYf%2BV5BQoIl6SgJB%2B3vz1%2FiEhcNYoouvTMVPuaEfMePOUjJRqyWEIXBjW5jZVMj%2F1xrjSMKPhzmMIQRj3JyyomtpL%2BQy4%2BIEpvFCWB4WOvTDTrYzTBjqkAbgzLeEIeHKtQnBPKoGmDL0PryEmJ11N%2Bi4XK9kM3ZtYgEJB13mxMaWoI1OjgVCSeRkAX7VvwCoTbTXSBzO0Hc8CTnw%2Fd11htrgeTnBGXh96TyDulPT475OJkWIKY7iCC0LVntk%2By65CRgcy26RhzBTMUpTtXRTfAc9O0L2%2BZYR1UykvHpt%2BoRTtxNd50WGTIGvh%2BGSNdQjU%2FCU%2F1bmC4k2IaktE&X-Amz-Signature=da98a784d556830f1721548300b64c51e5ce8849c2eb31a33a16488ddbd071ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7SRTBM7%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T080452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDclew7TZHkzhQYIQqdMOAX2Av9vi1bGLAzutu3siBKfAIhAOkSgJxIR6ViTkL%2B%2F9IVtR8nHBVOh2ShKsFgKF5S5RloKv8DCAEQABoMNjM3NDIzMTgzODA1IgzWRBl5EUIvCZA0QEAq3AO9aVmmDy%2BGj1ykTub0gb2c0OrLhbT4tt4sLVnU34wQOo4CjO6%2BrJZkNQH%2BnRgnw0S1GwRIUAjb5yY5Q1RY2y%2FmJZ3KVVCX2F1sH6Ae6NFdpXN2fnJsY40JMlOpuAtIffxlXo4icR6qwoDUKJw6CkayetQyBvMPTHbFTSKuCjKcfPo4kpYtLMIkgXoEPCUaPrFv7PDM6spXj5XSpLrYgvfpIZq9ftbYZtFfRuWDBAWRGFsWy0bQB27viIpuwd4194xFNsCp8amPbqGL53roZLyEWJXToOpKAw70L6AHqz74Ao0lxAN38ISflPsR4rRL3DLK7MR7xyh7z9OFO9fd2L7X2MztZ8UwnCRFvJzU%2BaDPe8vkv%2FJK9h1E7ds%2FftbEupF%2BVXUOU4sBqwWcryWsSHKiIaV50H9y5z7qCWKo%2BVlvbGPyFKE1nOPzbLDYJ4WQvTvtVmo%2FsH88lT9JmW%2FjbIgPSaZrHv7oB2ekyX76aghXLKpwvzTbWV8PFyiWb8PzFTIgza1r020O25sN5SZoYf%2BV5BQoIl6SgJB%2B3vz1%2FiEhcNYoouvTMVPuaEfMePOUjJRqyWEIXBjW5jZVMj%2F1xrjSMKPhzmMIQRj3JyyomtpL%2BQy4%2BIEpvFCWB4WOvTDTrYzTBjqkAbgzLeEIeHKtQnBPKoGmDL0PryEmJ11N%2Bi4XK9kM3ZtYgEJB13mxMaWoI1OjgVCSeRkAX7VvwCoTbTXSBzO0Hc8CTnw%2Fd11htrgeTnBGXh96TyDulPT475OJkWIKY7iCC0LVntk%2By65CRgcy26RhzBTMUpTtXRTfAc9O0L2%2BZYR1UykvHpt%2BoRTtxNd50WGTIGvh%2BGSNdQjU%2FCU%2F1bmC4k2IaktE&X-Amz-Signature=2376999c4c53eb768b069bd381cbe866b53036a87fa5195cb1ae750a0b26635e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
