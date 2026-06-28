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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MUH7V32%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T102009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERgOJy8LyO6htg9Dw8WSb8XMrW0aKYu0NNT8R%2BlaQtgAiA3khmd49gEva2vcK4QoyRjiRQzZHfeudVeID5JVbdYjSqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMP5C%2FF1uWCz4hrFjeKtwDldctD18KJcBbIFJ7GeWt4%2F3r%2FNlkH65MaqbbXSWVAB9UE%2B5AJRNqDy4JRLN6tpImUdU7iVdjuZrOj1%2Ff42Bm0kmKm6775RHFmD7ZIQT43UP0qbPJDUflITCW6xvWaDHXCPKKrDp6ymhPCzYN9KLCtdoxNSJ7rNbXJCmrAmk%2FTS%2Fav7mrB%2B7a%2FA%2BzF%2BdZGtSDV4pxtjiuS9Q65hB0uCuTg7aicU%2FnDUaBeLWIlUUrzw%2BJ%2F9GlsSkBIGT8b54EvJ9w1uLTl2OE%2F7Zt3LNyOcl6P5L5WnEi3pnAggYtzp5bpCqnsh%2BUUfYH53zrufc%2BMwy7HPNzllKpP8ECYXTSdCyRJ7nVSurwH%2Fd07iXpy64mfomizsHqmVP01tYdwJnibJqBizBx6eRKIQQaSTN%2F9xBuCdPVKVIVgTUZPZR6TupfKwUH2KXj%2BDzDbbwKEyeHpeOdTsRWZtNmwdn5V9PTp9JMjbtmSW%2BfhjISGHVCD7Jy23wHVQ%2F2cQfUyTsMdn89jrDFM3bq9zm415dWv9lO%2Be%2FC%2FrshTNx9JNIBgFdXxSsZ7hh4YNcU6S3gdBW6aaa42euCKnuEDTXJo84sRTL0ENDotqS1dXqo27524wt5DhebJGhDXXGl4GqJorYH%2FIYwqtKD0gY6pgE%2FjGYSQ2NLAldzJLZ4OY1ghHFG5RIwmvrjGih1Mz26Lrl6qr%2FpjcSavojfD9QzfjfoafvTlR8QMwd9aL9bP8rqfDaCR6HgjNjGX7O7%2BAGvnjCUKcoX2QsmtG8DKeRpA23AJPdywofZOVWnOF8f%2FZllxjbQm7MZKkYea8HQScrycdxp%2F%2Fsn7svJQs8NrWHywOlRseOaOMewdIeiJOxy4NhTORZae2ns&X-Amz-Signature=f3788eea1b4ff59e343e16f8e842a8793dc20a39107ce8549cedded9cbf57c64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MUH7V32%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T102009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERgOJy8LyO6htg9Dw8WSb8XMrW0aKYu0NNT8R%2BlaQtgAiA3khmd49gEva2vcK4QoyRjiRQzZHfeudVeID5JVbdYjSqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMP5C%2FF1uWCz4hrFjeKtwDldctD18KJcBbIFJ7GeWt4%2F3r%2FNlkH65MaqbbXSWVAB9UE%2B5AJRNqDy4JRLN6tpImUdU7iVdjuZrOj1%2Ff42Bm0kmKm6775RHFmD7ZIQT43UP0qbPJDUflITCW6xvWaDHXCPKKrDp6ymhPCzYN9KLCtdoxNSJ7rNbXJCmrAmk%2FTS%2Fav7mrB%2B7a%2FA%2BzF%2BdZGtSDV4pxtjiuS9Q65hB0uCuTg7aicU%2FnDUaBeLWIlUUrzw%2BJ%2F9GlsSkBIGT8b54EvJ9w1uLTl2OE%2F7Zt3LNyOcl6P5L5WnEi3pnAggYtzp5bpCqnsh%2BUUfYH53zrufc%2BMwy7HPNzllKpP8ECYXTSdCyRJ7nVSurwH%2Fd07iXpy64mfomizsHqmVP01tYdwJnibJqBizBx6eRKIQQaSTN%2F9xBuCdPVKVIVgTUZPZR6TupfKwUH2KXj%2BDzDbbwKEyeHpeOdTsRWZtNmwdn5V9PTp9JMjbtmSW%2BfhjISGHVCD7Jy23wHVQ%2F2cQfUyTsMdn89jrDFM3bq9zm415dWv9lO%2Be%2FC%2FrshTNx9JNIBgFdXxSsZ7hh4YNcU6S3gdBW6aaa42euCKnuEDTXJo84sRTL0ENDotqS1dXqo27524wt5DhebJGhDXXGl4GqJorYH%2FIYwqtKD0gY6pgE%2FjGYSQ2NLAldzJLZ4OY1ghHFG5RIwmvrjGih1Mz26Lrl6qr%2FpjcSavojfD9QzfjfoafvTlR8QMwd9aL9bP8rqfDaCR6HgjNjGX7O7%2BAGvnjCUKcoX2QsmtG8DKeRpA23AJPdywofZOVWnOF8f%2FZllxjbQm7MZKkYea8HQScrycdxp%2F%2Fsn7svJQs8NrWHywOlRseOaOMewdIeiJOxy4NhTORZae2ns&X-Amz-Signature=91a5222459b265db1a92ddf4ea5734d051ae075901a78c57585d172be004bf5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
