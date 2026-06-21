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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z4EGWB7%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T210328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQC4L7me4BZmOlwf6uk5wVBJdF7voq6ykyHX3viKrtNXiwIhAIesyVmS9X%2FQ%2FzfWuXGqkCF%2BIYjUajwWuAv7dPTEl7ciKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw837Iuy4c3QBgxpCwq3ANdjdzYG74sHYanC93jpOYTiJA8ra3BF121W%2Fl9uOT2iv0UJ%2F%2B8Z2K3DrXK%2FyGwJZdYvUKt3J5uL9BiNXJsvoKyifwUby6CFB9GVexxACQipCksSN9a89QVNBeZkr61rw6nvcHm2p9EeNMffzOAX3f2NtXQ92GuREzrnXrRMpnkANvVqUTlZsSun0ja%2F1pneeqxcTdFhM6c4Y4veJ1a80%2Fq5h%2BF70U67Eni%2FdVzKlYaRNvYdG7%2BSdAqmWUKTqgZzlOe8Y4c55o7PT0LvgIjJsoipfLMSCl%2FHcAUKQmHzOsiN7c7ktOUQZm1nlApJLDlJl4NMqdvJPUgC8eZhofRS5oSBx9TmPdcnHhrQEXOi0%2Bw8Njh79J0hubUHdwgpd2OmcY4i0OiKUx77Tzubz1ALWw6%2BMr51JVpWA70QIf5veHvT%2FgN8RNf8hcrN9p2JZR1Bj01c0Itr4p%2BG5bEEPOWIzN41x0dFzLJYYS%2BKQFdIJd%2Ba%2B%2BJ86i%2B5lO00O1WgEnvc8ulPFfoVTBt8E8inoRY9ahhu23%2BXNKIcaTqEFNGZ7tNin8iGm82VOMRKl5fvToClZzVY%2B34mnIUmWwivwVXgJQku0TV5wupkCld3ZSo5zH8DIeNKTBwuPMwAybGMDCag%2BHRBjqkAZKDXQxO1oIIwJuwIReu0mGxViAoY0zD2XfOa8D6nGU0IHVTdmkoDbp6gPMIDhsp2I2J1a8OVlbCznl6vSuW51hDtA6CYWcNwoEi9Fvxm%2BWkgKqYQjO%2Bb%2FSqvNI5LerTpVTaAyJhcFqHDe9s%2Brmoesnjjs5%2BiJ31Dn6rjaJpoKb7R6jXwdVaSPMgOyoVIYLicZHP7yNb9yXcuF20blv4NQm18984&X-Amz-Signature=f6c6f914f2fbe9e4e000c9322f91d186e2cb211f66026a587e8aa0f895a51e38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z4EGWB7%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T210328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQC4L7me4BZmOlwf6uk5wVBJdF7voq6ykyHX3viKrtNXiwIhAIesyVmS9X%2FQ%2FzfWuXGqkCF%2BIYjUajwWuAv7dPTEl7ciKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw837Iuy4c3QBgxpCwq3ANdjdzYG74sHYanC93jpOYTiJA8ra3BF121W%2Fl9uOT2iv0UJ%2F%2B8Z2K3DrXK%2FyGwJZdYvUKt3J5uL9BiNXJsvoKyifwUby6CFB9GVexxACQipCksSN9a89QVNBeZkr61rw6nvcHm2p9EeNMffzOAX3f2NtXQ92GuREzrnXrRMpnkANvVqUTlZsSun0ja%2F1pneeqxcTdFhM6c4Y4veJ1a80%2Fq5h%2BF70U67Eni%2FdVzKlYaRNvYdG7%2BSdAqmWUKTqgZzlOe8Y4c55o7PT0LvgIjJsoipfLMSCl%2FHcAUKQmHzOsiN7c7ktOUQZm1nlApJLDlJl4NMqdvJPUgC8eZhofRS5oSBx9TmPdcnHhrQEXOi0%2Bw8Njh79J0hubUHdwgpd2OmcY4i0OiKUx77Tzubz1ALWw6%2BMr51JVpWA70QIf5veHvT%2FgN8RNf8hcrN9p2JZR1Bj01c0Itr4p%2BG5bEEPOWIzN41x0dFzLJYYS%2BKQFdIJd%2Ba%2B%2BJ86i%2B5lO00O1WgEnvc8ulPFfoVTBt8E8inoRY9ahhu23%2BXNKIcaTqEFNGZ7tNin8iGm82VOMRKl5fvToClZzVY%2B34mnIUmWwivwVXgJQku0TV5wupkCld3ZSo5zH8DIeNKTBwuPMwAybGMDCag%2BHRBjqkAZKDXQxO1oIIwJuwIReu0mGxViAoY0zD2XfOa8D6nGU0IHVTdmkoDbp6gPMIDhsp2I2J1a8OVlbCznl6vSuW51hDtA6CYWcNwoEi9Fvxm%2BWkgKqYQjO%2Bb%2FSqvNI5LerTpVTaAyJhcFqHDe9s%2Brmoesnjjs5%2BiJ31Dn6rjaJpoKb7R6jXwdVaSPMgOyoVIYLicZHP7yNb9yXcuF20blv4NQm18984&X-Amz-Signature=3d888184a11276200a6883ec2f8b53af5de620e1939af09bc1dd3b045dca040a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
