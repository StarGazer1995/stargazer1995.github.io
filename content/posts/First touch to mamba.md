---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM73YMY4%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWB8CtHJzbg%2Bz7KF0mDcZdTUVjDZZTCfp7XfZP%2FMNO4QIhAI9WxEboQ5nwbY%2BfHN1drZrG5qBgY%2FqhS54o325CMJsOKv8DCG0QABoMNjM3NDIzMTgzODA1Igy2whwkoHVY7Sg21tMq3AOFeSVGT5SUlPBNHGrdlGFjIMljo%2Bie0VQieeWyf%2BOZopr2G8vdy5Rha3O2KPgFPOvJ1iRhUpTVe1flzbxVJROdDS%2F%2F3vWl%2BGh1%2B1aecvd1KZx2W2%2BzyzdwfIUVZZfbuxufN2MFmhwh7xblspMc4wQ8lWBr%2BFMkPGeQdRGE8BShz%2BSCbD5%2BAlcDtWe%2B49r0mkWOz8aD%2FhcJzKPCrrcCwUYgRwrTKArK55%2B%2BHQrYq2YiL12OwRIhgUCiKlHCn3wvEJ5p2jSZiP%2B3rOv%2FmttzuTy8R3TuIsoCCFRLfyl1kSwIyh0WRxaI11TaEPhTgzUOcIYfklCaaU5OviYICbb3xgEYv2h6v%2BktecC3wdJyKCD23ltKgEi9XaP3flLItBcYXd1azvMyCrwy76fQlVjpWceEDSvA8qMGe31AQ9cTmqPXLh21ZG4IcSeR0byqTQ0c4equZ0QuJAHdWWgvds8t%2BgFs7ZAvGAQu1rCo0GkEG2qa5g4yu0GnQntKw4iZpqS5TudLiiSr7WJWxWKLLaIDv6IFj%2B%2F6Y7PAQytInKfr2Evcu%2BhcubDelZfoRe%2FqV3X47sb%2B2Wg5XM5W4L8NlJpY0PQ0pQQBhrs7YCxspLteD4rMzkYoSNdQSPG3a8zziDChvPvRBjqkAaYvOJAqvH5f588qCh9Sxd%2BzEkejSVjpwt6cot3HaIIdsqfWDNXkXsKGpGaxgqqvHzcVkmJ%2Bs%2FftJ2Sch4AzFamHhuYMvg%2BdeM0cqai7vyHibrnhm3VHYPeERDW0euFv%2FNRkpUyKKg2ZXkJCcCN6ZPlMHCY00v2yFiSZNUgBK1skCe4BaeQbgME7E%2FOwnCr2Y6UyVX8iJUXBK7TUL8NdImw4o%2B%2B2&X-Amz-Signature=32274e742d34aae6f9fa26b162803200cc43ff331edd60d1e44a75628cb8828b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
