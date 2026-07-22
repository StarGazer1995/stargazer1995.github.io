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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L5JEHG3%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T152616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQCjj74ahiIySW5oeE6TMaVhJI6g%2FCGlcu9JHUvviLTKDgIgPaAS%2FpYD37Tg%2FlBjszZZAwgAoIdLjBDwPjrUjc7zTjEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFM69P1EuNW7HrYJSrcA4CMIZzupdQ0%2F0LsqZxEpK2axN1hTWVF5Tl6hTuqb3DFYUE9oMwi4y3uCeDrmMiD16YAL%2B1DmevI7m6pTOECi%2Bfmft14b98gQWYAOjRHHZCqS9ABfhUUxxeLJhG9VIzPLbNUaDbm8wEnH4nO%2BrRFPc9Mz4qFmfSWATeGmFQ5mrCmFNJ%2B8fvZmVD9UHAmPjRRLrjYnzKcdAGx1SjLnxCs7Gb2aKcPB151mPJvLE2igODIeo4fO6MvCYR2%2B%2FmFs8VoyN9PUNoQIwrGBAJQQ%2FjjNK421f916AHaxvZni5cNouslOigzq53z0SvYeE20R6GvC4XWd15RWccUrBw83uX5slZYtjucasYoruUGtbheXZKrLaPw6F04rQPZxg%2Fq06sHZQFG2CBN%2BXQYlpIFd923WkuvPDobF8O9aVVvpj%2B6WPt5W1bVLwhFhJDwGzMefJvC6z8%2ByIxK%2B2X9cekBXVeAymx4Depdhe4p50ynzSNKJ9DM772Ab5stDCV52lRzD1ap6Uk4bnjvsKfx9DQXW%2FYT4%2Fb0kOoFKO1LJSr6cyiByebxYk5FvUkiVbFQKdKpxfy5voSYRPXu7QLDkODdQ2DnJnnlOMsKOI2vC4QwPWfpt3PuYZ9gvtoHUPPnpOFFMPWVg9MGOqUBAfgFKs6%2F3iiFexRFiMGg%2Bf7pXHWr%2B6hluLWTE7j6kav2zYjfe0dGtW9WWxK%2F%2FfrOHSDMYxx4VVNUNfY7KQ%2BkyI2JacF1w2kSo36VAiz4v%2BjY49Wsai5zLEmFNUeH0s0Gd%2BxDiQ%2BMk8Ii1VsjpK0ET1D3xPuMgGKaiNeYEh3ra553Bc6zX9QOSUnkePcK5w6SdidlwVXRHMFSPBj0sfwWD38IrGYm&X-Amz-Signature=573668738309131bb83447116382de5ebf7bf686f9c3713806f589045deb7a7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L5JEHG3%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T152616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQCjj74ahiIySW5oeE6TMaVhJI6g%2FCGlcu9JHUvviLTKDgIgPaAS%2FpYD37Tg%2FlBjszZZAwgAoIdLjBDwPjrUjc7zTjEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFM69P1EuNW7HrYJSrcA4CMIZzupdQ0%2F0LsqZxEpK2axN1hTWVF5Tl6hTuqb3DFYUE9oMwi4y3uCeDrmMiD16YAL%2B1DmevI7m6pTOECi%2Bfmft14b98gQWYAOjRHHZCqS9ABfhUUxxeLJhG9VIzPLbNUaDbm8wEnH4nO%2BrRFPc9Mz4qFmfSWATeGmFQ5mrCmFNJ%2B8fvZmVD9UHAmPjRRLrjYnzKcdAGx1SjLnxCs7Gb2aKcPB151mPJvLE2igODIeo4fO6MvCYR2%2B%2FmFs8VoyN9PUNoQIwrGBAJQQ%2FjjNK421f916AHaxvZni5cNouslOigzq53z0SvYeE20R6GvC4XWd15RWccUrBw83uX5slZYtjucasYoruUGtbheXZKrLaPw6F04rQPZxg%2Fq06sHZQFG2CBN%2BXQYlpIFd923WkuvPDobF8O9aVVvpj%2B6WPt5W1bVLwhFhJDwGzMefJvC6z8%2ByIxK%2B2X9cekBXVeAymx4Depdhe4p50ynzSNKJ9DM772Ab5stDCV52lRzD1ap6Uk4bnjvsKfx9DQXW%2FYT4%2Fb0kOoFKO1LJSr6cyiByebxYk5FvUkiVbFQKdKpxfy5voSYRPXu7QLDkODdQ2DnJnnlOMsKOI2vC4QwPWfpt3PuYZ9gvtoHUPPnpOFFMPWVg9MGOqUBAfgFKs6%2F3iiFexRFiMGg%2Bf7pXHWr%2B6hluLWTE7j6kav2zYjfe0dGtW9WWxK%2F%2FfrOHSDMYxx4VVNUNfY7KQ%2BkyI2JacF1w2kSo36VAiz4v%2BjY49Wsai5zLEmFNUeH0s0Gd%2BxDiQ%2BMk8Ii1VsjpK0ET1D3xPuMgGKaiNeYEh3ra553Bc6zX9QOSUnkePcK5w6SdidlwVXRHMFSPBj0sfwWD38IrGYm&X-Amz-Signature=2fedb655b11906b67a564d6dc3e8d8726967df7992857a9feaa63a5a75cf6b6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
