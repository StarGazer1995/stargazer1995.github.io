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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BZ56GTV%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T195712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEVJoF9H3aIBo4xi3o3zIUIVPJIBo5KnZxyhlH3TY48wIhANaA7emSWfRFk3nRA69WzUM88vwGYUJWnHGfqjrXA1%2BZKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKdc36Eevo251tpkQq3ANkCdETF%2BXrGCuMPN%2BOcXMEecSpAuos7kPnDa4d9W9%2Bwe053RRTV%2BNkk8XY8RvANdLLC95TlxZ4pyn2uuGPXCma56bM4qQDIrRgLb7AcxAvqklvsdUuveA3hvqjGtxo6MdbZj5HJAnb%2BXWOFfHZMVc9RWtdhjoqziN2%2FJxUGBU%2BNoDxUUtA9X1fOKI7VrLPniiqxOfdD7LwLDtNmdtNvtqf%2FlRSiVd9ugewirwE%2BtoXVlcUoBHdI0tISOHK6DvKqlajZRaIlmhpgH5rFQU3l7zN3GF6cIO7a1gi8LPXQJUWstwi80b57uEw4VpiVJbnieU4J8gbJ2xr279VOMuQepfqIv5LayjOYnqNZBn5sa0TVOEygygyGrhwsKZ38f4popdoi7%2Fs6WodudwFQR9oDf3lVKLVWzYnKPKNmAZqcEOAz0vZOvEbW5uhCGBIK5O12aWXxsSIqPLWI3ZVBl%2B031tUya5TQrkQ76tfH%2Feb%2Bc%2BQvc69ElYmJA6nkVY%2BdnePocK0rhFSB5bBLL5f5NOsw0V%2FD0tDmp08RGzxhOoh4N61ap5KUCWx6ojxf1Hg5z%2BZPEjGVkMf%2BzK97y50OtrBTkgN35oTODRuVqqfA58cvoRrY2j28FcfYn%2F1ns0EfjCc2MvRBjqkAWcMRSC0%2F3q6L%2B5UEzrdEyRIoYoD2Vgp93FcB0TwDClAdy4mT6rgE2p%2FnV1VXm%2BAlD6m2EShUxTkOWDOacOHeKSQgTkbEZA81LEFnXz3YpoBaJtVhz2kfLg9ppE9cgY04B0t3NYjH0%2FRcjueMtnPFg1O63ckl3iaRYbCEka6oeo798auduOgUx5Lb4ROG%2BaJvfIjaYqzXym4LfJlcVeR2%2BVxct%2B5&X-Amz-Signature=1f92a4d149b35df4c59fee09eecf4a8167b6f5a1b29a16ad0e873ec4f95be62f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BZ56GTV%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T195712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEVJoF9H3aIBo4xi3o3zIUIVPJIBo5KnZxyhlH3TY48wIhANaA7emSWfRFk3nRA69WzUM88vwGYUJWnHGfqjrXA1%2BZKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKdc36Eevo251tpkQq3ANkCdETF%2BXrGCuMPN%2BOcXMEecSpAuos7kPnDa4d9W9%2Bwe053RRTV%2BNkk8XY8RvANdLLC95TlxZ4pyn2uuGPXCma56bM4qQDIrRgLb7AcxAvqklvsdUuveA3hvqjGtxo6MdbZj5HJAnb%2BXWOFfHZMVc9RWtdhjoqziN2%2FJxUGBU%2BNoDxUUtA9X1fOKI7VrLPniiqxOfdD7LwLDtNmdtNvtqf%2FlRSiVd9ugewirwE%2BtoXVlcUoBHdI0tISOHK6DvKqlajZRaIlmhpgH5rFQU3l7zN3GF6cIO7a1gi8LPXQJUWstwi80b57uEw4VpiVJbnieU4J8gbJ2xr279VOMuQepfqIv5LayjOYnqNZBn5sa0TVOEygygyGrhwsKZ38f4popdoi7%2Fs6WodudwFQR9oDf3lVKLVWzYnKPKNmAZqcEOAz0vZOvEbW5uhCGBIK5O12aWXxsSIqPLWI3ZVBl%2B031tUya5TQrkQ76tfH%2Feb%2Bc%2BQvc69ElYmJA6nkVY%2BdnePocK0rhFSB5bBLL5f5NOsw0V%2FD0tDmp08RGzxhOoh4N61ap5KUCWx6ojxf1Hg5z%2BZPEjGVkMf%2BzK97y50OtrBTkgN35oTODRuVqqfA58cvoRrY2j28FcfYn%2F1ns0EfjCc2MvRBjqkAWcMRSC0%2F3q6L%2B5UEzrdEyRIoYoD2Vgp93FcB0TwDClAdy4mT6rgE2p%2FnV1VXm%2BAlD6m2EShUxTkOWDOacOHeKSQgTkbEZA81LEFnXz3YpoBaJtVhz2kfLg9ppE9cgY04B0t3NYjH0%2FRcjueMtnPFg1O63ckl3iaRYbCEka6oeo798auduOgUx5Lb4ROG%2BaJvfIjaYqzXym4LfJlcVeR2%2BVxct%2B5&X-Amz-Signature=2e7018fca01daea98ec4abcf2f8c47e7a3f2fed7ed68102b124a0429a55a11f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
