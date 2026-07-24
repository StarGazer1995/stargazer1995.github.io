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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI7ZJAB4%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T225153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIGOrRxnFUsxEe15%2FxFAx16NOypGzAPGbKmcKMG%2F%2BMSF%2BAiEA9EaN%2BS79cO50KdKUsqWDffdJxnfjfIjT6kpDhJ8yrdUq%2FwMIDxAAGgw2Mzc0MjMxODM4MDUiDPDf4hvQ0jcKC1MuQircA6YtxeIJ0l1feCbl%2F%2F6AQ3XrZLOO6UoSLzS8w04voxN6F8S%2Fq58Cr%2Fwyg7mLBKwEIdIzGzYQ6TuFLOIvri8RIcFJiWjDiZdbiAHDUWuMoGvfcGVgcs9JOqA024Ayz2XSzn4tNDGo0bhQe53P5Jy8KDHKVvel9eRbHaoPK6B1QktnVwbPRK%2F0PSvkS6PGLYQJFj6B8Wi4vca42jgW6WyUabhLxp03YMremxsnB6oC4NRx5jFNQJ%2BY4fkTcKhV1X5eQBjGfkkHTrhJLZtWskxF17BAWp%2B5C8rPapsizYjCCx2fyNHrqZAyvf0iRGfUhi7HLwujXMcZxkM5v9FupaW8%2FYjrgS3hy%2BgXl9TmOaERCULcVbG%2F5bZ36v8zZqBUu37z7fjaBgPc%2FckYiBLFAr3uP5juYrFyE7e0tb%2FM3UoqNMxi1HkMJkw5P6Sar1xY7qTaVOtUvnt1Z6M7nENYqYAjV6bJl%2Fu5tRh2Gnp%2BuoIKiFG8wr%2F8uh3aY1HGmNKTuj3Dbcci79ZGa5NknsEar57ZBjU0I5QfSb7DduOPPfz8lTxIJdiEyrDtXe%2BCU3N0LpPGSyZSNPN58mBdQRwds%2BHkZJsY%2BbFJaU2yVv5MwYllXyambAEw6CGhwbBYeINQMOS4j9MGOqUBn2rkdS%2BS42pkgkH7r8E7kHW4YV9dcQ4MP4IcWUiSq2gmb4RXIZ6Qs8oU9YoX%2Br6D4YeTSZ%2FMaV7XWkks2yFleB%2BglTfEazGL8stxUd3hezgj52%2FygTtsOHVLjtNfjBqzYUanPz1aRrSYUeqyCeKdjh%2Bl7PBi%2FlB%2B9yRnAvtBWE5tKNDnen5pj7E1WRSln8lniriywi4Cr0aHsgH82WjwDtMHRS6g&X-Amz-Signature=f045bfdbbf47dca9e71beddecc29ecb421a71c2a8c50e2495e798377d2acecb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI7ZJAB4%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T225153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIGOrRxnFUsxEe15%2FxFAx16NOypGzAPGbKmcKMG%2F%2BMSF%2BAiEA9EaN%2BS79cO50KdKUsqWDffdJxnfjfIjT6kpDhJ8yrdUq%2FwMIDxAAGgw2Mzc0MjMxODM4MDUiDPDf4hvQ0jcKC1MuQircA6YtxeIJ0l1feCbl%2F%2F6AQ3XrZLOO6UoSLzS8w04voxN6F8S%2Fq58Cr%2Fwyg7mLBKwEIdIzGzYQ6TuFLOIvri8RIcFJiWjDiZdbiAHDUWuMoGvfcGVgcs9JOqA024Ayz2XSzn4tNDGo0bhQe53P5Jy8KDHKVvel9eRbHaoPK6B1QktnVwbPRK%2F0PSvkS6PGLYQJFj6B8Wi4vca42jgW6WyUabhLxp03YMremxsnB6oC4NRx5jFNQJ%2BY4fkTcKhV1X5eQBjGfkkHTrhJLZtWskxF17BAWp%2B5C8rPapsizYjCCx2fyNHrqZAyvf0iRGfUhi7HLwujXMcZxkM5v9FupaW8%2FYjrgS3hy%2BgXl9TmOaERCULcVbG%2F5bZ36v8zZqBUu37z7fjaBgPc%2FckYiBLFAr3uP5juYrFyE7e0tb%2FM3UoqNMxi1HkMJkw5P6Sar1xY7qTaVOtUvnt1Z6M7nENYqYAjV6bJl%2Fu5tRh2Gnp%2BuoIKiFG8wr%2F8uh3aY1HGmNKTuj3Dbcci79ZGa5NknsEar57ZBjU0I5QfSb7DduOPPfz8lTxIJdiEyrDtXe%2BCU3N0LpPGSyZSNPN58mBdQRwds%2BHkZJsY%2BbFJaU2yVv5MwYllXyambAEw6CGhwbBYeINQMOS4j9MGOqUBn2rkdS%2BS42pkgkH7r8E7kHW4YV9dcQ4MP4IcWUiSq2gmb4RXIZ6Qs8oU9YoX%2Br6D4YeTSZ%2FMaV7XWkks2yFleB%2BglTfEazGL8stxUd3hezgj52%2FygTtsOHVLjtNfjBqzYUanPz1aRrSYUeqyCeKdjh%2Bl7PBi%2FlB%2B9yRnAvtBWE5tKNDnen5pj7E1WRSln8lniriywi4Cr0aHsgH82WjwDtMHRS6g&X-Amz-Signature=2c98c1a721996f4f07d8d4faf91fe55db4a482b51ec91b7e2530d5cb83d93804&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
