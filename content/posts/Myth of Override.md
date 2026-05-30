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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3DRWVU%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T054100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDpjXiSpQAh0g0PGwSgDz0uHRf2E%2B0gncI4xNEBiCKr4gIge%2BhdEsmZyFnzV2FWlWROKbOa3wuF6tiDWIPAmtNE7vgqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPw5VTkX3pOgbdPdOyrcAwxprZf2r%2BOtpYle%2B2joUFatZjgGvVRtN4E6ThRSE%2Fvq21aIjTWNmHmE4hEeKewgs%2FxfvlCjcmDdgcRiUyFncYM6xyM77FX52VfCqV6qOL2xBG9TgPBI84JjTQ6JfEXRRtTCRvJTrwI48Fc69Aar7eOJoXiaVOhxzlFA%2FX08mUyeXPk2oMsDO4NfmwvwFsYQSr1FQvuDEuTHcV8x6IkkTGlrimQmj93XdpQChPlgoAMQjtkoANQ4igcYpwtdVCufu6EkBFRiTI3NEcXys%2BJa0vC9FIR%2B3aOOyJWniO9gwIzCzxyOyqtQWrUx2orVXfflT3lP7NtNWlEtr5vXjeCnNbVv%2FSy%2B3TML10TakC6FEjt15OP3sNjr0LHNd10bhi%2F95wLDIkjT1klluvyxRCuNJftYHay3st0KXfK2lxbwag6MDpeGDLI3lvSwXwlTg0i5jN4OFyTbd3fZ1k7nEYFZEnjOZKNrRKuPyht5odkKYX3RrgHE3aTC36RRh5WIqkQkGe663QrwLr5xkpqRGozc1%2BqukMkYPpGdGGoAK459PBeRk%2FxBquZ0vlVK6%2BdHuI%2B9PdLVz1nUcFAM5NCyRnQ6uDxpdFoPdosZ%2BBDqpWztZlpdjnb6qB%2FTHzj%2BN8kvMPfW6dAGOqUBKaqJitu%2BTAC3H0i%2B9Nifcw%2Brv%2FtRPvLutlkbdWw8nH5miJQjDXd77%2BiE0mbTXOHM%2FXpmxOyEVLNZOi0DuCjloyv61c9ehVeBt2Z1yEi%2BvTyOP7aQmQ9reJ%2F%2BCvVkvPLBsufkJIfoVsMPTxaaEkW8%2Fn7eoGtdM0kvx%2BglG8uS3ee5%2BziYPxne6PF6rsOf7Fvw0afwmCggbLNVqMSg%2BRB%2F9ppl3vYx&X-Amz-Signature=4f843e4de4fa35040632f45e13b44b5dd47fc5976c1e0673e19e4e7cab219234&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3DRWVU%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T054100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDpjXiSpQAh0g0PGwSgDz0uHRf2E%2B0gncI4xNEBiCKr4gIge%2BhdEsmZyFnzV2FWlWROKbOa3wuF6tiDWIPAmtNE7vgqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPw5VTkX3pOgbdPdOyrcAwxprZf2r%2BOtpYle%2B2joUFatZjgGvVRtN4E6ThRSE%2Fvq21aIjTWNmHmE4hEeKewgs%2FxfvlCjcmDdgcRiUyFncYM6xyM77FX52VfCqV6qOL2xBG9TgPBI84JjTQ6JfEXRRtTCRvJTrwI48Fc69Aar7eOJoXiaVOhxzlFA%2FX08mUyeXPk2oMsDO4NfmwvwFsYQSr1FQvuDEuTHcV8x6IkkTGlrimQmj93XdpQChPlgoAMQjtkoANQ4igcYpwtdVCufu6EkBFRiTI3NEcXys%2BJa0vC9FIR%2B3aOOyJWniO9gwIzCzxyOyqtQWrUx2orVXfflT3lP7NtNWlEtr5vXjeCnNbVv%2FSy%2B3TML10TakC6FEjt15OP3sNjr0LHNd10bhi%2F95wLDIkjT1klluvyxRCuNJftYHay3st0KXfK2lxbwag6MDpeGDLI3lvSwXwlTg0i5jN4OFyTbd3fZ1k7nEYFZEnjOZKNrRKuPyht5odkKYX3RrgHE3aTC36RRh5WIqkQkGe663QrwLr5xkpqRGozc1%2BqukMkYPpGdGGoAK459PBeRk%2FxBquZ0vlVK6%2BdHuI%2B9PdLVz1nUcFAM5NCyRnQ6uDxpdFoPdosZ%2BBDqpWztZlpdjnb6qB%2FTHzj%2BN8kvMPfW6dAGOqUBKaqJitu%2BTAC3H0i%2B9Nifcw%2Brv%2FtRPvLutlkbdWw8nH5miJQjDXd77%2BiE0mbTXOHM%2FXpmxOyEVLNZOi0DuCjloyv61c9ehVeBt2Z1yEi%2BvTyOP7aQmQ9reJ%2F%2BCvVkvPLBsufkJIfoVsMPTxaaEkW8%2Fn7eoGtdM0kvx%2BglG8uS3ee5%2BziYPxne6PF6rsOf7Fvw0afwmCggbLNVqMSg%2BRB%2F9ppl3vYx&X-Amz-Signature=e906a9738b188b4bf3aaaca2e0aed98f01f73e378ca7d0be8a69369b2404c018&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
