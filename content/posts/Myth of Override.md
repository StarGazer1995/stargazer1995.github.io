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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L55FG3X%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T192229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqmGvpbHBTNApay%2BgIs%2BupXuq%2FIiYi38yGT2vq3%2B0ccgIgX60%2Bh1F9yzukURVFv7%2BFQC7sEqGwvdR7YWfwAu5kF2EqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJp9%2FyJqyxUecdTJKircAzGNocI2fDquvtdJ5A7QhYD2EuqZ9DHya399xmDTkr72c4XId%2BF2MliuyEIMsKWmZ8bw7ToxIfJzfwpfJ10XdLCCM25WP35sN4GFpPPdK0ZHYsdvsH1HpKdiQjbKQYnVUZ7mvk6PvEPePd5CI8TW7eJggsMcG%2B6THaX2zi4E90rNbPbdRTgRXV%2F82e6lLvFidcT3cP%2BWKrM8iZeC8iQJnrh2gb0cMIww58cGHTzIqcAAfk8L9UK3XJFcuZe3EwfkdQqt3sIK9AS4ok%2B5kPrzZyru%2F2IzrU3DLc4r%2BjZ1w1k6YOVFwRB6fJ9KKzgqgHEUB5MzGH1kzXvfm44ZmZxROq2m4uNWn26SKG52SIR5nhjBgWP94tMwqq4pL8I5CDNJgcdRdz2WF%2Fhk%2B8VLTxGLLL8lIc3ZPU3xuU3jAldPdSVCDMyQN1DCIdXjE21HxQLdlMRppAFcdcMHAJ5osR4nosjGSt7s8A2AgLq%2Fzf4tZG8aIv29duJz72Y8w2Ezs%2BiIeS3uX7xs%2Bj8pVNbc9VvKcc1%2FGk3BGtLwUqVMvOvXp7tR7hQQaTFjbNmoQzfr2%2BAT6UeK083bIliS1EcPPH7h4pZ85OiwQryH1%2F2CAm%2FOeuEp5T4b%2FfUwhbpyD8UNMODR%2BdIGOqUBhbqNrESCsur9XM0uA0p5RL%2F9Cx1OZ85aZ1x01F9vpG6I2Z1vgaTk%2FlpGg%2FOkLP9qZtykn3c1m9gJyCWxQPWD9h6odgdqiRmfmEcxyMWeTfUSUjXSRNHAdpp0NpDRC2v4OiDrQVBAydef5yNprMiuYmcZebOHbi1%2B2aXdJUx61HacGTUdRffRpoO%2Fc1kVa%2BYQYalHV5%2B9u%2B9EcJTijRr6SgDaPL4U&X-Amz-Signature=7d6d1f4e7496df3b3d1fece81ad5d679aa3275c8398dc88797a47270d1a223fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L55FG3X%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T192229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqmGvpbHBTNApay%2BgIs%2BupXuq%2FIiYi38yGT2vq3%2B0ccgIgX60%2Bh1F9yzukURVFv7%2BFQC7sEqGwvdR7YWfwAu5kF2EqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJp9%2FyJqyxUecdTJKircAzGNocI2fDquvtdJ5A7QhYD2EuqZ9DHya399xmDTkr72c4XId%2BF2MliuyEIMsKWmZ8bw7ToxIfJzfwpfJ10XdLCCM25WP35sN4GFpPPdK0ZHYsdvsH1HpKdiQjbKQYnVUZ7mvk6PvEPePd5CI8TW7eJggsMcG%2B6THaX2zi4E90rNbPbdRTgRXV%2F82e6lLvFidcT3cP%2BWKrM8iZeC8iQJnrh2gb0cMIww58cGHTzIqcAAfk8L9UK3XJFcuZe3EwfkdQqt3sIK9AS4ok%2B5kPrzZyru%2F2IzrU3DLc4r%2BjZ1w1k6YOVFwRB6fJ9KKzgqgHEUB5MzGH1kzXvfm44ZmZxROq2m4uNWn26SKG52SIR5nhjBgWP94tMwqq4pL8I5CDNJgcdRdz2WF%2Fhk%2B8VLTxGLLL8lIc3ZPU3xuU3jAldPdSVCDMyQN1DCIdXjE21HxQLdlMRppAFcdcMHAJ5osR4nosjGSt7s8A2AgLq%2Fzf4tZG8aIv29duJz72Y8w2Ezs%2BiIeS3uX7xs%2Bj8pVNbc9VvKcc1%2FGk3BGtLwUqVMvOvXp7tR7hQQaTFjbNmoQzfr2%2BAT6UeK083bIliS1EcPPH7h4pZ85OiwQryH1%2F2CAm%2FOeuEp5T4b%2FfUwhbpyD8UNMODR%2BdIGOqUBhbqNrESCsur9XM0uA0p5RL%2F9Cx1OZ85aZ1x01F9vpG6I2Z1vgaTk%2FlpGg%2FOkLP9qZtykn3c1m9gJyCWxQPWD9h6odgdqiRmfmEcxyMWeTfUSUjXSRNHAdpp0NpDRC2v4OiDrQVBAydef5yNprMiuYmcZebOHbi1%2B2aXdJUx61HacGTUdRffRpoO%2Fc1kVa%2BYQYalHV5%2B9u%2B9EcJTijRr6SgDaPL4U&X-Amz-Signature=c72dac872acea5f2f49783612c1d6c56f68cefece3e922a12c9fb9d5040d5df1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
