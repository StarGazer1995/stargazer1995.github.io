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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGJX3KD4%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T050029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIHwx5xrW7xCOfsCwXMwgUrTd28%2FYJ2Wc0l2EG2qhTXlGAiBE1BgWjUcyXr0f0WPsg58ArQCt3N9GvX2jXeoEAFN1iyqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI4oXRH7G%2Fys1SpjSKtwDQMzDDFO%2B8DLWkvQcgcPCcB1PDoBx2fxGV2TjFKH2Dd2Ay3SaCfoNqNZ5Ba9NSBUuHx%2F%2FNtf5Gf%2BVQ2xxtUcxBYyn9V9yKz9xYMudyGUa5oIdsdelxjLFU4goQIW%2FbiuJeBqXII3f%2B%2B6JoYs%2BPR%2F7JyTuiAaYFAPSIgFcHkM4sptjuOLiTPRi8I3q%2BE26xiP1lNZ4FfJ12%2BJbee8odzc0TiAqheBiWlQcIAEMIEt4FrpmB%2BkF6NWnlPa02lltmhF4sBrF%2FM9YT567bG8%2BRqenby80igtkUkQk7vHpkGSs5siq%2BnejxmAX1BpAFfzOhHcIzAP2xWYmNp6BHjP36Zg3j98%2FZe5Qtd840SMc74N8%2B4GJT2yfYK6lelxF4WwzxCrUWJWLy17z0IkctZxrzoRGCqHXe0EBnX7QH%2FRfm%2FifsVZfVYrNFwVJC9cyZMmc3u3X93%2Bp6wIKF8ArtiPOKOBwKn2UwxfjbF0jL4SshnhM9kFo5Vd5wLvPoEA7zeiJAwxUZhYqcTJ%2B9XWtnFCuYOHqE2eQsLY%2FdBEMqmxloNjHM5JrWbW5BYDfJ2D2Qlu36JC%2B%2BdlS4xQ0vgpCUPBtaRkO8XUpl2g15V4Io5sWVqg4WGnVI1k9QAxs8SA5Q8MwsPT6zwY6pgHdFmKk2xD%2FcTddfSjhxTb19t3TwsSn%2BaoZXkMPWFX6eCZMvIb%2FDbFqjtUIDFuFtkdPbT9Cea3cKKLtJb7maIYeki8AGEznlI57vwqS5nRKzwi0sm%2Fj7zI8SttfKL7dViMcDYknjsL22I8CLYHGfrNpUqF9t25EaPceUWBwFg326IYT3rRYOSqAMNGAfpsd9rixwCjdt31TVoI%2BB4ajwlPa6Pr9QuAL&X-Amz-Signature=1f90b475d8f4bd4c883a68808614c5d2ad742b1bcc8b905bd1859ee72493fe6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGJX3KD4%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T050029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIHwx5xrW7xCOfsCwXMwgUrTd28%2FYJ2Wc0l2EG2qhTXlGAiBE1BgWjUcyXr0f0WPsg58ArQCt3N9GvX2jXeoEAFN1iyqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI4oXRH7G%2Fys1SpjSKtwDQMzDDFO%2B8DLWkvQcgcPCcB1PDoBx2fxGV2TjFKH2Dd2Ay3SaCfoNqNZ5Ba9NSBUuHx%2F%2FNtf5Gf%2BVQ2xxtUcxBYyn9V9yKz9xYMudyGUa5oIdsdelxjLFU4goQIW%2FbiuJeBqXII3f%2B%2B6JoYs%2BPR%2F7JyTuiAaYFAPSIgFcHkM4sptjuOLiTPRi8I3q%2BE26xiP1lNZ4FfJ12%2BJbee8odzc0TiAqheBiWlQcIAEMIEt4FrpmB%2BkF6NWnlPa02lltmhF4sBrF%2FM9YT567bG8%2BRqenby80igtkUkQk7vHpkGSs5siq%2BnejxmAX1BpAFfzOhHcIzAP2xWYmNp6BHjP36Zg3j98%2FZe5Qtd840SMc74N8%2B4GJT2yfYK6lelxF4WwzxCrUWJWLy17z0IkctZxrzoRGCqHXe0EBnX7QH%2FRfm%2FifsVZfVYrNFwVJC9cyZMmc3u3X93%2Bp6wIKF8ArtiPOKOBwKn2UwxfjbF0jL4SshnhM9kFo5Vd5wLvPoEA7zeiJAwxUZhYqcTJ%2B9XWtnFCuYOHqE2eQsLY%2FdBEMqmxloNjHM5JrWbW5BYDfJ2D2Qlu36JC%2B%2BdlS4xQ0vgpCUPBtaRkO8XUpl2g15V4Io5sWVqg4WGnVI1k9QAxs8SA5Q8MwsPT6zwY6pgHdFmKk2xD%2FcTddfSjhxTb19t3TwsSn%2BaoZXkMPWFX6eCZMvIb%2FDbFqjtUIDFuFtkdPbT9Cea3cKKLtJb7maIYeki8AGEznlI57vwqS5nRKzwi0sm%2Fj7zI8SttfKL7dViMcDYknjsL22I8CLYHGfrNpUqF9t25EaPceUWBwFg326IYT3rRYOSqAMNGAfpsd9rixwCjdt31TVoI%2BB4ajwlPa6Pr9QuAL&X-Amz-Signature=844ad27e347d6b387d725c90e9ecf4d4772c6abc3fc1a985a0988559c0a5c3f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
