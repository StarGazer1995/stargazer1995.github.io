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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVKW26Y7%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T120011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDsYpBiSXH7KIer9WLgLcZGRYajvPD%2F3iO%2BgGuN3NlQlwIgQw2ZTIUReLNZoxjNhv%2BBEAOLZeZpRexsu0OU%2F0WcuuMq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDOhK0sZ4TknZqXZXnSrcA%2BpRwRHZTDAiBaYi0AHFQN%2Fu7lGUO4ttQQ%2FlPughuI5XFISnXQukT2%2B9cBhn4p1oMmHCFzsnRqCIfTMeMzxPj8wwzHG9Mx71cikAFh6yh2enPFk4n%2BtpFSO2hvVPSaCeFWXqzasw1mrR2X%2BTjiZ4MMfb1xqYz5keZ%2B7FSYPMhLM7Mss2YNlBJAGP1Z9qipnZx2LJQx10uYOLWaLSouT78Q12UO9P1mAvDPBcy96cX4%2BSP%2FPgz8pjQx9HODRyoOY2s6hPmpByJ5jOqUThDnG6zgtKZUA2O2qAimZWqxqYTEVkWyLsJ0BA9tOsylOd%2FDTt%2FAsZyPNg3lTUVWUfLHUrlXmZW%2BuJqyxn8V1Yu8cnV1DX%2BrcimX7SXOLub%2B471ozQYDIQcI2y5FeC7K626DQFQSyDHeDyo0GQoJbjulc6WW2gI9w6NdxTAjGSNnZlmqbTdeBtUqR16q6Z7Aor3mPEeZx2yflU58sBMwbhH%2BlcG2I74eo4RYPz0ga5KQx2gmaELYtxa8V%2Fyz%2BmoX6RS%2BHlFU095QCVb49Y076MP6IDU64mZRkvtL2l80qwQu7RCO6zIjgpdLxCaBhvcQXehefi06PUQyV9RxMe%2FoQrAdvUEnCjok3oli1z132g0YjiMP6ontIGOqUBTmQXg3U2rSMenwb98BmwJ4goKbbRZ2%2B9EndziO%2Fi8ndV6t7fyzgg5PdLveDVE8qIkfmvmWoI9qKp6HfNHhfO4b0xxWr91jrS3nEj4yigNeBsWZwExxXmwgl%2BWwtHITRwWST%2BgS%2FdRTROK1TYPvOH81Hs4g4BKnt%2BS9l66ihi%2BySXwVZq1Z8jJ5Zc%2FzslqkdFhBfJXKKaL4l%2Fwj6t%2F6tSa8Yd5R92&X-Amz-Signature=828a7aec2c94aa530888164453a67f3f6f236146d44c4093905483473da00a42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVKW26Y7%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T120011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDsYpBiSXH7KIer9WLgLcZGRYajvPD%2F3iO%2BgGuN3NlQlwIgQw2ZTIUReLNZoxjNhv%2BBEAOLZeZpRexsu0OU%2F0WcuuMq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDOhK0sZ4TknZqXZXnSrcA%2BpRwRHZTDAiBaYi0AHFQN%2Fu7lGUO4ttQQ%2FlPughuI5XFISnXQukT2%2B9cBhn4p1oMmHCFzsnRqCIfTMeMzxPj8wwzHG9Mx71cikAFh6yh2enPFk4n%2BtpFSO2hvVPSaCeFWXqzasw1mrR2X%2BTjiZ4MMfb1xqYz5keZ%2B7FSYPMhLM7Mss2YNlBJAGP1Z9qipnZx2LJQx10uYOLWaLSouT78Q12UO9P1mAvDPBcy96cX4%2BSP%2FPgz8pjQx9HODRyoOY2s6hPmpByJ5jOqUThDnG6zgtKZUA2O2qAimZWqxqYTEVkWyLsJ0BA9tOsylOd%2FDTt%2FAsZyPNg3lTUVWUfLHUrlXmZW%2BuJqyxn8V1Yu8cnV1DX%2BrcimX7SXOLub%2B471ozQYDIQcI2y5FeC7K626DQFQSyDHeDyo0GQoJbjulc6WW2gI9w6NdxTAjGSNnZlmqbTdeBtUqR16q6Z7Aor3mPEeZx2yflU58sBMwbhH%2BlcG2I74eo4RYPz0ga5KQx2gmaELYtxa8V%2Fyz%2BmoX6RS%2BHlFU095QCVb49Y076MP6IDU64mZRkvtL2l80qwQu7RCO6zIjgpdLxCaBhvcQXehefi06PUQyV9RxMe%2FoQrAdvUEnCjok3oli1z132g0YjiMP6ontIGOqUBTmQXg3U2rSMenwb98BmwJ4goKbbRZ2%2B9EndziO%2Fi8ndV6t7fyzgg5PdLveDVE8qIkfmvmWoI9qKp6HfNHhfO4b0xxWr91jrS3nEj4yigNeBsWZwExxXmwgl%2BWwtHITRwWST%2BgS%2FdRTROK1TYPvOH81Hs4g4BKnt%2BS9l66ihi%2BySXwVZq1Z8jJ5Zc%2FzslqkdFhBfJXKKaL4l%2Fwj6t%2F6tSa8Yd5R92&X-Amz-Signature=6a3253f367bf7522a02bd47ce5bf0e1f471cf97721eaacc1e053fa3952ba8886&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
