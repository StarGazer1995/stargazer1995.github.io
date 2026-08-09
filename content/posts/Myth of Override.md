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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XCNKMNF%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T201853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIACAVKEsNkV4l6%2Bp00KpM6OnCBA88NghjPDR5Ct6cJmmAiEA%2BD1OqP%2FkTsILyeBMVpTDu6qBn80DJPi3IR0MM%2BA1OIAqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGBEey7B6K0wcB%2BEiSrcA8Gg9d1b9CWiKf4%2BoHn59UdFUMNlNu6IWhP7IeBG%2B%2BdMp6Iu71LbkU%2FF8LCf2yPbwfhVgChHagNW%2BznfqSpd9OA97QZnIG2%2FBW5CeB9Xa5W9FUB31F28RISXrFnSHD%2Bq0LKxhvp%2Bo6ZrS5iL1APfL5bvYu6R6lwXvVkTfukg6bAJAtZu3jQy1B5tu6jLYdHmf4APGN2JZK%2BSBI8bUF5Jxj5skhwo7hhD3asWokC0G3AFMsaOxqLL0hMNgqET6fEYaApvZwfQuHmpryXi8R%2BAP5hNaz2HH%2F%2FyotnbA%2BWiPsKdoF8qvuhmuzrsLDzbItAcBsqzOCV%2B05SuzWesYJHc3bv%2BoeZkNoHPlPp1e7DQwrZITwA7RxFvIQj4YkI%2Fd%2BzPYB3jDRqAICdfR2Zwvtg7tHgruap1bnlMkOZzAVqTWfHflcO5GfvX8q16jWpVGsS1U8909D4PaTcSJmPezDcoDxnJAQAZUGyvTTJVAB7aKQ7w3Iwf9cauBEr7efWrU8v6jMRK%2BOAP9L84oPhLq5gY6hZFtlWj2NS5DQthu2SQCfDxbC5je%2F%2Ba4fn6J2XkqdWE7KPJ7nZ%2BbbKfrfZWi8Y3BUjodDL4a19izdtozsCPJ3n3C8pRbaVr%2BbspI09%2FMOab49MGOqUBtlto3Gmm3NMkjvzMYkQ%2BQsiv020KtMEz6JvJrl26igiesGK92F1vx80O6Vi0IpflTM8ZyXgQ5YHlSQMh7GP4Pbg4BO358%2BZOF1dY97t%2B1YGS4A5JJ%2FYm2wYMgna4gbZjauQbwQehWd3yxdcYHsfn39Q7xIQXJlwMKGXeQsofLsxvisFA6v9vdN%2Bfg9DDwoys0BBty7uapBR0AMHilXQZzYq7kqNQ&X-Amz-Signature=641debbfd4292767e6804e3904e05e669c4683ff459edb707af135a0e199ff08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XCNKMNF%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T201853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIACAVKEsNkV4l6%2Bp00KpM6OnCBA88NghjPDR5Ct6cJmmAiEA%2BD1OqP%2FkTsILyeBMVpTDu6qBn80DJPi3IR0MM%2BA1OIAqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGBEey7B6K0wcB%2BEiSrcA8Gg9d1b9CWiKf4%2BoHn59UdFUMNlNu6IWhP7IeBG%2B%2BdMp6Iu71LbkU%2FF8LCf2yPbwfhVgChHagNW%2BznfqSpd9OA97QZnIG2%2FBW5CeB9Xa5W9FUB31F28RISXrFnSHD%2Bq0LKxhvp%2Bo6ZrS5iL1APfL5bvYu6R6lwXvVkTfukg6bAJAtZu3jQy1B5tu6jLYdHmf4APGN2JZK%2BSBI8bUF5Jxj5skhwo7hhD3asWokC0G3AFMsaOxqLL0hMNgqET6fEYaApvZwfQuHmpryXi8R%2BAP5hNaz2HH%2F%2FyotnbA%2BWiPsKdoF8qvuhmuzrsLDzbItAcBsqzOCV%2B05SuzWesYJHc3bv%2BoeZkNoHPlPp1e7DQwrZITwA7RxFvIQj4YkI%2Fd%2BzPYB3jDRqAICdfR2Zwvtg7tHgruap1bnlMkOZzAVqTWfHflcO5GfvX8q16jWpVGsS1U8909D4PaTcSJmPezDcoDxnJAQAZUGyvTTJVAB7aKQ7w3Iwf9cauBEr7efWrU8v6jMRK%2BOAP9L84oPhLq5gY6hZFtlWj2NS5DQthu2SQCfDxbC5je%2F%2Ba4fn6J2XkqdWE7KPJ7nZ%2BbbKfrfZWi8Y3BUjodDL4a19izdtozsCPJ3n3C8pRbaVr%2BbspI09%2FMOab49MGOqUBtlto3Gmm3NMkjvzMYkQ%2BQsiv020KtMEz6JvJrl26igiesGK92F1vx80O6Vi0IpflTM8ZyXgQ5YHlSQMh7GP4Pbg4BO358%2BZOF1dY97t%2B1YGS4A5JJ%2FYm2wYMgna4gbZjauQbwQehWd3yxdcYHsfn39Q7xIQXJlwMKGXeQsofLsxvisFA6v9vdN%2Bfg9DDwoys0BBty7uapBR0AMHilXQZzYq7kqNQ&X-Amz-Signature=eb8f8c5f8e6bf7c0ad94a984cc4df6779dd2f7bc9d373e5c2a2e00a7c4a7a92c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
