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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRQWD7T4%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T114742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnTi2kqmU90aa%2FXqsiBms9FXDyVzcDHdTkKxoCmIai3AIhAOPli9DucmagrTRU7CrWlG0XZtJT7AGha%2FRW4G%2FZ%2FBbNKv8DCHUQABoMNjM3NDIzMTgzODA1Igy%2B3gDFoAhe4fTo%2Bzkq3AOgKRz%2BabNK1zrfb7kXeHelOc8H%2BBlOjI6iOKlJZbbJiroM7HTnDGCxtp2ECVZE2QRgxbW2kSkACksZqMAtC9LC0S83r2%2FjK3VlxbC9%2BMGEZX9NH%2FhbjNp6KljdMRkAS8m2%2FU9wP0Ys4G4MjwzhJBBRpIbwA10sxW0CcLFLByvpIZBkzXt6N4f4A80gwfT4mzx6IYhgcepo%2FLh%2FesTFx7OW4IRWwBf4jDEhXey0CHHCMZlQfxfGoHgosBObqansQ%2Fjc29Dh%2FfaS4rkDwmDk17n%2BT7u%2BAeVRj%2Fyl2xLm5U9JNZEyExsFQ9%2FtDqv4PCKWf2M20wefYIIwzcTcwhqtW6aYhUQ%2BSQjDIG%2F1tdPWxsW6%2BNyjyr0YSEs5fM%2FuJDRlnYmt3u%2FdGN159Y3FtiMkB3C39LbGTfHmQgCI11qHnVUVbTKoJRdtI8Vi5GqHnmPDlS0uKVU5zhxPWg0MAfsqeVXcsaYv7I5XGnscTzBwK%2BVFSjC9I9DVL6nJwFw0EyEjm%2FzEPifP3hM1zV1YyEasENB%2BBLL7pmLw2ztfr3Xtfy1UqgOHXTMdJSMFPfIySvm8jNMKnFggcERBBCs%2BwAdxf5rMdWG0OHGu%2BiWBqg8k2VruiFh3ZFkxHW4NJ1C%2BbTCkipzQBjqkAfe3IPA4xWivoW6FnolRUfAcwO03icX48UwlMozHICEBPoBn9otdWcz1P%2FdfGUI5NBQvh6%2Beft97Wk7OksN%2Bpy4EgD0VUehDa5gy2BbQZD8z87puDirCTpG92HilzsfgiwaC9cnCJY2eNe3zN1F9UL%2BDE2zXZEW4P5t6OBiFNUYwo9MMF70ea7hOCLMpUslf19pf6j72477Dvn759hmIL9j9xeu2&X-Amz-Signature=03a2aa5a321cfee95885d759fd1f31e0d209b129cb72404d47df03dbdc1d49c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRQWD7T4%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T114742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnTi2kqmU90aa%2FXqsiBms9FXDyVzcDHdTkKxoCmIai3AIhAOPli9DucmagrTRU7CrWlG0XZtJT7AGha%2FRW4G%2FZ%2FBbNKv8DCHUQABoMNjM3NDIzMTgzODA1Igy%2B3gDFoAhe4fTo%2Bzkq3AOgKRz%2BabNK1zrfb7kXeHelOc8H%2BBlOjI6iOKlJZbbJiroM7HTnDGCxtp2ECVZE2QRgxbW2kSkACksZqMAtC9LC0S83r2%2FjK3VlxbC9%2BMGEZX9NH%2FhbjNp6KljdMRkAS8m2%2FU9wP0Ys4G4MjwzhJBBRpIbwA10sxW0CcLFLByvpIZBkzXt6N4f4A80gwfT4mzx6IYhgcepo%2FLh%2FesTFx7OW4IRWwBf4jDEhXey0CHHCMZlQfxfGoHgosBObqansQ%2Fjc29Dh%2FfaS4rkDwmDk17n%2BT7u%2BAeVRj%2Fyl2xLm5U9JNZEyExsFQ9%2FtDqv4PCKWf2M20wefYIIwzcTcwhqtW6aYhUQ%2BSQjDIG%2F1tdPWxsW6%2BNyjyr0YSEs5fM%2FuJDRlnYmt3u%2FdGN159Y3FtiMkB3C39LbGTfHmQgCI11qHnVUVbTKoJRdtI8Vi5GqHnmPDlS0uKVU5zhxPWg0MAfsqeVXcsaYv7I5XGnscTzBwK%2BVFSjC9I9DVL6nJwFw0EyEjm%2FzEPifP3hM1zV1YyEasENB%2BBLL7pmLw2ztfr3Xtfy1UqgOHXTMdJSMFPfIySvm8jNMKnFggcERBBCs%2BwAdxf5rMdWG0OHGu%2BiWBqg8k2VruiFh3ZFkxHW4NJ1C%2BbTCkipzQBjqkAfe3IPA4xWivoW6FnolRUfAcwO03icX48UwlMozHICEBPoBn9otdWcz1P%2FdfGUI5NBQvh6%2Beft97Wk7OksN%2Bpy4EgD0VUehDa5gy2BbQZD8z87puDirCTpG92HilzsfgiwaC9cnCJY2eNe3zN1F9UL%2BDE2zXZEW4P5t6OBiFNUYwo9MMF70ea7hOCLMpUslf19pf6j72477Dvn759hmIL9j9xeu2&X-Amz-Signature=bd9603f55ff020314b445df0c28c17120cdb6ca87bf30f44a10d334b94a4475d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
