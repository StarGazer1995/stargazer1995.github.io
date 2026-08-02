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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OSU2AZH%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T164454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCICDo%2BFVWLIYs%2B8USzLAY53igWh%2FuQ%2BH%2BfqGoJh%2Fi50U1AiAOK%2FFgcOS4A3KYaZ6kCZ1m9jJ3scx7Iw8TojyrMa4PwSqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd91MpqlklayKPwWuKtwD8W8xVqYl6yEDU8wQy80dblqdIOY8s%2FfZWHuClbVIR3uCrDqHFr9IyvmkyxBGyAZrXgWSr4Un1jc%2BCLGQ7g284zxdsQtpqiAIXW9A32AYWtyU09H6i2KXPH7YHQY9jNsXeHoGh3%2FnZ6%2BkfyqVSGTj3HIaWMAfIzSWZeof73f7rKOogWQQpbE7KCMLjMW3O45VOL8yvpTJRKvdWcIncwu79Xt7A95qidWOYzzz5fVYI9ES8bp9G2mbdzWKLKEIGw5H1whyXWnrxcDW0rRQC77eUjXKUNJikwzw3c47jHwnxl%2BLd6WnKtIEKfSQ1%2BFXxPS5IWuqDYfIsJaOwFLfudqYk5dCEopfqhvwzxe2mZu8N0cMdXtCpe%2Bw8MZx02ZPX4WHzuHwi7aAfiyS5ACjNaDZUIvUnTDDSk5etg%2FrcF0y6TddUhu86Fa8LFXDQEYrzjsB4w2qN2hcc9IaylGuZBtL5ypsrjmoXUxuQauqb2amlw18b8e8mef9dILtJe9FFl3yBnNoVG3ia9gNixB2Cx%2BKsQ%2FMwwjPKfIG1D%2F73dygNNy8C1OkwtrJejZ5xuf9WYxBInm4w96Y%2FuXXpPR9Dq5FNALEK4z2duD0UaXOGscw%2F%2FVTDPguZTH6cWfQso0wm5G90wY6pgHz%2F6r9pZLj%2BlBipmN2Mk3Us1xrQDZLLabt63NVSwhzgUqr%2Bwp6e%2B3z5eZNb7IeC1XpXdA3zCSKg%2BBJHiwu46WCHgqcT5gzDtGi1bZe2GQTGZZ5cSSaq9Wn%2BJ9PmncvhKwJXh7AlhHRukFdiaw0MtRcnP6WPmwo9pd7MNa4jCWryTtd%2BhWL8uWAMkDVDoO8u9zJvk1YQzd%2BJhi46zxLZ5I3juqDQYVa&X-Amz-Signature=31b431bdc84bb00bd02b62257546255834deb9e31efa1174b9755bbe784d4a5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OSU2AZH%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T164454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCICDo%2BFVWLIYs%2B8USzLAY53igWh%2FuQ%2BH%2BfqGoJh%2Fi50U1AiAOK%2FFgcOS4A3KYaZ6kCZ1m9jJ3scx7Iw8TojyrMa4PwSqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd91MpqlklayKPwWuKtwD8W8xVqYl6yEDU8wQy80dblqdIOY8s%2FfZWHuClbVIR3uCrDqHFr9IyvmkyxBGyAZrXgWSr4Un1jc%2BCLGQ7g284zxdsQtpqiAIXW9A32AYWtyU09H6i2KXPH7YHQY9jNsXeHoGh3%2FnZ6%2BkfyqVSGTj3HIaWMAfIzSWZeof73f7rKOogWQQpbE7KCMLjMW3O45VOL8yvpTJRKvdWcIncwu79Xt7A95qidWOYzzz5fVYI9ES8bp9G2mbdzWKLKEIGw5H1whyXWnrxcDW0rRQC77eUjXKUNJikwzw3c47jHwnxl%2BLd6WnKtIEKfSQ1%2BFXxPS5IWuqDYfIsJaOwFLfudqYk5dCEopfqhvwzxe2mZu8N0cMdXtCpe%2Bw8MZx02ZPX4WHzuHwi7aAfiyS5ACjNaDZUIvUnTDDSk5etg%2FrcF0y6TddUhu86Fa8LFXDQEYrzjsB4w2qN2hcc9IaylGuZBtL5ypsrjmoXUxuQauqb2amlw18b8e8mef9dILtJe9FFl3yBnNoVG3ia9gNixB2Cx%2BKsQ%2FMwwjPKfIG1D%2F73dygNNy8C1OkwtrJejZ5xuf9WYxBInm4w96Y%2FuXXpPR9Dq5FNALEK4z2duD0UaXOGscw%2F%2FVTDPguZTH6cWfQso0wm5G90wY6pgHz%2F6r9pZLj%2BlBipmN2Mk3Us1xrQDZLLabt63NVSwhzgUqr%2Bwp6e%2B3z5eZNb7IeC1XpXdA3zCSKg%2BBJHiwu46WCHgqcT5gzDtGi1bZe2GQTGZZ5cSSaq9Wn%2BJ9PmncvhKwJXh7AlhHRukFdiaw0MtRcnP6WPmwo9pd7MNa4jCWryTtd%2BhWL8uWAMkDVDoO8u9zJvk1YQzd%2BJhi46zxLZ5I3juqDQYVa&X-Amz-Signature=d793ab8f90bca7cb9a7c1d2a794a42d93487fc6114ab6e60f436c7de4d4388ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
