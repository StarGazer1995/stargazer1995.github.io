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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CC5W6DX%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T041925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJIMEYCIQDrJPjmp9iTVXlR01FNnRGt9JxSltZcAcEcQw1imFLlOQIhAP9EMKrx4ccFl5zJpQpUeQFKeeZTbtLExXbpKlKH1iuqKv8DCAsQABoMNjM3NDIzMTgzODA1Igw7MUmBiKQ0Nfyxq9Mq3ANl9CnCszcs1hmfHg92JAF%2FwewQ5el%2Fenv10sbOjUMR%2F%2FEWUFS%2F0GPElYgOUay1Ql6jjqb05wVfjfaBRpvDXfBzYjs44RyvOKpE4MXVPOksLnt8bmSGqExrU1k5ysvVUBgjJCfegewTrHQ4u4%2FS1DQ7qBgGTMTE5gN%2B8f6JE0ERtn972H7knMisBYyQppOKiueU2fg5eLxnw6ZRt7MU86BlqN1Qc51FL5tl2UKVgGk2pA7SFApn84QmWtxdprG6Sy8NqMSTEwd0PwgpnvYZlrMmG%2B0zIziY700tpRzTZEVcvNvkTuaVSWIgqywD6%2BZngLx7SdsB%2F3po4nKbwVm28V5q%2FFoIW%2Fe1fb7pRFmeGIS4wHtO68XpAO72guLv%2BzrQKibaG2dK%2F6POUBTW%2BowJYlue0G3yQ7cMZxZzskXoafu3QILCVVNF8nHosstMj5RwGJ4DX8OmpneSvA83tyjKj3WbjM3hqk%2B%2BOPyXHRuau68h42YsolSfPU2wk%2FL7cy5%2F2PT5fyDIf8Aq2b6O%2FP91WCOQ1Y8%2F%2FbLlTCxUNtp8iMwyyLFuXDR2ixHknUCW2zhOkG1iTCxZpU7XaCMhzZg%2F%2BfUzh7UvQ31ewuex8GMEZytYI88kOkFT2LiDvqm53TCtgP%2FTBjqkAU7xFHzt5jbsiUZ3NQL9g5OOVP2NxTaso1mWaddULuNeS%2BaNazZJl2mQLdRzZqygowYbTVtuonQDmqnQf5X39OIaLdHYgJ7r7ksAY80SxpD34R6rcjzk61w6D8QH1Ne40IAYcCz5ZZmTne4NT9lGDnwTuM1WTstdKxKwTZ0C%2BPDjoq7HjBwj7YwI1qJGr78wIBzgffF9uPjuVoRIpgqYDwh%2FbgX3&X-Amz-Signature=598e8a6c32bed116fae33548ae9b8ca1c98888ca21bfe6961689e62c13c39f49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CC5W6DX%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T041925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJIMEYCIQDrJPjmp9iTVXlR01FNnRGt9JxSltZcAcEcQw1imFLlOQIhAP9EMKrx4ccFl5zJpQpUeQFKeeZTbtLExXbpKlKH1iuqKv8DCAsQABoMNjM3NDIzMTgzODA1Igw7MUmBiKQ0Nfyxq9Mq3ANl9CnCszcs1hmfHg92JAF%2FwewQ5el%2Fenv10sbOjUMR%2F%2FEWUFS%2F0GPElYgOUay1Ql6jjqb05wVfjfaBRpvDXfBzYjs44RyvOKpE4MXVPOksLnt8bmSGqExrU1k5ysvVUBgjJCfegewTrHQ4u4%2FS1DQ7qBgGTMTE5gN%2B8f6JE0ERtn972H7knMisBYyQppOKiueU2fg5eLxnw6ZRt7MU86BlqN1Qc51FL5tl2UKVgGk2pA7SFApn84QmWtxdprG6Sy8NqMSTEwd0PwgpnvYZlrMmG%2B0zIziY700tpRzTZEVcvNvkTuaVSWIgqywD6%2BZngLx7SdsB%2F3po4nKbwVm28V5q%2FFoIW%2Fe1fb7pRFmeGIS4wHtO68XpAO72guLv%2BzrQKibaG2dK%2F6POUBTW%2BowJYlue0G3yQ7cMZxZzskXoafu3QILCVVNF8nHosstMj5RwGJ4DX8OmpneSvA83tyjKj3WbjM3hqk%2B%2BOPyXHRuau68h42YsolSfPU2wk%2FL7cy5%2F2PT5fyDIf8Aq2b6O%2FP91WCOQ1Y8%2F%2FbLlTCxUNtp8iMwyyLFuXDR2ixHknUCW2zhOkG1iTCxZpU7XaCMhzZg%2F%2BfUzh7UvQ31ewuex8GMEZytYI88kOkFT2LiDvqm53TCtgP%2FTBjqkAU7xFHzt5jbsiUZ3NQL9g5OOVP2NxTaso1mWaddULuNeS%2BaNazZJl2mQLdRzZqygowYbTVtuonQDmqnQf5X39OIaLdHYgJ7r7ksAY80SxpD34R6rcjzk61w6D8QH1Ne40IAYcCz5ZZmTne4NT9lGDnwTuM1WTstdKxKwTZ0C%2BPDjoq7HjBwj7YwI1qJGr78wIBzgffF9uPjuVoRIpgqYDwh%2FbgX3&X-Amz-Signature=0ebce5e642fb1d6570d37d9389bf09847ee77d1df94fbbc2595d7ff3b8d16b11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
