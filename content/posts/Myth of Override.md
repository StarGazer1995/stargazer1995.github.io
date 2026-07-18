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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSDYYV73%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T144407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBMXdf0xcg1Z%2BqDP5DNuWrYtWhASsDxZQuxJ6oAPXgpAiEA7EbjuYHCEg2HmBgOYDORafaEWtx0Xucx3dNix0naiMgq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDCLLQ%2FKeFKPrBE3qtyrcA%2Bzz%2F8ZbiJdS%2BgtJxKpzcK9jDgihUsm71JpZESIU4treJqnd%2B4M7GobebifKuVtjyJ%2F05r%2B%2FPG4kZLc7CSTGD5dKi5MEUY2b5sDyJKGEQ8xdFFlOJNflfpgn55ts79voFlpCw%2BQUS2FHTu1SAV8d5rz%2FTYNoXxKWoD%2FFlvcYQi7w%2FlskVrUjIqzV9tajDW9HCO1pr%2Bw1tO7qBbEUY763ubQR5PIptl3NfF4%2FfUF6kzchbn7itTfuW7cn0vUgsaFRJ2RiWxrSFvmipMvLn%2B1yfMrZFoh%2FSRxR2R4yuBzkuGXl7H%2FF8EY66g2nnO%2Bq9GyCG1N1NbuqoXZomTCoswESZAGBQk%2BNiFPO0amF6jm%2Bz7PeukCUBh5tJxgccflt1XqE%2Bldqg3zIJJw2jaMR9f2yBqJFq4I4ayoIzI%2FwMdQWOGXOEFTdHgc7KEdkcGk4bBHqzz6zca8A0I0tRnzCTHvTDOL4NIO4jsm8%2BYmzae616d22EHyGfdcmddy9cpkGgVedtL3sPB6nacHgwzavbCsb21KD1JB2tL54dv6%2BHktxJXnkKkFIHZ6i%2BFRffeXisctwsQnatgZzf4Ef1glgHgRIwp%2FXQS43ZtZZAC21FIglpt0HpIJafoPZfS12gnLfMMyA7tIGOqUB%2FTJ1brN8JAKgSp3KJTUVT70FY15gRNc3%2FdV%2Bbutxr%2BeBwpus608wwg4ijjI6we6wcysd3TgaRQAa2Bw2P9Y0MOaJc52d4iI7PX6dN2%2Bma7GwFSWVhamLbVb8evQBB5udz8%2Bxvi5HpkeLiPphFyVwiDSxISSyCR0GNF1VnHtv%2Bf4PCYgWkYisZWhaOmZyIbolflAbV%2BVoi3WbN3wwuFGhSRBrt7SJ&X-Amz-Signature=83f2dca6596278e346101a91c0cadb4b503ddcf2f42a47266ae57df22471de76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSDYYV73%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T144407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBMXdf0xcg1Z%2BqDP5DNuWrYtWhASsDxZQuxJ6oAPXgpAiEA7EbjuYHCEg2HmBgOYDORafaEWtx0Xucx3dNix0naiMgq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDCLLQ%2FKeFKPrBE3qtyrcA%2Bzz%2F8ZbiJdS%2BgtJxKpzcK9jDgihUsm71JpZESIU4treJqnd%2B4M7GobebifKuVtjyJ%2F05r%2B%2FPG4kZLc7CSTGD5dKi5MEUY2b5sDyJKGEQ8xdFFlOJNflfpgn55ts79voFlpCw%2BQUS2FHTu1SAV8d5rz%2FTYNoXxKWoD%2FFlvcYQi7w%2FlskVrUjIqzV9tajDW9HCO1pr%2Bw1tO7qBbEUY763ubQR5PIptl3NfF4%2FfUF6kzchbn7itTfuW7cn0vUgsaFRJ2RiWxrSFvmipMvLn%2B1yfMrZFoh%2FSRxR2R4yuBzkuGXl7H%2FF8EY66g2nnO%2Bq9GyCG1N1NbuqoXZomTCoswESZAGBQk%2BNiFPO0amF6jm%2Bz7PeukCUBh5tJxgccflt1XqE%2Bldqg3zIJJw2jaMR9f2yBqJFq4I4ayoIzI%2FwMdQWOGXOEFTdHgc7KEdkcGk4bBHqzz6zca8A0I0tRnzCTHvTDOL4NIO4jsm8%2BYmzae616d22EHyGfdcmddy9cpkGgVedtL3sPB6nacHgwzavbCsb21KD1JB2tL54dv6%2BHktxJXnkKkFIHZ6i%2BFRffeXisctwsQnatgZzf4Ef1glgHgRIwp%2FXQS43ZtZZAC21FIglpt0HpIJafoPZfS12gnLfMMyA7tIGOqUB%2FTJ1brN8JAKgSp3KJTUVT70FY15gRNc3%2FdV%2Bbutxr%2BeBwpus608wwg4ijjI6we6wcysd3TgaRQAa2Bw2P9Y0MOaJc52d4iI7PX6dN2%2Bma7GwFSWVhamLbVb8evQBB5udz8%2Bxvi5HpkeLiPphFyVwiDSxISSyCR0GNF1VnHtv%2Bf4PCYgWkYisZWhaOmZyIbolflAbV%2BVoi3WbN3wwuFGhSRBrt7SJ&X-Amz-Signature=32f1030299965fc9855853ebf9643b51eaa2905878e671e09c58b70467ae1eab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
