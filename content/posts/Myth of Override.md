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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQOCQKX%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T171735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQD5IdJCn9UaNmHvKQMRP84krCdoM3beoylTPj9%2FAYn9%2BQIgUBict8lXuQUF7Q6wiapNZpv%2FbqBOOVxA4Cx0VXcISsoq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOqr6fr4Kun1J5NVuircA0vtZcer8jfk7OnhJ6VR3q5sEmQt23AOYfcivG4b2hMp9tMucFeaBPuzeSFW6VuAEqv1uZl0c7s5Xb9kFu9LhJlW0RePdqU7aW60SQqU8vAza5qUUxLX42bLeaoFQNUZmHTuFA1Mlae4sl73pRYMPJ1INxAd9sZjmzvhU0%2BunLHlnMS5ufXijZ6l6wkct3ioJRWpNo7CquaCK15otLyvwM%2FnxljQlY%2FoICSU0VxDjYEdF%2BhGmUOboyaNWVoeETHTCwqxW8XWkuHXfTLZ3xmzl107%2FXE%2B0jmaGXd9gBTRY9jd5tY8sEY7Ec0lPsaTAoCSX2cTk%2B1tT9DZiqlSQN4vQROBsTgO9GRBH5wGf36jz%2FG9Jj1hDcTRySgSLLLm5rhPAq%2F%2FYt5J%2FNpmOL5hwT%2Bd2FvWjz0tdgTH310ysN7oiPQ2Gb88tt2WwOrz2LLWiVAhVEIdmGHkTdqYcmPkZAWJcJfG8MNu0omUOrMKigJxWJd8c6pNMrgIVO4bNzAais%2BoFrLkHJ8L%2Fgz6h73xGr1klB5P%2F3ml8Y%2BpOrvX3w6ESdsksCZ45WtNgaewXAq18gwNk21ltP8VAQPdv5HS2fB4MbtWA2L8iLYHzVVu4FXNgug%2BzLEaoNcHMMXkJ0zsMPXWzdMGOqUBF%2Fz5u6RsyIkB%2FbGQijjUD%2F0PqCPrjdDJaGaFjVmdME6fiztoE%2Fl9pGY9tDqpvhVpJt1nSTgdH9sK%2FJpI5N1cGjqfl%2BlavvkLkGeCk8YzwOXQl4iCdLn8%2Fl9SjK2ZnhBRuOMGOLzS1b33xkItmD2ZL0InEGrpo38UVPxF%2BKiwOfhiwIfqI40AdVBF8k8iYE4l73WKs7IWnfkyF6gF8f21GH3rLi4M&X-Amz-Signature=3691bda42b4d037adbcb9b38f2f4f9d5f3dde424622bfc1988aba9845ef040bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQOCQKX%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T171735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQD5IdJCn9UaNmHvKQMRP84krCdoM3beoylTPj9%2FAYn9%2BQIgUBict8lXuQUF7Q6wiapNZpv%2FbqBOOVxA4Cx0VXcISsoq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOqr6fr4Kun1J5NVuircA0vtZcer8jfk7OnhJ6VR3q5sEmQt23AOYfcivG4b2hMp9tMucFeaBPuzeSFW6VuAEqv1uZl0c7s5Xb9kFu9LhJlW0RePdqU7aW60SQqU8vAza5qUUxLX42bLeaoFQNUZmHTuFA1Mlae4sl73pRYMPJ1INxAd9sZjmzvhU0%2BunLHlnMS5ufXijZ6l6wkct3ioJRWpNo7CquaCK15otLyvwM%2FnxljQlY%2FoICSU0VxDjYEdF%2BhGmUOboyaNWVoeETHTCwqxW8XWkuHXfTLZ3xmzl107%2FXE%2B0jmaGXd9gBTRY9jd5tY8sEY7Ec0lPsaTAoCSX2cTk%2B1tT9DZiqlSQN4vQROBsTgO9GRBH5wGf36jz%2FG9Jj1hDcTRySgSLLLm5rhPAq%2F%2FYt5J%2FNpmOL5hwT%2Bd2FvWjz0tdgTH310ysN7oiPQ2Gb88tt2WwOrz2LLWiVAhVEIdmGHkTdqYcmPkZAWJcJfG8MNu0omUOrMKigJxWJd8c6pNMrgIVO4bNzAais%2BoFrLkHJ8L%2Fgz6h73xGr1klB5P%2F3ml8Y%2BpOrvX3w6ESdsksCZ45WtNgaewXAq18gwNk21ltP8VAQPdv5HS2fB4MbtWA2L8iLYHzVVu4FXNgug%2BzLEaoNcHMMXkJ0zsMPXWzdMGOqUBF%2Fz5u6RsyIkB%2FbGQijjUD%2F0PqCPrjdDJaGaFjVmdME6fiztoE%2Fl9pGY9tDqpvhVpJt1nSTgdH9sK%2FJpI5N1cGjqfl%2BlavvkLkGeCk8YzwOXQl4iCdLn8%2Fl9SjK2ZnhBRuOMGOLzS1b33xkItmD2ZL0InEGrpo38UVPxF%2BKiwOfhiwIfqI40AdVBF8k8iYE4l73WKs7IWnfkyF6gF8f21GH3rLi4M&X-Amz-Signature=f85dbed17d775f49c0d377bea5767d0f175c9c144a2b02afd6e54c49dcd70d30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
