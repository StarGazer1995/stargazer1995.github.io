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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSM2NFSD%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T102732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIHSV3QoiDYBrALtXxH8KpLYved3LmDTWV2RTRQKFyIuyAiB68nUFVtX7sFPqkp0wQN3Ef%2Bw0u1%2BSRW%2B6VsbovInaeyqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjagPR4PC3Y2PVZ8lKtwDeiuplVrA3dnsqdcT%2FReCOZZi%2B8BqDB0AcUq%2FrzTTll2aA%2BlsMDmDqZCbhViW1nStror7dImvdu%2FZQpwpYTxtf%2FJbIA1DPs6p6L8IWWlKANG%2FBQbmrr7rR789%2BTqy5TYLp3Ry1b%2FcGYuir955stp92qTygxLe%2Ftgn6mcKbfQgVrJTQFMd1JMXJmNJqo%2FjVdlZoX3uBmr6pytMoA1ETws65k4%2FjfjAwWbNw7sptSyTuQLOU8K%2Fdw0daUSZVnRbN%2B4pxee1VtpprtjDtRRTyF69dhqh0sYjgMn3kD9yKwg0h52U%2FEDZIV7Jkaypuo7oZCqZryENveIVrpGWEk4A7lbpHG5wZzfyJ%2FAYfP0NStIvHqaKAYeOHHU6cI9S3QCblx7089rfs25DfnxTnYOXnxoCV9Bhd6GHdkVtJfewIT56N6j7DHN%2B9yr37cfbBvvjx4M9dPIBCzg0M1lQ%2B9kbq07eNqloLVym3o6OIT7g5VaJERy7DHKx7YilZ3fOk44KsQ2YcjXs2djJlJxpEtr16NdyH0rZItIhd%2Bgme0VY8lv7%2BmAkKnuKwW8P2EOSgjDPS54fNgJW%2Bd6XF5BfeBG%2BH6k09nHVE2u6l488VHMeHYAtt6VmLXHhNI%2BeQ6ntlOQw%2F9WY0gY6pgFQ5azC92Q2fQ9Yo8m6Di7WO4QibQ2ZECdZTPth354NU8LsWwOWvIQ7RQ7SbBMnWjL1%2BQdkvPEFArJMd1krMqydyJVgHwXqP7gs%2BXC3BftP13eQcPztefo6PikdeY34lgHZ7iNzhveEag9vUMsNHnIdN3N%2BjgTPc3Q3gF13VR4PwfpLELeWLQJ7iwfH31YAB7P9L2Kxp0Q09F9KcF6LEX%2FpvdmbSfX%2F&X-Amz-Signature=f51814b634088a89cbd2540866dc92265ec76d47b38479758087138b5727f407&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSM2NFSD%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T102732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIHSV3QoiDYBrALtXxH8KpLYved3LmDTWV2RTRQKFyIuyAiB68nUFVtX7sFPqkp0wQN3Ef%2Bw0u1%2BSRW%2B6VsbovInaeyqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjagPR4PC3Y2PVZ8lKtwDeiuplVrA3dnsqdcT%2FReCOZZi%2B8BqDB0AcUq%2FrzTTll2aA%2BlsMDmDqZCbhViW1nStror7dImvdu%2FZQpwpYTxtf%2FJbIA1DPs6p6L8IWWlKANG%2FBQbmrr7rR789%2BTqy5TYLp3Ry1b%2FcGYuir955stp92qTygxLe%2Ftgn6mcKbfQgVrJTQFMd1JMXJmNJqo%2FjVdlZoX3uBmr6pytMoA1ETws65k4%2FjfjAwWbNw7sptSyTuQLOU8K%2Fdw0daUSZVnRbN%2B4pxee1VtpprtjDtRRTyF69dhqh0sYjgMn3kD9yKwg0h52U%2FEDZIV7Jkaypuo7oZCqZryENveIVrpGWEk4A7lbpHG5wZzfyJ%2FAYfP0NStIvHqaKAYeOHHU6cI9S3QCblx7089rfs25DfnxTnYOXnxoCV9Bhd6GHdkVtJfewIT56N6j7DHN%2B9yr37cfbBvvjx4M9dPIBCzg0M1lQ%2B9kbq07eNqloLVym3o6OIT7g5VaJERy7DHKx7YilZ3fOk44KsQ2YcjXs2djJlJxpEtr16NdyH0rZItIhd%2Bgme0VY8lv7%2BmAkKnuKwW8P2EOSgjDPS54fNgJW%2Bd6XF5BfeBG%2BH6k09nHVE2u6l488VHMeHYAtt6VmLXHhNI%2BeQ6ntlOQw%2F9WY0gY6pgFQ5azC92Q2fQ9Yo8m6Di7WO4QibQ2ZECdZTPth354NU8LsWwOWvIQ7RQ7SbBMnWjL1%2BQdkvPEFArJMd1krMqydyJVgHwXqP7gs%2BXC3BftP13eQcPztefo6PikdeY34lgHZ7iNzhveEag9vUMsNHnIdN3N%2BjgTPc3Q3gF13VR4PwfpLELeWLQJ7iwfH31YAB7P9L2Kxp0Q09F9KcF6LEX%2FpvdmbSfX%2F&X-Amz-Signature=e98e4c11682212d14cba638c33001478e04827551586fc2f88d997a5ae0a1b8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
