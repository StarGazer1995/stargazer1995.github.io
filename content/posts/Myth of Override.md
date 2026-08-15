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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWR7ENTF%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T003321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIB9tXPgjZr89j1Zs6EvrBjq1XNBHOA1m59UCFeo1plAJAiBNSIQbgW%2Bf7fldcR2CzpQokIClo5XkqaAJ4U6M1MEYcSr%2FAwgIEAAaDDYzNzQyMzE4MzgwNSIMErCKeaBSGa9PlN2QKtwD1Szn4YQGY4ZyXm27I0bLc6jQ01akbDUU6ZgPh4Ywz21DNG%2BJivWClLRAyU0EJMg8YUiA0JuF8d4P3%2FqZACavc0mhRul9JXMFG8i%2Fd4OSlTKnxNqYIgngq3QV73XzQ68ZIFBcU4s28TKEfbN%2BGP0tMVWnhUTOvOM0mhXVHtw3uqMRlmwrnftW0BZDp07t8a9K7wbMp6FKfFpLTURCxqHFSM%2BfKLh8Dqbnbu3G%2FQfp7Zz1oJJMa%2FCQhfyUKivE1YQwoFZMZgJ%2FCBb%2B%2BoZu4beOv9hbSWku8d9P%2Bry1MYhwNdYfVRaTxBiMiOLU6aljo3j738Rt7PM54kdejQslSNfj0xdVU7CaXMC%2F6JguMudDsMdt%2FAzKfkx4F69nSIOpvjDWf3TmKtl18PIZ8WJVeEnaD5uz7WC7OSxFCP7tXlvu1ieq%2BPPyFr55s95jHt2kWX7%2F4JWVVL4Tursp4pNM44UmOD6T6C5pqfLbyHHZKXalxemBfAj%2BSzx%2BLiF0VHRKZF585fm5ixned0JPNUCfVBLxevOwwcs9XAbsZDaMHuz85%2BvT3FLvtSnO%2FV0oD9LOF%2BRfHkzAYNdUp3U2Dnb%2BNwwFncfKdXNf7vF4TNYmdMIOvlmCGSPYcgk9%2FB%2FsrGkwxMb%2B0wY6pgHj7cobpI4zxs7V3oX4F35M9x6xm7%2B3qrj5HcGiyhc4BW%2BHgu7%2FkKNoIuIVw2acK5N7m4h4edulxuhmvH1UOGfKM1tWgHVOz3kud06eKCjHESR5EjGUcQYBaqTNjeF0b50ZqcPan%2BrVaMqgglsFTZLt3RAtL89EV%2FXL%2B95t6dfvGuobzpuGzQASX5kZOoW5bZjaOqOzHdUX7x3NAPGN8kW%2FploBjbPi&X-Amz-Signature=08f39ece225d9bada462838fb674d20ac2bf2d79c28845782aaea11e9d70c1b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWR7ENTF%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T003321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIB9tXPgjZr89j1Zs6EvrBjq1XNBHOA1m59UCFeo1plAJAiBNSIQbgW%2Bf7fldcR2CzpQokIClo5XkqaAJ4U6M1MEYcSr%2FAwgIEAAaDDYzNzQyMzE4MzgwNSIMErCKeaBSGa9PlN2QKtwD1Szn4YQGY4ZyXm27I0bLc6jQ01akbDUU6ZgPh4Ywz21DNG%2BJivWClLRAyU0EJMg8YUiA0JuF8d4P3%2FqZACavc0mhRul9JXMFG8i%2Fd4OSlTKnxNqYIgngq3QV73XzQ68ZIFBcU4s28TKEfbN%2BGP0tMVWnhUTOvOM0mhXVHtw3uqMRlmwrnftW0BZDp07t8a9K7wbMp6FKfFpLTURCxqHFSM%2BfKLh8Dqbnbu3G%2FQfp7Zz1oJJMa%2FCQhfyUKivE1YQwoFZMZgJ%2FCBb%2B%2BoZu4beOv9hbSWku8d9P%2Bry1MYhwNdYfVRaTxBiMiOLU6aljo3j738Rt7PM54kdejQslSNfj0xdVU7CaXMC%2F6JguMudDsMdt%2FAzKfkx4F69nSIOpvjDWf3TmKtl18PIZ8WJVeEnaD5uz7WC7OSxFCP7tXlvu1ieq%2BPPyFr55s95jHt2kWX7%2F4JWVVL4Tursp4pNM44UmOD6T6C5pqfLbyHHZKXalxemBfAj%2BSzx%2BLiF0VHRKZF585fm5ixned0JPNUCfVBLxevOwwcs9XAbsZDaMHuz85%2BvT3FLvtSnO%2FV0oD9LOF%2BRfHkzAYNdUp3U2Dnb%2BNwwFncfKdXNf7vF4TNYmdMIOvlmCGSPYcgk9%2FB%2FsrGkwxMb%2B0wY6pgHj7cobpI4zxs7V3oX4F35M9x6xm7%2B3qrj5HcGiyhc4BW%2BHgu7%2FkKNoIuIVw2acK5N7m4h4edulxuhmvH1UOGfKM1tWgHVOz3kud06eKCjHESR5EjGUcQYBaqTNjeF0b50ZqcPan%2BrVaMqgglsFTZLt3RAtL89EV%2FXL%2B95t6dfvGuobzpuGzQASX5kZOoW5bZjaOqOzHdUX7x3NAPGN8kW%2FploBjbPi&X-Amz-Signature=582fb29e4f98859ae500af50b022b47b32813335706c81e529855e2cf976677e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
