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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WWKK63Z%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T015315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIG0sof6jP%2BmQqbvsfRjQ1AK%2B0exSI2wNv0mItmkoEpKcAiBo4%2BeWp5eSRhFA1zS9PuVVXFhUJH3tZJBK66CU0A%2Bz6Sr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMGgzWcyjeHlNjjItxKtwDRlvce2i9yQQo12O%2BerXEOqTsOI9BPvgRlFU8rYFeUL87cq2%2BAibkUXnUo%2BOvTAiqpfb5p7b2GPX55g8CwjV%2B4e15KHO6Kde3gn5qaisKt%2BqOE6w0%2BCa3la4Po560um1itc1XkfNXQpSA9cUI8tcLbCE2b9N%2BSu3wyFUTKbcJrp8iggM7rqR34Dcf3Xx09sdsIsAOGl75Lv04auvDOx6E8EkZTjei518PFl9J0%2FOH4FMFKZ91P7gaVi30rGe9yincfLw9YeEOWFWv1QWq6ZIZOj92%2BQ6Ph5m5iPT%2FC9l62zsNCw4CuhTq8hk0j7TMmZVAJJzfO4V2VVarFCpuo41uZ42v%2FOYPZZXW9no6Q3q6VsNzlpvVJHyXu6usJUUzF63wbrwapjZmko%2FtHfHfXhL4j%2F8I%2BVrddY3lM2To28Iq9ijOjbVMIDRg0iCXLaPfv3x5EjQOYSn9V%2Bnr%2Fyh%2FHl1rk6NSrsE2difXsUbZH%2FFxyCQI1vsK4%2BT6w%2FsfBz0jRuX6wQ2NWHyZl%2BfZ%2FRYupCdywHXwae9Myo0GtNgtqVeJbBLxIfwsbO2KeiWoFx9tNQmAqUl4BK2P3O%2BXLf7SWrIHqIOsmehSAOPXfNPWmk%2FdgaClhLFTWZ3HiFBY2g0w2Kmx1QY6pgFu30Twh096Acx7RPy6sc1ltr%2BXrws8KXPdCotq71frhbBl4ar6wksjOwAvOjIWRDhPGhmXqqpWz4r0e7D%2BJREPnT1WN035JwTl2bdg5k8KXc0RzlRzJ1z%2Fhiqb8RRcIv3sTrUnwkUgYPHLwVf8A%2FD28X2D8jta4g1PsDJUlD1k9ZSjFbYUXXYDxGFKGokrfBnSx6QhJatCiEKQoHJRJIwoCLx7j7NO&X-Amz-Signature=11b8c37d26ee86cb4cb99e45dcbfe361345d7549c97a45750ae8ecab9c312b11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WWKK63Z%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T015315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIG0sof6jP%2BmQqbvsfRjQ1AK%2B0exSI2wNv0mItmkoEpKcAiBo4%2BeWp5eSRhFA1zS9PuVVXFhUJH3tZJBK66CU0A%2Bz6Sr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMGgzWcyjeHlNjjItxKtwDRlvce2i9yQQo12O%2BerXEOqTsOI9BPvgRlFU8rYFeUL87cq2%2BAibkUXnUo%2BOvTAiqpfb5p7b2GPX55g8CwjV%2B4e15KHO6Kde3gn5qaisKt%2BqOE6w0%2BCa3la4Po560um1itc1XkfNXQpSA9cUI8tcLbCE2b9N%2BSu3wyFUTKbcJrp8iggM7rqR34Dcf3Xx09sdsIsAOGl75Lv04auvDOx6E8EkZTjei518PFl9J0%2FOH4FMFKZ91P7gaVi30rGe9yincfLw9YeEOWFWv1QWq6ZIZOj92%2BQ6Ph5m5iPT%2FC9l62zsNCw4CuhTq8hk0j7TMmZVAJJzfO4V2VVarFCpuo41uZ42v%2FOYPZZXW9no6Q3q6VsNzlpvVJHyXu6usJUUzF63wbrwapjZmko%2FtHfHfXhL4j%2F8I%2BVrddY3lM2To28Iq9ijOjbVMIDRg0iCXLaPfv3x5EjQOYSn9V%2Bnr%2Fyh%2FHl1rk6NSrsE2difXsUbZH%2FFxyCQI1vsK4%2BT6w%2FsfBz0jRuX6wQ2NWHyZl%2BfZ%2FRYupCdywHXwae9Myo0GtNgtqVeJbBLxIfwsbO2KeiWoFx9tNQmAqUl4BK2P3O%2BXLf7SWrIHqIOsmehSAOPXfNPWmk%2FdgaClhLFTWZ3HiFBY2g0w2Kmx1QY6pgFu30Twh096Acx7RPy6sc1ltr%2BXrws8KXPdCotq71frhbBl4ar6wksjOwAvOjIWRDhPGhmXqqpWz4r0e7D%2BJREPnT1WN035JwTl2bdg5k8KXc0RzlRzJ1z%2Fhiqb8RRcIv3sTrUnwkUgYPHLwVf8A%2FD28X2D8jta4g1PsDJUlD1k9ZSjFbYUXXYDxGFKGokrfBnSx6QhJatCiEKQoHJRJIwoCLx7j7NO&X-Amz-Signature=e2fda6be011392a1ebe458b7a3b6eaaed50d003c9a5ddb42aaf2a9958e2eaaa7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
